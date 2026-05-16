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

## Accuracy and Robustness

### Spatial Accuracy

Higher spatial accuracy can improve forces, pressure gradients, heat-transfer rates, and wake details. It may also require better mesh quality and more iterations.

| Setting | Best For |
|---------|----------|
| **Robust** | First runs, difficult geometry, or early setup checks. |
| **Standard** | Most production engineering runs. |
| **High Accuracy** | Final studies, validation work, and smooth meshes with adequate resolution. |

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
