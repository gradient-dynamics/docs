# Advanced solver controls

```{py:currentmodule} gradientdynamics.fluxcore
```

FluxCore is a complete GPU-native CFD and multiphysics solver. Its typed control
objects expose physical models, nonlinear progression, time advancement,
GPU-native linear-system solution, multigrid policy, monitoring and result
production without exposing the proprietary algorithms beneath them.

Automatic settings are the recommended starting point. Expert controls are
available for verification, difficult meshes, time-resolved studies and
repeatable production workflows.

```{note}
FluxCore is not a repackaging of a conventional segregated CPU solver. The
simulation path—from equation assembly through convergence assessment and
result production—is designed for GPU execution as one coordinated system.
```

## Aggregate configuration

````{py:class} AdvancedControls(*, spatial: SpatialControls | None = None, progression: ProgressionControls | None = None, convergence: ConvergenceCriteria | None = None, turbulence: TurbulenceModel | None = None, time: SteadyTimeControls | PhysicalTimeControls | None = None, linear_solvers: LinearSolverSet | None = None, outputs: OutputControls | None = None, rotating_zones: Sequence[RotatingZone] = (), thermal: ThermalControls | None = None, checkpoints: CheckpointControls | None = None, compute: ComputePreference | None = None)

Optional expert controls attached to {py:class}`SimulationConfig`.

Unspecified groups use FluxCore's validated automatic policies. The detailed
objects are documented under {doc}`turbulence`, {doc}`time-integration`,
{doc}`linear-solvers` and {doc}`output-controls`.

```{py:method} production() -> AdvancedControls
:classmethod:

Create balanced production defaults with automatic stability management,
convergence monitoring and checkpointing.
```

```{py:method} validation() -> AdvancedControls
:classmethod:

Create stricter reporting and convergence defaults for verification and
validation work.
```
````

## Spatial controls

````{py:class} SpatialControls(*, accuracy: str = "second_order", boundedness: str = "automatic", gradient_quality: str = "enhanced", non_orthogonal_handling: str = "automatic", wall_resolution: str = "resolved")

Accuracy and robustness policy for spatial operators on polyhedral meshes.

```{py:attribute} accuracy
:type: Literal["first_order", "second_order"]

Requested formal spatial accuracy. First order is intended for diagnosis and
initialisation, not final production results.
```

```{py:attribute} boundedness
:type: Literal["automatic", "strict", "low_dissipation"]

Policy for maintaining physical states near steep gradients and difficult
cells.
```

```{py:attribute} gradient_quality
:type: Literal["standard", "enhanced"]

Gradient accuracy policy for irregular polyhedra and boundary-layer cells.
```

```{py:attribute} non_orthogonal_handling
:type: Literal["automatic", "conservative", "aggressive"]

Treatment level for non-orthogonal and skewed cells.
```
````

## Nonlinear progression

````{py:class} ProgressionControls(*, initial_cfl: float = 1.0, target_cfl: float = 100.0, ramp_iterations: int = 500, growth_factor: float = 1.25, retreat_factor: float = 0.5, update_limit: float | None = None, adaptive: bool = True, recovery: str = "automatic")

Controls how a steady or inner transient solve advances from a robust startup
state toward high-throughput convergence.

```{py:attribute} initial_cfl
:type: float

Starting pseudo-time Courant number.
```

```{py:attribute} target_cfl
:type: float

Maximum requested pseudo-time Courant number after successful progression.
```

```{py:attribute} ramp_iterations
:type: int

Nominal pseudo-iterations over which the target is earned.
```

```{py:attribute} growth_factor
:type: float

Maximum CFL growth after a successful convergence window.
```

```{py:attribute} retreat_factor
:type: float

CFL multiplier used after a rejected or unstable update.
```

```{py:attribute} adaptive
:type: bool

Allow FluxCore to advance or retreat based on observed nonlinear behaviour.
```

```{py:attribute} recovery
:type: Literal["automatic", "strict", "disabled"]

Policy when an attempted update does not satisfy stability and progress gates.
```
````

## Convergence criteria

````{py:class} ConvergenceCriteria(*, residual: float = 1e-6, minimum_iterations: int = 100, monitor_window: int = 50, mass_imbalance: float | None = 1e-4, energy_imbalance: float | None = None, force_coefficient_delta: float | None = None, heat_balance: float | None = None, require_all: bool = True)

Multi-signal definition of a converged engineering state.

```{py:attribute} residual
:type: float

Normalised equation-residual target.
```

```{py:attribute} mass_imbalance
:type: float | None

Optional domain mass-balance tolerance.
```

```{py:attribute} energy_imbalance
:type: float | None

Optional energy-balance tolerance for thermal and CHT workflows.
```

```{py:attribute} force_coefficient_delta
:type: float | None

Maximum change in a monitored coefficient across the rolling window.
```

```{py:attribute} heat_balance
:type: float | None

Optional normalised heat-flux balance target across selected interfaces.
```

```{py:attribute} require_all
:type: bool

Require every enabled criterion rather than residual reduction alone.
```
````

## Rotating zones

````{py:class} RotatingZone(*, zone: str, axis: tuple[float, float, float], angular_speed: float, origin: tuple[float, float, float] = (0.0, 0.0, 0.0), rotating_patches: Sequence[str] = (), stationary_patches: Sequence[str] = ())

Moving-reference-frame definition for fans, pumps and turbomachinery.

```{py:attribute} zone
:type: str

Named mesh cell zone.
```

```{py:attribute} axis
:type: tuple[float, float, float]
```

```{py:attribute} angular_speed
:type: float

Angular speed in radians per second.
```
````

## Thermal coupling

````{py:class} ThermalControls(*, specific_heat: float | None = None, laminar_prandtl: float = 0.71, turbulent_prandtl: float = 0.85, wall_heat_transfer: str = "automatic", contact_resistance: Mapping[tuple[str, str], float] | None = None, outer_iterations: int | None = None, outer_tolerance: float | None = None)

Fluid energy and multi-region solid-coupling policy.

```{py:attribute} contact_resistance
:type: Mapping[tuple[str, str], float] | None

Optional thermal contact resistance for named region-interface pairs.
```

```{py:attribute} outer_iterations
:type: int | None

Maximum fluid–solid coupling transactions.
```

```{py:attribute} outer_tolerance
:type: float | None

Coupled temperature and heat-flux convergence target.
```
````

## Checkpoints and restart

````{py:class} CheckpointControls(*, every_pseudo_steps: int | None = 250, every_physical_steps: int | None = 25, keep_last: int = 2, resume_from: str | Path | None = None, restart_required: bool = False, export_final_state: bool = True)

Checkpoint, warm-start and restart policy.

```{py:attribute} every_pseudo_steps
:type: int | None

Checkpoint cadence for steady pseudo-time advancement.
```

```{py:attribute} every_physical_steps
:type: int | None

Checkpoint cadence for physical-time simulations.
```

```{py:attribute} resume_from
:type: str | Path | None

Compatible steady or transient state used to initialise the run.
```

```{py:attribute} restart_required
:type: bool

Fail instead of starting from the default initial state if a requested
checkpoint is missing or incompatible.
```
````

## Compute selection

````{py:class} ComputePreference(*, accelerator: str = "auto", device_count: int | str = "auto", precision: str = "automatic", memory_profile: str = "balanced", partitioning: str = "automatic")

Managed GPU-capacity preference. Availability is organisation-specific.

```{py:attribute} accelerator
:type: Literal["auto", "a100", "h100", "b200"]
```

```{py:attribute} device_count
:type: int | Literal["auto"]
```

```{py:attribute} memory_profile
:type: Literal["balanced", "capacity", "throughput"]
```

```{py:attribute} partitioning
:type: Literal["automatic", "geometry", "balanced"]

High-level distribution policy for supported multi-GPU runs.
```
````

## Composed example

```python
from gradientdynamics.fluxcore import (
    AdvancedControls,
    CheckpointControls,
    ComputePreference,
    ConvergenceCriteria,
    ProgressionControls,
    SpatialControls,
)

advanced = AdvancedControls(
    spatial=SpatialControls(accuracy="second_order", gradient_quality="enhanced"),
    progression=ProgressionControls(
        initial_cfl=1.0,
        target_cfl=200.0,
        ramp_iterations=800,
        adaptive=True,
    ),
    convergence=ConvergenceCriteria(
        residual=1e-7,
        mass_imbalance=1e-5,
        force_coefficient_delta=2e-5,
        monitor_window=100,
    ),
    turbulence=turbulence,
    time=time_controls,
    linear_solvers=linear_solvers,
    outputs=output_controls,
    checkpoints=CheckpointControls(
        every_pseudo_steps=250,
        every_physical_steps=25,
        keep_last=3,
    ),
    compute=ComputePreference(
        accelerator="h100",
        device_count="auto",
        memory_profile="throughput",
    ),
)
```

The four variables composed above are fully defined on the dedicated API
pages. The public surface communicates FluxCore's depth while its algorithms,
GPU kernels, data structures and solver architecture remain proprietary.
