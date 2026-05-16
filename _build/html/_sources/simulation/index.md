# Simulation

Simulation pages describe how to configure and run Gradient Dynamics multiphysics solver workflows in Studio. The focus is on engineering setup, validation habits, and result interpretation rather than internal implementation.

## Supported Workflows

| Workflow | Typical Use |
|----------|-------------|
| **External aerodynamics** | Vehicles, aircraft, buildings, sports equipment, and exposed components. |
| **Internal flow** | Pipes, ducts, manifolds, enclosures, HVAC systems, and flow distribution. |
| **Thermal analysis** | Heat transfer in fluids and solids, electronics cooling, cold plates, and heat exchangers. |
| **Rotating machinery** | Fans, pumps, compressors, turbines, propellers, and rotating zones. |
| **Coupled multiphysics** | Cases where flow, heat transfer, and multiple regions interact. |

## Simulation Workflow

1. Start from a generated or imported mesh.
2. Choose the physics and materials for each region.
3. Assign boundary conditions to named surfaces.
4. Select turbulence and solver settings appropriate for the application.
5. Run the simulation and monitor convergence.
6. Post-process fields, forces, heat-transfer metrics, and derived quantities.

## Topics

- [Simulation Setup](setup.md)
- [Turbulence Models](turbulence-models.md)
- [Boundary Conditions](boundary-conditions.md)
- [Solver Settings](solver-settings.md)
- [Running Simulations](running.md)
- [Post-Processing](post-processing.md)
