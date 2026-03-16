# Solver Settings

Gradient Dynamics offers two classes of CFD solver: **density-based** and **pressure-based**. For most applications, the density-based solver is recommended — it is purpose-built for GPU-native execution and delivers the best performance on cloud hardware.

## Solver Types

### Density-Based (Recommended)

The density-based solver solves the fully coupled compressible Navier-Stokes equations — continuity, momentum, and energy — as a unified system. Density, momentum, and total energy are the primary solution variables; pressure is derived from the equation of state.

**Why it performs better on GPUs:**

The density-based formulation is naturally suited to GPU architecture because:

- All governing equations are updated simultaneously in a single sweep, enabling fully parallel execution across all mesh cells
- Explicit time-marching schemes (Runge-Kutta) have no global coupling — each cell update depends only on its neighbors, matching the GPU's massively parallel execution model
- The structured Cartesian block mesh provides regular, coalesced memory access patterns that maximize GPU memory bandwidth utilization
- No iterative pressure-velocity coupling loops (as in SIMPLE/PISO) means minimal divergence of parallel execution threads

The result is near-linear strong scaling across GPU cores and predictable, fast runtimes even on large meshes.

**When to use density-based:**
- External aerodynamics (vehicles, aircraft, buildings)
- Internal flows at moderate-to-high Reynolds numbers
- Compressible flows (any Mach number)
- High-fidelity RANS, URANS, LES, or DES
- Any case where GPU performance is a priority (i.e., most cases)

```{admonition} Low-Mach Preconditioning
:class: note
The density-based solver includes low-Mach preconditioning, which maintains accuracy and conditioning for nearly-incompressible flows (M < 0.1). You do not need to switch to a pressure-based solver for low-speed flows.
```

#### Time-Marching Schemes

| Scheme | Description | Best For |
|--------|-------------|----------|
| **Explicit (Runge-Kutta)** | Multi-stage explicit time stepping; maximum GPU parallelism | Steady RANS, LES, high-accuracy transient |
| **Implicit** | Larger stable time steps; better for stiff problems | Difficult geometries, strongly coupled physics |

The default is **explicit Runge-Kutta** for steady and transient RANS, and **explicit** for LES. Switch to implicit only if the explicit scheme has convergence difficulties.

#### CFL Number

The **CFL number** (Courant-Friedrichs-Lewy) controls the time step size for explicit schemes.

| CFL Setting | Description |
|-------------|-------------|
| 0.5 – 1.0 | Conservative — use for difficult starting conditions |
| 1.0 – 2.0 | Standard for steady RANS (default: 1.5) |
| 2.0 – 5.0 | Aggressive — faster convergence, higher risk of divergence |

The solver computes a local time step at each cell based on the CFL criterion. CFL ramping is applied automatically: the solver starts at a low CFL and ramps up as the solution stabilizes.

#### Flux Scheme

| Scheme | Description | Best For |
|--------|-------------|----------|
| **Roe** | Approximate Riemann solver; captures shocks well | Transonic and supersonic flows |
| **AUSM+** | Low-dissipation; better for low-Mach accuracy | Subsonic aerodynamics (default) |
| **HLLC** | Robust; good all-around performance | General purpose |

#### Spatial Order

| Order | Description |
|-------|-------------|
| **1st order** | Robust, fast — good for startup iterations |
| **2nd order** | Default for production runs — accurate, bounded |
| **3rd order MUSCL** | High-accuracy for LES and detailed analysis |

The solver automatically transitions from 1st to 2nd order after the solution has stabilized (order ramping).

---

### Pressure-Based

The pressure-based solver uses a segregated pressure-velocity coupling approach (SIMPLE or PIMPLE algorithms) and solves the incompressible Navier-Stokes equations. This solver is available for cases where an incompressible formulation is strictly required.

```{admonition} Performance Note
:class: warning
The pressure-based solver requires iterative pressure Poisson solves that involve global communication across the mesh, limiting GPU parallelism. For most applications, the density-based solver with low-Mach preconditioning delivers equivalent accuracy with significantly better GPU performance. The pressure-based solver is provided for compatibility but is not recommended as the primary solver.
```

**When to use pressure-based:**
- Strictly incompressible flows where density variation is physically meaningless
- Compatibility with specific post-processing or validation workflows

#### Pressure-Velocity Coupling

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **SIMPLE** | Semi-Implicit Method for Pressure-Linked Equations | Steady-state RANS |
| **PIMPLE** | Hybrid SIMPLE/PISO | Transient with large time steps |

#### Relaxation Factors

Under-relaxation factors control how aggressively the solution is updated each iteration. Lower values are more stable but converge slower.

| Field | k-ω SST | k-ε | Spalart-Allmaras |
|-------|---------|-----|-----------------|
| **Velocity (U)** | 0.5 | 0.6 | 0.6 |
| **Pressure (p)** | 0.2 | 0.3 | 0.3 |
| **k** | 0.4 | 0.4 | — |
| **ω / ε** | 0.4 | 0.4 | — |
| **Turbulent viscosity** | 0.05 | 0.1 | 0.1 |

---

## Linear Solver

Both solver types use iterative linear solvers for implicit systems.

### Preconditioners

| Preconditioner | Description | Performance |
|---------------|-------------|-------------|
| **AMG** | Algebraic Multigrid (default) | Best for large meshes |
| **Chebyshev** | Polynomial smoothing | Good with AMG as smoother |
| **Jacobi** | Diagonal scaling | Fast per iteration; good on GPU |

**AMG with Jacobi or Chebyshev smoothing** is the default. For the density-based solver, the explicit scheme bypasses the linear solver entirely for most fields — preconditioning only applies to implicit residual smoothing steps.

## Convergence Criteria

### Density-Based Convergence

Convergence is monitored via the **L2 norm of the density residual** and integrated force/moment quantities.

| Metric | Threshold | Description |
|--------|-----------|-------------|
| **Density residual** | < 1e-5 | Primary convergence indicator |
| **Force coefficient plateau** | < 0.1% change over 100 iterations | Engineering convergence |

The simulation stops when residuals drop below the threshold **and** force coefficients have plateaued.

### Pressure-Based Convergence

| Residual | Default Threshold | Description |
|----------|------------------|-------------|
| **Continuity** | 1e-4 | Mass conservation |
| **Velocity** | 1e-5 | Momentum equations |
| **Turbulence** | 1e-5 | Turbulence transport |

### Plateau Detection

Studio automatically detects when residuals have plateaued and can terminate early, even if the absolute threshold hasn't been reached. This is useful for complex flows where residuals stabilize above the threshold while the solution is physically converged.

## Startup Controls

### CFL Ramping (Density-Based)

The solver automatically ramps the CFL number from a low starting value (typically 0.1–0.5) up to the target CFL over the first 50–200 iterations. This establishes a stable initial flow field before pushing the time step to the maximum stable value.

You can adjust the ramp rate if the default leads to early divergence.

### Turbulence Ramping

For difficult cases, the solver can gradually introduce turbulence equations:

1. **Start iteration** — Iteration at which turbulence equations are activated
2. **Ramp iterations** — Iterations to blend from laminar to fully turbulent

Use this when:
- The initial iterations diverge immediately
- Complex geometries with sharp features cause early instability

## Troubleshooting Convergence

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| Immediate divergence (density-based) | CFL too high | Reduce target CFL; enable CFL ramping |
| Immediate divergence (pressure-based) | Relaxation too aggressive | Reduce relaxation factors by 30% |
| Oscillating residuals | Mesh quality or boundary condition issue | Check mesh quality; verify BCs |
| Slow convergence | CFL too conservative / relaxation too low | Gradually increase CFL or relaxation |
| Turbulence residuals stuck | Poor initialization | Enable turbulence ramping |
| Force coefficients not plateauing | Flow not yet periodic | Extend iteration count; check domain size |
