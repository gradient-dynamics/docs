# Multi-Region Meshing

Multi-region meshing creates separate mesh zones for different physical domains within the same simulation. This is required for conjugate heat transfer (CHT), rotating machinery, and any problem involving different materials or physics in adjacent regions.

## When to Use Multi-Region

| Scenario | Regions | Example |
|----------|---------|---------|
| **Conjugate heat transfer** | Fluid + Solid | Air flowing over an aluminum heat sink |
| **Rotating machinery** | Rotating + Stationary | Fan impeller inside a duct |
| **Multi-material thermal** | Solid + Solid | PCB with copper traces in FR4 substrate |
| **Porous media** | Fluid + Porous | Flow through a filter or catalyst |

## Creating Regions

### From the Regions Tab

1. Navigate to the **Regions** tab
2. Click **Add Region**
3. Configure:
   - **Name** — Descriptive label (e.g., `fluid`, `heatsink`, `impeller`)
   - **Type** — Fluid, Solid, Porous, or Rotating
   - **Material** — Select from the material library or enter custom properties
   - **Mesh size** — Per-region cell size override

### From Multi-Body CAD

When you upload a multi-body STEP file, each solid body is automatically detected. You can assign each body to a region:

1. Studio detects the bodies and lists them
2. Assign each body as **Fluid** or **Solid**
3. Interfaces between touching bodies are automatically identified

## Region Types

### Fluid Region

Standard fluid flow region. Configure:
- Density and viscosity (or select a material like Air, Water)
- Reference pressure and temperature

### Solid Region

Solid material for thermal conduction. No fluid equations are solved. Configure:
- Thermal conductivity
- Density and specific heat capacity

### Rotating Region (MRF)

A fluid region with a rotating reference frame. Configure:
- **Rotation axis** — Direction vector (e.g., [0, 0, 1] for Z-axis)
- **Rotation origin** — Center point of rotation
- **Angular velocity** — In RPM or rad/s

### Porous Region

A fluid region with additional resistance modeling. Configure:
- Darcy coefficient (viscous resistance)
- Forchheimer coefficient (inertial resistance)
- Porosity

## Interfaces

Where two regions touch, an **interface** must be defined. Interfaces control how information is transferred between regions.

### Interface Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Perfect contact** | Direct thermal coupling, no resistance | Metal-to-metal contact |
| **Contact resistance** | Thermal resistance between regions | Imperfect contact, thermal paste |
| **Thin wall** | Modeled as a thin solid layer | Sheet metal, PCB layers |
| **Frozen rotor** | Steady-state rotating-stationary coupling | Fans, compressors (steady RANS) |
| **Mixing plane** | Circumferentially averaged interface | Turbomachinery stage coupling |

### Configuring Interfaces

1. Navigate to the **Interfaces** tab
2. Select the two regions that share a boundary
3. Choose the interface type
4. Configure type-specific parameters (e.g., contact resistance value, wall thickness)

## Per-Region Mesh Settings

Each region can have independent mesh settings:

- **Cell size** — Different resolution for fluid vs. solid zones
- **Boundary layers** — Enable/disable per region (typically enabled for fluid, disabled for solid)
- **Refinement** — Region-specific refinement levels

```{tip}
For CHT problems, the solid region often needs a coarser mesh than the fluid region. Set the solid cell size 2–4× larger than the fluid cell size to save cells without sacrificing accuracy.
```

## Multi-Region Export

When exporting a multi-region mesh:

- Each region is exported as a separate **cell zone** with proper labeling
- Interfaces are marked with matching patch names on both sides
- Format-specific zone types are applied (e.g., Fluent zone type 1 for fluid, 17 for solid)
- OpenFOAM exports include a `cellZones` file and proper `regionProperties`
