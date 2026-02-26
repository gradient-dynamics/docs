# Multi-Region Meshing

Multi-region meshing creates separate mesh zones for different physical domains within the same simulation. Each region is independently meshed and assigned a unique ID, then coupled at shared interfaces.

## When to Use Multi-Region

| Scenario | Regions | Example |
|----------|---------|---------|
| **Conjugate heat transfer** | Fluid + Solid | Air flowing over an aluminum heat sink |
| **Rotating machinery** | Rotating + Stationary | Fan impeller inside a duct |
| **Multi-material thermal** | Solid + Solid | PCB with copper traces in FR4 substrate |
| **Porous media** | Fluid + Porous | Flow through a filter or catalyst |

## How It Works

When you set up a multi-region mesh, the mesher:

1. **Meshes each region independently** using its own cell size and boundary layer settings
2. **Assigns a unique region ID** to every region (integers starting from 0, in the order regions are defined)
3. **Tags every cell** with its region ID — so the complete mesh knows which cells belong to which region
4. **Detects or constructs interfaces** between touching regions
5. **Exports with zone information** so your solver can apply different physics per region

```{admonition} Region IDs
:class: note
Region IDs are assigned automatically in the order regions are defined — the first region gets ID 0, the second gets ID 1, and so on. You reference regions by **name** (not ID) when setting up interfaces and boundary conditions. The IDs appear in the exported mesh and are used by solvers to assign physics per zone.
```

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

## Region IDs in the Exported Mesh

Every cell in the exported mesh carries a region tag. In the output:

- **OpenFOAM** — Each region exports as a separate `polyMesh` with a `cellZones` file
- **ANSYS Fluent** — Zone types are set per region (Fluid = 1, Solid = 17)
- **CGNS** — Separate zones per region with proper zone type labels
- **VTU** — A `cell_region_ids` array tags every cell with its integer region ID

Example region metadata in a 2-region CHT mesh:

| Region Name | Region ID | Type | Cells |
|-------------|-----------|------|-------|
| `pipe_wall` | 0 | Solid | 8,965 |
| `internal_flow` | 1 | Fluid | 3,624 |

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
| **Boundary layers** | Enabled | Disabled |
| **Min cell size** | Flow-dependent | Less critical |

```{tip}
For CHT problems, the solid region typically needs a coarser mesh than the fluid region. Set the solid cell size 2–4× larger than the fluid cell size to save cells without sacrificing thermal accuracy.
```

## Multi-Region Example: Pipe CHT

A conjugate heat transfer pipe — fluid flowing inside a solid pipe wall:

**Regions:**

| Name | Type | Cell Size | Boundary Layers |
|------|------|-----------|-----------------|
| `pipe_wall` | Solid | 1.5 mm | Disabled |
| `internal_flow` | Fluid | 2.0 mm | Enabled, 5 layers, first height 0.1 mm |

**Interface:**

| Name | Region A | Region B | Type |
|------|----------|----------|------|
| `cht_interface` | `pipe_wall` | `internal_flow` | CHT |

**Resulting region IDs in exported mesh:**
- `pipe_wall` → Region ID 0
- `internal_flow` → Region ID 1

## Multi-Region Export

When exporting a multi-region mesh:

- Each region is exported as a separate **cell zone** with proper labeling and its region ID
- Interface patches on both sides carry matching names (e.g., `pipe_wall_to_internal_flow`)
- Format-specific zone types are applied automatically
- OpenFOAM exports include `regionProperties` and per-region `constant/` directories

See {doc}`export` for format-specific details.
