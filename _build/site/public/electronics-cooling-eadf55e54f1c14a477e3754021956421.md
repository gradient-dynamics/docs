# Example: Electronics Cooling

This example demonstrates setting up a thermal management simulation for an electronics enclosure. You'll model airflow over heat-generating components and evaluate cooling effectiveness.

## Objective

- Generate a mesh for an electronics enclosure with heat-generating components
- Run a simulation to evaluate airflow and temperature distribution
- Identify hot spots and areas of poor cooling
- Compare different cooling configurations

## Step 1: Create a Meshing Project

1. **Dashboard** → **New Project** → **Meshing**
2. Name: "Electronics Cooling"
3. Upload your enclosure geometry (STEP format)

## Step 2: Geometry Preparation

Electronics cooling geometries typically include:

- **Enclosure** — The outer housing that contains the electronics
- **Components** — PCBs, processors, heat sinks, fans
- **Vents** — Intake and exhaust openings

```{admonition} Geometry Simplification
:class: tip
For CFD, simplify your geometry:
- Remove small features (screws, labels, textures) that don't affect flow
- Close small gaps that the mesh can't resolve
- Combine parts that aren't thermally distinct into single bodies
- Keep heat sinks and other flow-critical features

The AI Assistant can suggest which features to keep and which to remove.
```

## Step 3: Domain Configuration

1. Select **Internal Flow** (if air flows through the enclosure via vents)
2. The fluid volume is the air inside the enclosure
3. Identify inlet vents and outlet vents as surfaces

For **conjugate heat transfer** (modeling solid heat conduction through heat sinks):
1. Select **Conjugate Heat Transfer (CHT)** domain type
2. Define fluid region (air inside the enclosure)
3. Define solid regions (heat sink, PCB, processor package)

## Step 4: Multi-Region Setup (CHT)

### Regions

| Region | Type | Material |
|--------|------|----------|
| `air` | Fluid | Air (ρ = 1.225 kg/m³, μ = 1.81e-5 Pa·s) |
| `heatsink` | Solid | Aluminum (k = 205 W/m·K) |
| `pcb` | Solid | FR4 (k = 0.3 W/m·K) |

### Interfaces

| Interface | Regions | Type |
|-----------|---------|------|
| `air_heatsink` | air ↔ heatsink | Perfect contact |
| `heatsink_pcb` | heatsink ↔ pcb | Contact resistance (if thermal paste modeled) |

## Step 5: Surface Naming

| Surface | Name | Condition |
|---------|------|-----------|
| Intake vent | `inlet` | Velocity inlet |
| Exhaust vent | `outlet` | Pressure outlet |
| Enclosure walls | `enclosure_wall` | No-slip wall (adiabatic) |
| Processor top | `processor` | Heat flux wall (e.g., 65 W) |
| Heat sink fins | `heatsink_surface` | No-slip wall (coupled for CHT) |

## Step 6: Mesh Settings

| Parameter | Value |
|-----------|-------|
| Target cell size | 5 mm |
| Min cell size | 0.5 mm |
| Refinement levels | 8 |
| Boundary layers | Enabled (fluid region only) |
| BL layers | 5 |
| First layer height | 0.1 mm |
| Growth rate | 1.2 |

### Refinement Zones

| Zone | Location | Cell Size | Purpose |
|------|----------|-----------|---------|
| Heat sink region | Around heat sink fins | 1 mm | Resolve fin gaps |
| Vent regions | At intake/exhaust openings | 2 mm | Resolve jet flows |
| Component zone | Around hot components | 2 mm | Thermal resolution |

## Step 7: Simulation Setup

| Setting | Value |
|---------|-------|
| Turbulence model | k-ω SST |
| Inlet velocity | Based on fan curve (e.g., 2 m/s) |
| Outlet pressure | 0 Pa |
| Enclosure walls | Adiabatic wall (no heat loss) |
| Processor surface | Heat flux: 65 W / surface area |
| Turbulence intensity | 5% |
| Max iterations | 1000 |

## Step 8: Results Analysis

### Temperature Distribution

1. Color surfaces by **Temperature**
2. Identify the maximum temperature on the processor
3. Check that the maximum temperature is below the thermal design limit (typically 85–100°C)

### Airflow Patterns

1. Add **streamlines** seeded from the intake vent
2. Trace the airflow path through the enclosure
3. Identify:
   - Areas with good airflow (near vents, through heat sink)
   - Dead zones with stagnant air (poor cooling)
   - Short-circuiting paths (air going directly from inlet to outlet without cooling components)

### Heat Sink Performance

1. Add **slice planes** through the heat sink fins, colored by velocity
2. Check that air flows through all fin channels
3. Low-velocity or recirculating regions indicate poor heat sink utilization

### Hot Spot Identification

1. Color all solid surfaces by temperature
2. Hottest regions indicate inadequate cooling
3. Common hot spots:
   - Components far from airflow path
   - Areas behind flow obstructions
   - Stagnation zones between closely packed components

## Design Optimization Workflow

1. **Baseline** — Run the initial configuration and record temperatures
2. **Modify** — Adjust vent positions, fan speed, or heat sink design
3. **Re-mesh** — Generate a new mesh for the modified geometry
4. **Re-simulate** — Run the simulation with the same conditions
5. **Compare** — Check if maximum temperature decreased

### Common Improvements

| Change | Effect |
|--------|--------|
| Increase fan speed | Lower temperatures, more noise |
| Add/reposition vents | Better airflow to hot spots |
| Larger heat sink | More surface area for cooling |
| Thermal pads/paste | Better component-to-heatsink contact |
| Baffles/guides | Direct airflow to problem areas |
