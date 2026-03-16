# Surfaces and Named Selections

Surfaces (also called **named selections** or **boundary patches**) are named regions of the mesh boundary. Properly named surfaces are essential for applying boundary conditions in simulation and for organizing mesh exports.

## What Are Named Selections?

When the mesher generates a mesh, every face on the domain boundary is assigned to a named selection. These names carry through to the simulation setup — boundary conditions (inlet velocity, outlet pressure, wall type) are applied to named selections by name. The solver never sees raw face indices; it sees patch names.

Named selections are created from three sources:

1. **Domain boundaries** — Studio automatically names the bounding box faces (inlet, outlet, sides, top, ground) based on domain type and flow direction
2. **CAD surface names** — Face or body names from STEP/IGES files are preserved and become named selections automatically
3. **User-defined selections** — Any additional groupings you create manually in the Surfaces tab

## Auto-Created Named Selections

When you generate a mesh, Studio creates these named selections automatically:

### External Flow

| Named Selection | Description |
|----------------|-------------|
| `inlet` | Upstream face of the domain box |
| `outlet` | Downstream face of the domain box |
| `top` | Top face of the domain box |
| `side_left`, `side_right` | Lateral faces |
| `ground` | Bottom face (when ground plane is enabled) |
| `symmetry` | Symmetry cut plane (when enabled) |
| *(geometry face names)* | Faces from your CAD file (e.g., `car_body`, `windshield`) |

### Internal Flow

| Named Selection | Description |
|----------------|-------------|
| `inlet` | Open inlet face(s) detected on the geometry |
| `outlet` | Open outlet face(s) detected on the geometry |
| *(geometry face names)* | Interior wall surfaces from the CAD file |

### Rotating Machinery

| Named Selection | Description |
|----------------|-------------|
| `inlet`, `outlet` | Domain inlet/outlet |
| `rotating_wall` | Rotating geometry surfaces |
| `stationary_wall` | Stationary housing surfaces |
| `mrf_interface` | Rotating/stationary zone interface |

## Managing Named Selections

### Viewing and Editing

1. Navigate to the **Surfaces** tab in your workspace
2. All named selections are listed with their face count and current type
3. Click a selection to highlight it in the 3D viewer
4. Rename any selection by clicking the name field

### Creating New Selections

To group multiple CAD faces into a single named selection:

1. Select multiple faces in the 3D viewer (Shift + click, or drag to box-select)
2. Click **Create Selection** in the Surfaces panel
3. Enter a name for the new selection
4. All selected faces are merged into this patch

This is useful when a CAD file has many individual face IDs for what should logically be one surface (e.g., a car body split into dozens of separate STEP faces).

### Splitting Selections

To separate faces from an existing selection:

1. Select the faces you want to split out in the 3D viewer
2. Click **Extract** in the Surfaces panel
3. Assign the extracted faces to a new or existing selection

### Recommended Naming Conventions

Use lowercase names that describe the physical role:

| Name | Description |
|------|-------------|
| `inlet` | Flow entry surface |
| `outlet` | Flow exit surface |
| `wall` | Generic solid wall |
| `car_body` | Vehicle body |
| `ground` | Ground plane |
| `symmetry` | Symmetry plane |
| `top`, `side_left`, `side_right` | Far-field boundaries |
| `wheel_front_left` | Specific component surfaces |

```{tip}
Studio's AI Assistant and boundary condition auto-detection use surface names to assign BCs automatically. Using standard names like `inlet`, `outlet`, and `wall` enables full automation of the simulation setup step.
```

## How Named Selections Are Processed

When you click **Generate Mesh**, the following happens on the backend:

1. The domain geometry and all named selection assignments are serialized and sent to the cloud GPU job
2. During meshing, the block AMR grid is classified — each block is tagged as fluid, solid, or cut-cell
3. All boundary faces of the fluid region are assigned to their named selections based on the geometry input
4. CAD face names from STEP files are matched to faces in the cut-cell mesh using spatial proximity and normal direction
5. Domain boundary faces (inlet, outlet, sides) are assigned automatically based on their position
6. The final named selection map is stored with the mesh and used directly in the simulation setup

After meshing, you can view the named selection assignments in the 3D viewer and make any corrections before running a simulation.

## Per-Selection Mesh Controls

For STEP/IGES files with preserved face topology, you can set mesh parameters on individual named selections:

### Surface Mesh Size Override

Override the global cell size for specific surfaces. Useful for:

- Finer resolution on aerodynamically important surfaces (leading edges, spoilers)
- Coarser resolution on less important surfaces (far-field, housing)

### Feature Angle

Controls how the mesher handles sharp edges. Faces meeting at angles greater than the feature angle threshold are treated as separate geometric features and receive refined AMR at the edge.

- **Low angle (15–30°)** — Captures more edges, finer mesh along features
- **High angle (45–60°)** — Only captures sharp edges, fewer refinement cells

## Named Selection Types

Each named selection has a boundary type that the solver uses to apply the correct physics:

| Selection Type | Description |
|---------------|-------------|
| **Wall** | No-slip solid boundary |
| **Inlet** | Flow entry |
| **Outlet** | Flow exit |
| **Symmetry** | Mirror plane |
| **Far-field** | Distant boundary |

Types are assigned automatically from surface names and domain type. You can override any assignment in the Surfaces tab.

## Auto-Detection

Studio can automatically identify and name common boundary types:

- **Domain boundaries** — Inlet, outlet, top, sides, ground are named based on position and domain configuration
- **Geometry surfaces** — CAD face names from STEP files are preserved automatically
- **Open faces** — For internal flow, open faces (inlets, outlets) are detected by their exposure to the domain boundary

Use the AI Assistant to trigger auto-detection: *"Detect and name the surfaces on my geometry"*
