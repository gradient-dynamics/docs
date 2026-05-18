# Solver Settings

Solver settings control how Studio advances a simulation, monitors convergence, and balances accuracy, robustness, and runtime. The defaults are chosen for general engineering workflows; adjust them when you have a validation requirement, a difficult case, or a known setup preference.

## Solver Selection

Choose the solver family based on the physics and engineering objective.

| Solver Family | Use For |
|---------------|---------|
| **Automatic** | Recommended starting point. Studio selects stable defaults from the project physics, mesh, and boundary conditions. |
| **Compressible Flow** | High-speed flows, pressure waves, density changes, or mixed-speed applications. |
| **Incompressible Flow** | Low-speed liquid or gas flows where density variation is not important. |
| **Coupled Multiphysics** | Cases where flow, heat transfer, and multiple regions interact strongly. |
| **Transient Flow** | Time-varying wakes, rotating machinery, startup/shutdown, or unsteady thermal response. |

If you are unsure, start with **Automatic** and refine only after reviewing convergence and result sensitivity.

For a method-level explanation of the solver families, including flux reconstruction, pressure-based coupling, and gradient schemes, see [Solver Technology](solver-technology.md).

## Accuracy and Robustness

### Spatial Accuracy

Higher spatial accuracy can improve forces, pressure gradients, heat-transfer rates, and wake details. It may also require better mesh quality and more iterations.

| Setting | Best For |
|---------|----------|
| **Robust** | First runs, difficult geometry, or early setup checks. |
| **Standard** | Most production engineering runs. |
| **High Accuracy** | Final studies, validation work, and smooth meshes with adequate resolution. |

Higher-order settings work by reconstructing face values from surrounding cells. This improves smooth gradients, wakes, shear layers, and pressure fields when the mesh supports it. Near shocks, separation, sharp thermal fronts, or poor-quality cells, bounded or limited reconstruction may deliberately add diffusion to prevent non-physical oscillations.

### Time Behaviour

| Mode | Best For |
|------|----------|
| **Steady** | Design-point studies where the final mean state is the main result. |
| **Transient** | Time-dependent loads, vortex shedding, rotating machinery, startup, or thermal response. |

For transient runs, choose a time step small enough to resolve the physical event you care about. Studio reports time-step and stability guidance during setup.

### Convergence Controls

| Control | Purpose |
|---------|---------|
| **Maximum iterations** | Stops a run after a set amount of solver work. |
| **Residual target** | Defines the convergence threshold. |
| **Monitor quantities** | Tracks forces, pressure drop, heat flux, temperature, or other engineering outputs. |
| **Early stopping** | Stops when residuals and monitor quantities have stabilized. |

Residuals alone are not always enough. For final studies, also check that the engineering quantities of interest have stabilized.

## Linear Solver Controls

Implicit and pressure-based workflows solve sparse linear systems inside each nonlinear CFD iteration. Studio defaults are chosen for stable general use, but advanced runs may expose solver and preconditioner choices.

| Control | What it means |
|---------|---------------|
| **PCG** | Preconditioned conjugate-gradient solve. Best suited to symmetric positive-definite systems such as many pressure or diffusion solves. |
| **BiCGStab-type solver** | Krylov solve for nonsymmetric systems, often used for convection-diffusion, momentum, turbulence, and coupled transport equations. |
| **GAMG / AMG** | Algebraic multigrid. Builds coarse correction levels from the system itself to accelerate pressure and elliptic solves. |
| **Chebyshev smoother** | Polynomial smoothing method used to damp selected error modes, often inside a multigrid or preconditioning workflow. |
| **Preconditioner** | A cheaper approximate solve that makes the main iterative method converge in fewer iterations. |

Use Automatic settings unless the residual history clearly points to a linear-solver bottleneck. If pressure or continuity residuals stall on a large mesh, a multigrid-style pressure solve can help. If a transport equation is slow or noisy, a more suitable Krylov solver or smoother may improve robustness. These changes should be evaluated with residuals, monitor quantities, and mesh quality together.

## Turbulence and Wall Treatment

Choose turbulence settings based on the application, mesh resolution, and validation target. The default turbulence model is suitable for many external and internal engineering flows, but some cases require a specific model.

Near-wall treatment should match the mesh resolution near walls. Use the y+ calculator and the [Near-Wall Resolution](../meshing/boundary-layers.md) guide before running final drag, pressure-drop, or heat-transfer studies.

## Multiphysics Settings

For thermal and coupled cases, verify:

- Materials are assigned to every region.
- Fluid and solid regions have the intended interfaces.
- Heat sources and thermal boundary conditions use consistent units.
- Monitor points or integrated quantities capture the engineering output you need.

## Practical Defaults

For a first run:

1. Use **Automatic** solver selection.
2. Keep **Standard** spatial accuracy.
3. Set a conservative maximum iteration count.
4. Monitor at least one engineering quantity, such as drag, pressure drop, outlet temperature, or heat flux.
5. Review residuals, monitors, and mesh quality before increasing fidelity.

## When to Tune Settings

Tune solver settings when:

- Residuals stall early or diverge.
- Forces, pressure drop, or temperatures have not stabilized.
- A mesh sensitivity study shows inconsistent trends.
- The case has strong separation, high-speed effects, tight thermal coupling, or difficult rotating interfaces.
- You are matching a verification, validation, or benchmark target.

See [Running Simulations](running.md) and [Troubleshooting](../knowledge-base/troubleshooting.md) for symptoms and recommended next steps.
