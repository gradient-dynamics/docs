# Simulation Setup

This guide walks you through configuring a CFD simulation in Gradient Dynamics Studio. Simulation setup is done in the **Simulation** tab of a CFD project.

## Prerequisites

Before setting up a simulation, you need a mesh. You can:

1. **Generate a mesh** in a Meshing project and import it
2. **Upload a mesh** directly to the CFD project (VTU, CGNS, or OpenFOAM format)
3. **Use an existing mesh** from a previous project

## Setup Overview

A simulation configuration consists of four parts:

1. **Turbulence model** — The physics model for turbulent flow
2. **Boundary conditions** — What happens at each surface (inlets, outlets, walls)
3. **Solver settings** — Numerical algorithm and convergence parameters
4. **Run parameters** — Maximum iterations, convergence criteria

## Step-by-Step Configuration

### 1. Select Turbulence Model

Choose the turbulence model from the dropdown in the Simulation tab. The default is **k-ω SST**, which works well for most external and internal flow applications.

Available models depend on your subscription tier — see [Turbulence Models](turbulence-models.md) for details on each model.

### 2. Set Boundary Conditions

Studio auto-detects boundary types from your surface names:

- Surfaces named `inlet` → Velocity inlet
- Surfaces named `outlet` → Pressure outlet
- All other surfaces → Wall (no-slip)

You can override any auto-detected condition. See [Boundary Conditions](boundary-conditions.md) for all available types and parameters.

### 3. Configure Solver Settings

For most cases, the defaults work well:

- **Algorithm:** SIMPLE
- **Relaxation factors:** Pre-configured for the selected turbulence model
- **Preconditioner:** AMG (Algebraic Multigrid)

See [Solver Settings](solver-settings.md) for advanced tuning.

### 4. Set Run Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| **Max iterations** | Maximum outer solver iterations | 500 – 2000 |
| **Convergence criterion** | Residual threshold for completion | 1e-4 (continuity) |

```{tip}
Start with 500 iterations. If residuals haven't converged, you can always extend the run. Most RANS simulations converge within 300–1000 iterations.
```

## Credit Cost Estimation

Before running, Studio shows the estimated credit cost based on:

- Mesh size (number of cells)
- Expected runtime
- GPU resources required

The estimate is shown when you click **Run Simulation**, before confirming.

## Quick Setup with the AI Assistant

For the fastest setup, use the AI Assistant:

> "Set up a simulation at 30 m/s with k-omega SST"

The assistant will:
1. Select the turbulence model
2. Set inlet velocity to 30 m/s
3. Configure outlet as pressure outlet (0 Pa)
4. Apply default solver settings
5. Ask for your confirmation before running
