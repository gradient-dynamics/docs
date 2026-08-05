# Simulation setup reference

These pages provide detailed setup guidance for FluxCore workflows in Studio.
They focus on the engineering choices that define a reproducible simulation:
physics, materials, boundary conditions, turbulence, run controls and outputs.

## Supported workflows

| Workflow | Typical use |
|---|---|
| External aerodynamics | Vehicles, aircraft, buildings and exposed components |
| Internal flow | Pipes, ducts, manifolds, enclosures and flow distribution |
| Thermal and CHT | Cold plates, heat sinks, electronics and heat exchangers |
| Rotating machinery | Fans, pumps, compressors, turbines and propellers |
| Time-resolved flow | Unsteady loads, wakes and transient operating conditions |

FluxCore is a novel GPU-native simulation engine, developed as a coherent
computational product for accelerator hardware rather than adapted from a
traditional CPU solver. The public documentation describes supported physics,
controls, boundary conditions and outputs; implementation details remain
proprietary.

## Recommended workflow

1. Start from a checked generated or imported mesh.
2. Choose the physics and materials for every region.
3. Assign conditions to named boundaries.
4. Select turbulence and numerical controls appropriate to the application.
5. Define monitors and engineering outputs before launching.
6. Run, inspect convergence and confirm conservation and physical plausibility.
7. Compare important quantities with a reference or mesh-sensitivity study.

```{toctree}
:maxdepth: 1

Simulation setup <setup>
FluxCore technology <solver-technology>
Turbulence models <turbulence-models>
Boundary conditions <boundary-conditions>
Solver settings <solver-settings>
Running simulations <running>
Post-processing <post-processing>
```
