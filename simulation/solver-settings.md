# Solver Settings

Gradient Dynamics provides a comprehensive suite of CFD solvers covering compressible and incompressible flows, explicit and implicit time integration, and both segregated and coupled solution strategies. All solvers are purpose-built for GPU-native execution on structured Cartesian block-AMR meshes.

## Solver Classification

Solvers in Gradient Dynamics are categorized along three independent axes:

| Axis | Options | Description |
|------|---------|-------------|
| **Flow regime** | Compressible, Incompressible | Whether density variations are significant |
| **Time integration** | Explicit, Implicit, Hybrid | How the solution advances in time |
| **Coupling strategy** | Coupled, Segregated | Whether equations are solved together or sequentially |

The combination you choose determines the solver algorithm. Studio exposes the most commonly used combinations; the AI Assistant can recommend the best match for your application.

---

## Density-Based Solver (Recommended)

The density-based solver solves the fully coupled compressible Navier-Stokes equations — continuity, momentum, and energy — as a unified system. Density, momentum, and total energy are the primary solution variables; pressure is derived from the equation of state.

This is the **recommended solver** for the vast majority of applications. It is natively designed for GPU hardware and delivers the best performance.

**Why it performs better on GPUs:**

- All governing equations are updated simultaneously in a single sweep, enabling fully parallel execution across all mesh cells
- Explicit time-marching schemes (Runge-Kutta) have no global coupling — each cell update depends only on its neighbors, matching the GPU's massively parallel execution model
- The structured Cartesian block mesh provides regular, coalesced memory access patterns that maximize GPU memory bandwidth utilization
- No iterative pressure-velocity coupling loops means minimal divergence of parallel execution threads

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

### Time-Marching Schemes

| Scheme | Type | Description | Best For |
|--------|------|-------------|----------|
| **SSP-RK3** | Explicit | Strong stability preserving 3rd-order Runge-Kutta; maximum GPU parallelism | Steady RANS, LES, high-accuracy transient (default) |
| **Explicit Euler** | Explicit | First-order explicit; simplest and most robust | Initial startup, debugging |
| **Implicit Euler** | Implicit | Larger stable time steps; better for stiff problems | Difficult geometries, strongly coupled physics |

The default is **SSP-RK3** (explicit) for steady and transient RANS, and for LES. Switch to implicit only if the explicit scheme has convergence difficulties or if very large time steps are required.

### CFL Number

The **CFL number** (Courant-Friedrichs-Lewy) controls the time step size for explicit schemes.

| CFL Setting | Description |
|-------------|-------------|
| 0.5 – 1.0 | Conservative — use for difficult starting conditions |
| 1.0 – 2.0 | Standard for steady RANS (default: 1.5) |
| 2.0 – 5.0 | Aggressive — faster convergence, higher risk of divergence |

The solver computes a local time step at each cell based on the CFL criterion. **CFL ramping** is applied automatically: the solver starts at a low CFL (typically 0.1) and ramps up to the target over the first 50–200 iterations as the solution stabilizes.

### Flux Schemes

The flux scheme determines how flow quantities are evaluated at cell faces — a critical choice for accuracy and stability.

| Scheme | Description | Best For |
|--------|-------------|----------|
| **AUSM+** | Low-dissipation Mach-number splitting; accurate at low Mach | Subsonic aerodynamics (default) |
| **AUSM+UP** | Enhanced AUSM+ with pressure-based dissipation for all-speed flows | Mixed low/high Mach flows |
| **HLLC** | Harten-Lax-van Leer with contact restoration; robust shock capturing | General purpose, transonic flows |
| **Roe** | Linearized approximate Riemann solver; sharp shock resolution | Transonic and supersonic flows |
| **Rusanov** | Most dissipative but most robust; Lax-Friedrichs type | Startup, very difficult flows |
| **SLAU2** | Simple Low-dissipation AUSM; excellent for low-Mach accuracy | Low-speed external aerodynamics |

### Reconstruction and Spatial Order

Higher-order spatial reconstruction improves accuracy by reconstructing the solution at cell faces from neighboring cell values.

| Scheme | Order | Description |
|--------|-------|-------------|
| **1st order** | 1 | No reconstruction — robust, dissipative; good for startup |
| **MUSCL** | 2nd | Monotone Upstream-centered Scheme for Conservation Laws — accurate, bounded (default) |
| **WENO3** | 3rd | Weighted Essentially Non-Oscillatory — high-accuracy, shock-safe |
| **WENO5** | 5th | Fifth-order WENO — maximum accuracy for LES and detailed analysis |

The solver can automatically transition from 1st to 2nd order after the solution has stabilized (order ramping).

#### Slope Limiters

Limiters prevent unphysical oscillations near shocks and steep gradients when using higher-order reconstruction.

| Limiter | Description |
|---------|-------------|
| **Van Leer** | Good balance of accuracy and robustness (default) |
| **Minmod** | Most dissipative — safest for difficult flows |
| **Superbee** | Least dissipative — sharpest gradients, higher oscillation risk |
| **Van Albada** | Smooth limiter — good for smooth subsonic flows |
| **Venkatakrishnan** | Standard for unstructured CFD; converges well |
| **Barth-Jespersen** | Strictly enforces monotonicity — most robust for shocks |

### Wall Treatment

The density-based solver supports several wall treatment approaches for resolving or modelling the near-wall boundary layer on Cartesian cut-cell meshes.

| Wall Treatment | Description | Best For |
|----------------|-------------|----------|
| **None** | Wall-resolved — no modelling; relies on fine near-wall AMR | LES, y+ ≈ 1 simulations |
| **Spalding** | Continuous wall function valid across the full y+ range | General-purpose RANS (default) |
| **Reichardt** | Similar to Spalding; slightly different blending profile | Alternative for RANS |
| **Linelets** | Embedded 1D wall-normal profiles within each near-wall cell | High-accuracy wall treatment on coarser meshes |

```{admonition} Linelets
:class: tip
The linelet wall treatment embeds a one-dimensional sub-grid within each near-wall cell, solving the boundary layer profile locally without requiring the global mesh to resolve it. This gives wall-resolved accuracy at wall-function mesh resolution — particularly effective on Cartesian cut-cell meshes where traditional boundary layer extrusion is not used.
```

---

## Pressure-Based Solver

The pressure-based solver uses a **segregated** approach, solving the momentum and pressure equations sequentially through a pressure-velocity coupling algorithm. It solves the incompressible Navier-Stokes equations and is available for cases where an incompressible formulation is specifically required.

```{admonition} Performance Note
:class: warning
The pressure-based solver requires iterative pressure Poisson solves that involve global communication across the mesh, limiting GPU parallelism. For most applications, the density-based solver with low-Mach preconditioning delivers equivalent accuracy with significantly better GPU performance. The pressure-based solver is provided for compatibility but is not recommended as the primary solver.
```

**When to use pressure-based:**
- Strictly incompressible flows where density variation is physically meaningless
- Compatibility with specific validation workflows that require a pressure-based formulation

### Pressure-Velocity Coupling Algorithms

The pressure-velocity coupling algorithm determines how the segregated momentum and pressure equations interact.

| Algorithm | Type | Description | Best For |
|-----------|------|-------------|----------|
| **SIMPLE** | Segregated, Implicit | Semi-Implicit Method for Pressure-Linked Equations; solves momentum then corrects pressure | Steady-state RANS (default) |
| **SIMPLEC** | Segregated, Implicit | SIMPLE-Consistent; improved pressure correction with less under-relaxation needed | Faster steady-state convergence |
| **PISO** | Segregated, Implicit | Pressure-Implicit with Splitting of Operators; multiple pressure corrections per step | Transient flows, small time steps |
| **PIMPLE** | Segregated, Implicit | Hybrid SIMPLE + PISO; outer SIMPLE loops with inner PISO corrections | Transient with large time steps; most stable |

```{tip}
For steady RANS, use **SIMPLE** or **SIMPLEC**. For transient simulations (URANS, LES, DES), use **PISO** or **PIMPLE**. PIMPLE is the most stable option for complex transient flows.
```

### Relaxation Factors

Under-relaxation factors control how aggressively the solution is updated each iteration. Lower values are more stable but converge slower. The solver automatically applies model-appropriate defaults.

| Field | k-ω SST | k-ε | Spalart-Allmaras | RSM |
|-------|---------|-----|-----------------|-----|
| **Velocity (U)** | 0.3 | 0.3 | 0.4 | 0.2 |
| **Pressure (p)** | 0.1 | 0.1 | 0.15 | 0.08 |
| **k** | 0.3 | 0.3 | — | 0.3 |
| **ω / ε** | 0.3 | 0.3 | — | 0.3 |
| **ν̃ (SA variable)** | — | — | 0.4 | — |
| **Turbulent viscosity** | 0.1 | 0.1 | 0.1 | 0.1 |

---

## Coupled Solver

The coupled solver solves the momentum and pressure equations simultaneously as a single block system, rather than sequentially as in the segregated approach. This eliminates the need for pressure-velocity coupling iterations and can converge significantly faster for strongly coupled flows.

**When to use coupled:**
- Flows where pressure and velocity are tightly coupled (high-speed internal flows, strong buoyancy)
- Cases where the segregated approach requires excessive iterations to converge
- Complex multi-physics simulations

```{admonition} Coupled vs Segregated
:class: note
The **segregated** approach (SIMPLE, PISO, etc.) solves each equation in sequence and iterates to convergence. The **coupled** approach solves momentum and pressure together in a single matrix system. Coupled is more robust for difficult flows but uses more memory per iteration. For most standard simulations, the density-based solver remains the recommended first choice.
```

---

## FSAC (Fractional Step Artificial Compressibility)

The **FSAC** method is a hybrid explicit-implicit approach that combines the efficiency of explicit time marching with an artificial compressibility formulation for pressure. It bridges the gap between fully explicit density-based solvers and fully implicit pressure-based methods.

**How it works:**
1. The momentum equations are advanced explicitly using a fractional step approach
2. An artificial compressibility term is added to the continuity equation, allowing pressure waves to propagate at a finite (artificial) speed
3. The pressure field is updated without requiring a global Poisson solve

**When to use FSAC:**
- Incompressible flows where you want the GPU performance benefits of an explicit approach
- Cases where the density-based solver's compressible formulation is unnecessary but the pressure-based solver is too slow
- Transitional flows between low-speed and moderate-speed regimes

---

## ACM (Artificial Compressibility Method)

The **ACM** is a technique for solving incompressible flow equations using a compressible-like formulation. By adding an artificial time derivative to the continuity equation (the "pseudo-compressibility" term), the system becomes hyperbolic and can be marched in time using explicit methods — without the global pressure coupling that makes traditional incompressible solvers slow on GPUs.

**When to use ACM:**
- Steady incompressible flows where you want explicit time-marching efficiency
- As an alternative to the pressure-based solver for truly incompressible problems
- When GPU throughput is more important than time-accuracy of the pressure field

```{admonition} ACM vs Low-Mach Preconditioning
:class: note
Both ACM and low-Mach preconditioning address the challenge of solving low-speed flows on GPU hardware. Low-Mach preconditioning (available in the density-based solver) modifies the compressible equations to remain well-conditioned at low Mach numbers. ACM instead adds a fictitious compressibility to the incompressible equations. In practice, the density-based solver with low-Mach preconditioning is recommended for most users — ACM is available for advanced use cases.
```

---

## Solver Summary

```{admonition} Compressible vs Incompressible
:class: note
The **density-based solver** is the only solver that directly solves the compressible Navier-Stokes equations, but it also handles low-speed (incompressible) flows accurately through low-Mach preconditioning. This makes it the recommended default for **both** compressible and incompressible applications. The other solvers listed below are dedicated incompressible formulations, available as alternatives when an incompressible-only approach is preferred or required.
```

| Solver | Flow Regime | Time Integration | Coupling | GPU Performance | Recommended Use |
|--------|-------------|------------------|----------|-----------------|-----------------|
| **Density-based** | Compressible & incompressible (all Mach, with low-Mach preconditioning) | Explicit (SSP-RK3) or Implicit | Coupled | Excellent | Default for all standard CFD — subsonic through supersonic |
| **Pressure-based (SIMPLE)** | Incompressible only | Implicit | Segregated | Moderate | Steady incompressible RANS |
| **Pressure-based (SIMPLEC)** | Incompressible only | Implicit | Segregated | Moderate | Faster steady convergence |
| **Pressure-based (PISO)** | Incompressible only | Implicit | Segregated | Moderate | Transient incompressible |
| **Pressure-based (PIMPLE)** | Incompressible only | Implicit | Segregated | Moderate | Robust transient flows |
| **Coupled** | Incompressible only | Implicit | Coupled | Moderate–Good | Strongly coupled physics |
| **FSAC** | Incompressible only | Hybrid (Explicit/Implicit) | Hybrid | Good | GPU-efficient incompressible |
| **ACM** | Incompressible only | Explicit | Coupled | Good | Explicit incompressible marching |

---

## Linear Solvers and Preconditioners

For implicit systems (pressure equation in segregated solvers, block system in coupled solver), iterative linear solvers are used with preconditioning to accelerate convergence.

### Iterative Solvers

| Solver | Description | Best For |
|--------|-------------|----------|
| **PCG** | Preconditioned Conjugate Gradient | Symmetric positive-definite systems (pressure) |
| **BiCGStab** | BiConjugate Gradient Stabilized | Non-symmetric systems (momentum, turbulence) |
| **GMRES** | Generalized Minimal Residual | General purpose; robust for difficult systems |

### Preconditioners

| Preconditioner | Description | Performance |
|---------------|-------------|-------------|
| **AMG** | Algebraic Multigrid — builds a coarser hierarchy to accelerate convergence | Best for large meshes (default) |
| **Chebyshev** | Polynomial preconditioner — anisotropic-mesh friendly | Good balance of quality and GPU efficiency |
| **SGS** | Symmetric Gauss-Seidel — red-black coloring for GPU parallelism | Strong smoothing; moderate GPU cost |
| **Block-Jacobi** | Damped block-diagonal scaling | Stronger than Jacobi; good GPU parallelism |
| **Jacobi** | Simple diagonal scaling | Cheapest per iteration; good on GPU |

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
| Immediate divergence (density-based) | CFL too high | Reduce target CFL; extend CFL ramp |
| Immediate divergence (pressure-based) | Relaxation too aggressive | Reduce relaxation factors by 30% |
| Oscillating residuals | Mesh quality or boundary condition issue | Check mesh quality; verify BCs |
| Slow convergence | CFL too conservative / relaxation too low | Gradually increase CFL or relaxation |
| Turbulence residuals stuck | Poor initialization | Enable turbulence ramping |
| Force coefficients not plateauing | Flow not yet periodic | Extend iteration count; check domain size |
| Pressure-based not converging | Segregated coupling struggling | Try coupled solver or switch to density-based |
| Checkerboard pressure pattern | Inadequate pressure-velocity coupling | Use Rhie-Chow stabilization; try PIMPLE |
