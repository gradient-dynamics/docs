# Simulation Setup

This guide walks you through configuring a CFD simulation in Gradient Dynamics Studio. Simulation setup is done in the **Simulation** tab of a CFD project.

## Prerequisites

Before setting up a simulation, you need a mesh. You can:

1. **Generate a mesh** in a Meshing project and import it
2. **Use the mesh generated** within the same project
3. **Use an existing mesh** from a previous project

## Setup Overview

A simulation configuration consists of five parts:

1. **Solver type** — Density-based (recommended) or pressure-based
2. **Turbulence model** — The physics model for turbulent flow
3. **Boundary conditions** — What happens at each surface (inlets, outlets, walls)
4. **Solver settings** — Numerical algorithm and convergence parameters
5. **Run parameters** — Maximum iterations, convergence criteria

## Step-by-Step Configuration

### 1. Select Solver Type

Choose between **Density-Based** (recommended) and **Pressure-Based** solvers from the dropdown at the top of the Simulation tab.

**Density-based** is the default and recommended choice for the vast majority of applications. It is optimized for the GPU-native Cartesian AMR mesh and delivers the best performance. See [Solver Settings](solver-settings.md) for a detailed comparison.

Use **Pressure-based** only if your application specifically requires an incompressible formulation.

### 2. Select Turbulence Model

Choose the turbulence model from the dropdown. The default is **k-ω SST**, which works well for most external and internal flow applications.

Available models depend on your subscription tier — see [Turbulence Models](turbulence-models.md) for details on each model.

### 3. Set Boundary Conditions

Studio auto-detects boundary types from your surface names:

- Surfaces named `inlet` → Velocity inlet
- Surfaces named `outlet` → Pressure outlet
- All other surfaces → Wall (no-slip)

You can override any auto-detected condition. See [Boundary Conditions](boundary-conditions.md) for all available types and parameters.

### 4. Configure Solver Settings

For most cases, the defaults work well:

- **Density-based:** Explicit Runge-Kutta, CFL 1.5, AUSM+ flux scheme, 2nd order spatial
- **Pressure-based:** SIMPLE, pre-configured relaxation factors, AMG preconditioner

See [Solver Settings](solver-settings.md) for advanced tuning options.

### 5. Set Run Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| **Max iterations** | Maximum solver iterations | 500 – 2000 |
| **Convergence criterion** | Residual threshold for completion | 1e-5 (density) / 1e-4 (pressure) |

```{tip}
Start with 500 iterations. If residuals haven't converged, you can extend the run. Most RANS simulations converge within 300–1000 iterations.
```

## Credit Cost Estimation

Before running, Studio shows the estimated credit cost based on:

- Mesh size (number of cells)
- Expected runtime
- GPU resources required

The estimate is shown when you click **Run Simulation**, before confirming.

## Quick Setup with the AI Assistant

For the fastest setup, use the AI Assistant:

> "Set up a density-based simulation at 30 m/s with k-omega SST"

The assistant will:
1. Select the density-based solver
2. Select k-ω SST turbulence model
3. Set inlet velocity to 30 m/s
4. Configure outlet as pressure outlet (0 Pa)
5. Apply default solver settings
6. Ask for your confirmation before running
