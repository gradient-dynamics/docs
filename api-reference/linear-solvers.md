# Linear solvers and multigrid

```{py:currentmodule} gradientdynamics.fluxcore
```

FluxCore's nonlinear physics creates several large sparse systems with
different numerical character. The API can assign a typed GPU-native linear
policy to the primary coupled system, turbulence transport, fluid energy and
solid energy while retaining an automatic production default.

These objects configure convergence behaviour and computational budgets. They
do not reveal FluxCore's proprietary algorithms, GPU kernels or data layout.

## Shared convergence policy

````{py:class} LinearConvergence(*, relative_tolerance: float = 1e-3, absolute_tolerance: float | None = None, maximum_iterations: int = 200, minimum_iterations: int = 1, stagnation_window: int = 12, residual_growth_limit: float = 10.0, report_every: int = 10)

Stopping and protection criteria for one linear-system transaction.

```{py:attribute} relative_tolerance
:type: float

Required reduction relative to the initial linear residual.
```

```{py:attribute} absolute_tolerance
:type: float | None

Optional absolute residual floor.
```

```{py:attribute} maximum_iterations
:type: int

Iteration safety budget for one transaction.
```

```{py:attribute} stagnation_window
:type: int

Samples used to distinguish progress from stagnation.
```

```{py:attribute} residual_growth_limit
:type: float

Growth threshold that triggers protective recovery.
```
````

## Iterative linear solver

````{py:class} IterativeLinearSolver(*, convergence: LinearConvergence = LinearConvergence(), precision: str = "automatic", relaxation: float = 1.0, restart_budget: int = 3, recovery: str = "automatic")

General GPU-native iterative policy.

```{py:attribute} precision
:type: Literal["automatic", "mixed", "double"]

Precision policy. Automatic balances throughput with achieved convergence on
the selected GPU generation.
```

```{py:attribute} relaxation
:type: float

Linear update multiplier.
```

```{py:attribute} restart_budget
:type: int

Maximum automatic restart transactions before control returns to the enclosing
nonlinear step.
```

```{py:attribute} recovery
:type: Literal["automatic", "strict", "fail_fast"]

Behaviour after stagnation, loss of finite state or excessive residual growth.
```
````

## Multigrid hierarchy

````{py:class} MultigridCycle

```{py:attribute} V
:value: "v"
```

```{py:attribute} W
:value: "w"
```

```{py:attribute} F
:value: "f"
```
````

````{py:class} MultigridControls(*, maximum_levels: int = 20, minimum_coarse_size: int = 8, cycle: MultigridCycle | str = "v", pre_sweeps: int = 1, post_sweeps: int = 1, coarse_iterations: int = 50, coarse_tolerance: float = 0.1, relaxation: float = 0.75, smoother: str = "automatic", rebuild: str = "automatic", freeze_after_pseudo_step: int | None = 300)

GPU-resident hierarchy and cycling policy.

```{py:attribute} maximum_levels
:type: int

Maximum hierarchy depth. Construction stops earlier when the coarse-size
criterion is met.
```

```{py:attribute} minimum_coarse_size
:type: int

Minimum aggregate size used while constructing coarse levels.
```

```{py:attribute} cycle
:type: MultigridCycle | Literal["v", "w", "f"]

Traversal used across hierarchy levels.
```

```{py:attribute} pre_sweeps
:type: int

Smoothing passes before coarse-level correction.
```

```{py:attribute} post_sweeps
:type: int

Smoothing passes after coarse-level correction.
```

```{py:attribute} coarse_iterations
:type: int

Iteration budget on the coarsest active level.
```

```{py:attribute} smoother
:type: Literal["automatic", "point", "block"]

High-level smoothing policy. Automatic is recommended across mixed physics.
```

```{py:attribute} rebuild
:type: Literal["automatic", "every_step", "frozen"]

Hierarchy refresh policy as nonlinear coefficients and physical time evolve.
```

```{py:attribute} freeze_after_pseudo_step
:type: int | None

Allow reuse after the hierarchy has stabilised for the requested number of
pseudo-steps. Set to `None` to keep automatic rebuild decisions active.
```
````

````{py:class} MultigridLinearSolver(*, convergence: LinearConvergence = LinearConvergence(), multigrid: MultigridControls = MultigridControls(), maximum_cycles: int = 15, precision: str = "automatic", recovery: str = "automatic")

GPU-native multigrid linear policy.

```{py:attribute} maximum_cycles
:type: int

Maximum hierarchy cycles for one linear transaction.
```

```{py:attribute} multigrid
:type: MultigridControls

Hierarchy construction, traversal and smoothing controls.
```
````

## Per-system assignment

````{py:class} LinearSolverSet(*, primary: IterativeLinearSolver | MultigridLinearSolver | None = None, turbulence: IterativeLinearSolver | MultigridLinearSolver | None = None, fluid_energy: IterativeLinearSolver | MultigridLinearSolver | None = None, solid_energy: IterativeLinearSolver | MultigridLinearSolver | None = None, default: IterativeLinearSolver | MultigridLinearSolver | None = None)

Linear policies assigned by equation group.

```{py:attribute} primary
:type: IterativeLinearSolver | MultigridLinearSolver | None

Policy for the primary coupled flow system.
```

```{py:attribute} turbulence
:type: IterativeLinearSolver | MultigridLinearSolver | None

Policy for turbulence transport equations.
```

```{py:attribute} fluid_energy
:type: IterativeLinearSolver | MultigridLinearSolver | None

Policy for the fluid energy equation in thermal simulations.
```

```{py:attribute} solid_energy
:type: IterativeLinearSolver | MultigridLinearSolver | None

Policy for solid-region conduction systems.
```

```{py:attribute} default
:type: IterativeLinearSolver | MultigridLinearSolver | None

Fallback for equation groups without an explicit policy. Omit all policies to
use FluxCore's validated automatic selection.
```
````

## Multigrid example

```python
from gradientdynamics.fluxcore import (
    IterativeLinearSolver,
    LinearConvergence,
    LinearSolverSet,
    MultigridControls,
    MultigridLinearSolver,
)

flow_solver = MultigridLinearSolver(
    convergence=LinearConvergence(
        relative_tolerance=1e-4,
        maximum_iterations=250,
        stagnation_window=16,
    ),
    multigrid=MultigridControls(
        maximum_levels=16,
        cycle="v",
        pre_sweeps=2,
        post_sweeps=2,
        coarse_iterations=60,
        smoother="block",
        rebuild="automatic",
    ),
    maximum_cycles=20,
    precision="automatic",
)

transport_solver = IterativeLinearSolver(
    convergence=LinearConvergence(
        relative_tolerance=5e-4,
        maximum_iterations=120,
    ),
    recovery="automatic",
)

linear_solvers = LinearSolverSet(
    primary=flow_solver,
    turbulence=transport_solver,
    fluid_energy=flow_solver,
    solid_energy=flow_solver,
)
```
