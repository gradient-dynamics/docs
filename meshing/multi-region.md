# Multi-Region Meshing

Multi-region meshing creates separate mesh zones for different physical domains within the same simulation. Each region is independently meshed and coupled at shared interfaces.

## When to Use Multi-Region

| Scenario | Regions | Example |
|----------|---------|---------|
| **Conjugate heat transfer** | Fluid + Solid | Air flowing over an aluminum heat sink |
| **Rotating machinery** | Rotating + Stationary | Fan impeller inside a duct |
| **Multi-material thermal** | Solid + Solid | PCB with copper traces in FR4 substrate |
| **Porous media** | Fluid + Porous | Flow through a filter or catalyst |

## How It Works

When you set up a multi-region mesh, the mesher:

1. **Meshes each region independently** using its own cell size and near-wall AMR settings
2. **Tags every cell** with its region — so the solver knows which cells belong to which region
3. **Detects or constructs interfaces** between touching regions
4. **Assigns appropriate physics** to each region for simulation

## Creating Regions

### From the Regions Tab

1. Navigate to the **Regions** tab
2. Click **Add Region**
3. Configure each region:

| Field | Description | Example |
|-------|-------------|---------|
| **Name** | Unique label for this region | `fluid`, `heatsink`, `rotor` |
| **Type** | Physics type for this zone | Fluid, Solid, Porous, Rotating |
| **CAD geometry** | The solid body or volume that defines this region | Select from uploaded bodies |
| **Cell size** | Target mesh cell size for this region | 2 mm |
| **Boundary layers** | Enable/configure BL for this region | Enabled for fluid, disabled for solid |

### Region Types

| Type | Description | Typical Use |
|------|-------------|-------------|
| **Fluid** | Standard incompressible flow | Air, water, coolant |
| **Solid** | Solid material, thermal conduction only | Aluminum heat sink, PCB, housing |
| **Porous** | Fluid with added flow resistance | Filter, packed bed, heat exchanger |
| **Rotating** | Fluid in a rotating reference frame (MRF) | Fan impeller, pump rotor, turbine |

### From Multi-Body CAD

When you upload a multi-body STEP file, each solid body is automatically detected. You can then assign each body to a named region with its type and mesh settings. The bodies are listed in the feature tree — click each one to configure it.

## Region Overview

After meshing, the **Regions** panel shows a summary of each region:

| Region Name | Type | Cells |
|-------------|------|-------|
| `pipe_wall` | Solid | 8,965 |
| `internal_flow` | Fluid | 3,624 |

## Interfaces

Where two regions share a boundary, an **interface** couples them. Interfaces are defined by referencing the **names** of the two regions they connect.

### Auto-Detection

Enable **Auto-detect interfaces** to have Studio automatically identify touching faces between regions. This works well for clean, imported multi-body CAD where bodies share exact face geometry.

### Manual Interface Setup

1. Navigate to the **Interfaces** tab
2. Click **Add Interface**
3. Select the two region names (e.g., `pipe_wall` ↔ `internal_flow`)
4. Choose the interface type

### Interface Types

| Type | Description | Use Case |
|------|-------------|----------|
| **CHT** | Conjugate heat transfer coupling | Fluid-solid thermal problems |
| **CHT with contact resistance** | Adds thermal resistance at the boundary | Imperfect contact, thermal paste |
| **CHT thin wall** | Models a thin solid layer at the interface | Sheet metal, PCB copper layer |
| **Frozen rotor** | Steady-state rotating-stationary coupling | Fans, pumps (steady RANS) |
| **Mixing plane** | Circumferentially averaged interface | Turbomachinery stage coupling |
| **Sliding mesh** | Transient rotating interface | Time-accurate turbomachinery |
| **Periodic** | Repeating pattern coupling | Sector models, cyclic symmetry |

### Conformal vs. Non-Conformal

- **Conformal** — Faces on both sides of the interface match exactly (1:1 node correspondence). Best accuracy, requires geometry to be matched in CAD.
- **Non-conformal** — Faces don't match exactly. More flexible but requires interpolation at the interface. Used when mesh sizes differ significantly between regions.

## Per-Region Mesh Settings

Each region has independent mesh control:

| Setting | Fluid Region | Solid Region |
|---------|-------------|--------------|
| **Cell size** | Smaller (resolve flow) | Larger (save cells) |
| **Near-wall AMR** | Enabled | Disabled |
| **Min cell size** | Flow-dependent | Less critical |

```{tip}
For CHT problems, the solid region typically needs a coarser mesh than the fluid region. Set the solid cell size 2–4× larger than the fluid cell size to save cells without sacrificing thermal accuracy.
```

## Multi-Region Example: Pipe CHT

A conjugate heat transfer pipe — fluid flowing inside a solid pipe wall:

**Regions:**

| Name | Type | Cell Size | Near-Wall AMR |
|------|------|-----------|---------------|
| `pipe_wall` | Solid | 1.5 mm | Disabled |
| `internal_flow` | Fluid | 2.0 mm | Enabled (medium) |

**Interface:**

| Name | Region A | Region B | Type |
|------|----------|----------|------|
| `cht_interface` | `pipe_wall` | `internal_flow` | CHT |

**Resulting regions in the mesh:**
- `pipe_wall` → Solid zone
- `internal_flow` → Fluid zone
