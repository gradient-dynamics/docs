# Simulation Setup with the Assistant

The AI Assistant can configure and launch CFD simulations through natural language conversation. This page shows common interaction patterns for simulation setup.

## Turbulence Model Selection

### Ask for a Recommendation

> **You:** "What turbulence model should I use for external vehicle aerodynamics?"
>
> **Assistant:** "For vehicle aerodynamics, I recommend **k-ω SST**. It provides the best balance of accuracy and robustness for external flows with boundary layer separation. It handles both attached and separated flow regions well, and works with the boundary layers we configured (y+ ≈ 30)."

### Specify Directly

> **You:** "Use Spalart-Allmaras for this simulation"
>
> **Assistant:** *Sets the turbulence model to SA and adjusts relaxation factors accordingly.*

## Boundary Conditions

### Automatic Setup

> **You:** "Set up boundary conditions for 30 m/s freestream"
>
> **Assistant:** *Detects boundary patches from surface names and configures:*
> - `inlet` → Velocity inlet, 30 m/s
> - `outlet` → Pressure outlet, 0 Pa
> - `car_body` → No-slip wall
> - `ground` → Moving wall, 30 m/s
> - `top`, `sides` → Slip wall
>
> *Presents for confirmation.*

### Modify Specific Conditions

> **You:** "Change the inlet velocity to 50 m/s and add 3% turbulence intensity"
>
> **Assistant:** *Updates the inlet boundary condition with the new velocity and turbulence intensity.*

### Complex Setups

> **You:** "The wheels should rotate. Front wheels at 800 RPM, rear at 850 RPM."
>
> **Assistant:** *Configures rotating wall conditions for the wheel surfaces with the specified angular velocities.*

## Solver Configuration

### Use Defaults

> **You:** "Use default solver settings for k-omega SST"
>
> **Assistant:** *Applies the default relaxation factors and solver parameters optimized for k-ω SST.*

### Troubleshoot Convergence

> **You:** "The simulation is oscillating. What should I change?"
>
> **Assistant:** "I can see the residuals are oscillating. I recommend reducing the relaxation factors:
> - Velocity: 0.5 → 0.3
> - Pressure: 0.2 → 0.15
> - Turbulence: 0.4 → 0.3
>
> This should stabilize the convergence at the cost of requiring more iterations."

### Adjust Parameters

> **You:** "Increase the max iterations to 2000 and tighten convergence to 1e-5"
>
> **Assistant:** *Updates the run parameters and presents for confirmation.*

## Running Simulations

### Launch

> **You:** "Run the simulation"
>
> **Assistant:** "Ready to run with the following configuration:
> - Turbulence model: k-ω SST
> - Inlet: 30 m/s, TI = 1%
> - Outlet: 0 Pa
> - Max iterations: 1000
> - Estimated cost: 2.5 credits
>
> **[Run]** **[Cancel]**"

### During the Run

> **You:** "How is the simulation doing?"
>
> **Assistant:** "The simulation is at iteration 450 of 1000. Residuals are:
> - Continuity: 3.2e-4 (decreasing)
> - Velocity: 8.1e-5 (converged)
> - Turbulence: 2.4e-4 (decreasing)
>
> Convergence looks healthy. The simulation should converge within the next 200 iterations."

## Results Analysis

### Quick Summary

> **You:** "What are the results?"
>
> **Assistant:** "Simulation completed in 680 iterations. Key results:
> - Drag coefficient (Cd): 0.31
> - Lift coefficient (Cl): 0.12
> - Maximum velocity: 48 m/s (on roof)
> - Minimum pressure: -850 Pa (roof leading edge)
>
> These values are typical for a sedan geometry. Would you like me to set up some visualization views?"

### Visualization Guidance

> **You:** "Show me the wake structure"
>
> **Assistant:** "I recommend:
> 1. A centerline slice plane (Y = 0) colored by velocity magnitude — this shows the wake length and recirculation zone behind the car
> 2. Streamlines seeded from the inlet — this shows how the flow separates at the rear
>
> Would you like me to set these up?"

### Force Analysis

> **You:** "Calculate the drag force on the car body"
>
> **Assistant:** *Computes forces on the `car_body` surface and reports:*
> - Drag force: 142 N
> - Lift force: 55 N
> - Cd: 0.31 (frontal area: 2.2 m²)
> - Cl: 0.12

## Example: Complete Simulation Workflow

> **You:** "Set up and run a simulation at 120 km/h"
>
> **Assistant:** "I'll configure a RANS simulation at 33.3 m/s (120 km/h):
> - Turbulence model: k-ω SST
> - Inlet: 33.3 m/s, TI = 1%
> - Outlet: 0 Pa
> - Car body: No-slip wall
> - Ground: Moving wall at 33.3 m/s
> - Top/sides: Slip wall
> - Max iterations: 1000
>
> **[Confirm]**"
>
> **You:** "Confirm and run"
>
> **Assistant:** "Configuration applied. Launching simulation — estimated cost: 3.2 credits.
>
> **[Run]**"
>
> *... simulation runs ...*
>
> **You:** "What's the drag coefficient?"
>
> **Assistant:** "Cd = 0.31 based on a frontal area of 2.2 m². The total drag force is 175 N. This is in the expected range for a sedan (0.25–0.35)."
