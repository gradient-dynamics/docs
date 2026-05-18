# Simulation

Simulation pages describe how to configure and run Gradient Dynamics multiphysics solver workflows in Studio. The focus is on engineering setup, validation habits, and result interpretation, with enough solver-technology background to help you choose the right workflow.

## Supported Workflows

| Workflow | Typical Use |
|----------|-------------|
| **External aerodynamics** | Vehicles, aircraft, buildings, sports equipment, and exposed components. |
| **Internal flow** | Pipes, ducts, manifolds, enclosures, HVAC systems, and flow distribution. |
| **Thermal analysis** | Heat transfer in fluids and solids, cold plates, heat exchangers, and thermal-management systems. |
| **Rotating machinery** | Fans, pumps, compressors, turbines, propellers, and rotating zones. |
| **Coupled multiphysics** | Cases where flow, heat transfer, and multiple regions interact. |

## Solver Technology Highlights

Gradient Dynamics supports solver workflows on both structured and unstructured meshes. Unstructured meshing is the recommended starting point for most production CFD workflows, while structured meshing is available for repeatable automated studies and cases where that layout fits the validation target.

The solver stack includes pressure-based low-speed CFD, explicit compressible flow, transient simulation, turbulence modelling, rotating-zone workflows, heat transfer, and coupled multiphysics. The explicit compressible path uses flux reconstruction to build conservative face fluxes for density, momentum, and energy, which is useful for shocks, pressure waves, high-speed aerodynamics, nozzles, and flows with strong density variation.

See [Solver Technology](solver-technology.md) for an overview of flux reconstruction, numerical fluxes, gradient schemes, pressure-based coupling, and what these choices mean for engineering use.

## Simulation Workflow

1. Start from a generated or imported mesh.
2. Choose the physics and materials for each region.
3. Assign boundary conditions to named surfaces.
4. Select turbulence and solver settings appropriate for the application.
5. Run the simulation and monitor convergence.
6. Post-process fields, forces, heat-transfer metrics, and derived quantities.

## Topics

- [Simulation Setup](setup.md)
- [Solver Technology](solver-technology.md)
- [Turbulence Models](turbulence-models.md)
- [Boundary Conditions](boundary-conditions.md)
- [Solver Settings](solver-settings.md)
- [Running Simulations](running.md)
- [Post-Processing](post-processing.md)
