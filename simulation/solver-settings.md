# Solver Settings

Solver settings control the numerical algorithms used to solve the flow equations. For most cases, the defaults work well. This page covers advanced tuning options for when you need to troubleshoot convergence or optimize performance.

## Pressure-Velocity Coupling

The coupling algorithm determines how the pressure and velocity equations are solved together.

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **SIMPLE** | Semi-Implicit Method for Pressure-Linked Equations | Steady-state RANS (default) |
| **SIMPLEC** | SIMPLE-Consistent — faster convergence for simple flows | Well-behaved flows |
| **PISO** | Pressure-Implicit with Splitting of Operators | Transient simulations |
| **PIMPLE** | Hybrid SIMPLE-PISO | Transient with large time steps |

For **steady-state RANS**, use **SIMPLE** (the default). It provides the best balance of robustness and convergence speed.

## Relaxation Factors

Under-relaxation factors control how aggressively the solution is updated each iteration. Lower values are more stable but converge slower; higher values converge faster but risk instability.

### Default Relaxation Factors by Model

| Field | k-ω SST | k-ε | Spalart-Allmaras | RSM |
|-------|---------|-----|-----------------|-----|
| **Velocity (U)** | 0.5 | 0.6 | 0.6 | 0.4 |
| **Pressure (p)** | 0.2 | 0.3 | 0.3 | 0.2 |
| **k** | 0.4 | 0.4 | — | 0.3 |
| **ω / ε** | 0.4 | 0.4 | — | 0.3 |
| **Turbulent viscosity** | 0.05 | 0.1 | 0.1 | 0.05 |

```{tip}
If the simulation diverges, try reducing relaxation factors by 20–30%. If convergence is too slow, try increasing them gradually.
```

## Linear Solver

The pressure equation is solved using an iterative linear solver with preconditioning.

### Preconditioners

| Preconditioner | Description | Performance |
|---------------|-------------|-------------|
| **AMG** | Algebraic Multigrid (default) | Best for large meshes |
| **Jacobi** | Diagonal scaling | Simple, fast per iteration |
| **Chebyshev** | Polynomial smoothing | Good with AMG |
| **ILU** | Incomplete LU factorization | Good for small meshes |

**AMG** is the default and recommended preconditioner. It scales well to large meshes and handles anisotropic cells (boundary layers) effectively.

### AMG Settings

| Parameter | Default | Description |
|-----------|---------|-------------|
| **Max coarse levels** | 10 | Maximum levels in the multigrid hierarchy |
| **Coarse size** | 100 | Stop coarsening when matrix is this small |
| **Smoother** | Chebyshev | Smoothing algorithm at each level |
| **Pre-smooth iterations** | 2 | Smoothing passes before restriction |
| **Post-smooth iterations** | 2 | Smoothing passes after prolongation |

## Discretization Schemes

### Convection Schemes

| Scheme | Order | Bounded | Best For |
|--------|-------|---------|----------|
| **Upwind** | 1st | Yes | Initial iterations, robustness |
| **Linear upwind** | 2nd | No | Production RANS (default) |
| **Van Leer** | 2nd | Yes | Scalar transport, turbulence |

The solver uses **linear upwind** (2nd order) for velocity by default, providing good accuracy. Turbulence quantities use bounded schemes for stability.

### Gradient Schemes

- **Weighted Least Squares** — Default for conformal (hex-dominant) meshes. Most accurate.
- **Green-Gauss** — Used for polyhedral meshes. Robust and efficient.

### Non-Orthogonal Correctors

For meshes with non-orthogonality above 70°, enable non-orthogonal correctors:

| Setting | When to Use |
|---------|-------------|
| 0 correctors | Good quality mesh (non-orthogonality < 60°) |
| 1 corrector | Moderate non-orthogonality (60–75°) |
| 2 correctors | Poor orthogonality (> 75°) |

## Convergence Criteria

### Residual Thresholds

| Residual | Default Threshold | Description |
|----------|------------------|-------------|
| **Continuity** | 1e-4 | Mass conservation |
| **Velocity** | 1e-5 | Momentum equations |
| **Turbulence** | 1e-5 | Turbulence transport |

The simulation stops when all residuals drop below their thresholds, or when the maximum iteration count is reached.

### Plateau Detection

Studio can automatically detect when residuals have plateaued (stopped decreasing) and terminate early, even if the absolute threshold hasn't been reached. This is useful for complex flows where residuals may stabilize at a level above the threshold.

## Startup Controls

### Turbulence Ramping

For difficult cases, the solver can gradually introduce turbulence:

1. **Start iteration** — Iteration at which turbulence equations are activated (flow starts as laminar)
2. **Ramp iterations** — Number of iterations to blend from laminar to fully turbulent

This helps establish a stable initial flow field before turbulence modeling kicks in.

```{admonition} When to Use Ramping
:class: note
Use turbulence ramping when:
- The initial iterations diverge immediately
- Pressure spikes occur at startup
- Complex geometries with sharp features cause early instability
```

## Troubleshooting Convergence

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| Immediate divergence | Relaxation too aggressive | Reduce all relaxation factors by 30% |
| Oscillating residuals | Mesh quality issues | Check mesh quality, add non-orthogonal correctors |
| Slow convergence | Relaxation too conservative | Gradually increase relaxation factors |
| Pressure oscillations | Rhie-Chow instability | Enable RC ramping |
| Turbulence residuals stuck | Poor initialization | Enable turbulence ramping |
