# Surfaces

Surfaces (also called boundary patches) are named regions of the mesh boundary. Properly named surfaces are essential for applying boundary conditions in simulation and for organizing mesh exports.

## Why Name Surfaces?

Every face on the boundary of your mesh belongs to a surface. When you run a simulation, boundary conditions (inlet velocity, outlet pressure, wall type) are applied to surfaces **by name**. Clear, descriptive names make simulation setup faster and less error-prone.

## Naming Surfaces

### From the Surfaces Tab

1. Navigate to the **Surfaces** tab in your workspace
2. Click on a surface in the 3D viewer — it highlights
3. Enter a name in the surface panel (e.g., `inlet`, `outlet`, `car_body`)
4. The surface appears in the surface list with its name

### Recommended Naming Conventions

Use clear, lowercase names that describe the physical role:

| Name | Description |
|------|-------------|
| `inlet` | Flow entry surface |
| `outlet` | Flow exit surface |
| `wall` | Generic solid wall |
| `car_body` | Vehicle body surface |
| `ground` | Ground plane |
| `symmetry` | Symmetry plane |
| `top` / `side_left` / `side_right` | Far-field boundaries |
| `wheel_front_left` | Specific component surfaces |

```{tip}
Studio's AI Assistant and auto-detection features use surface names to automatically assign boundary conditions. Using standard names like `inlet`, `outlet`, and `wall` enables this automation.
```

## Per-Surface Mesh Controls

For STEP/IGES files with preserved face topology, you can set mesh parameters on individual surfaces:

### Surface Mesh Size

Override the global cell size for specific surfaces. Useful for:

- Finer resolution on aerodynamically important surfaces (leading edges, spoilers)
- Coarser resolution on less important surfaces (far-field, housing)

### Feature Angle

Controls how the mesher handles sharp edges. Faces meeting at angles greater than the feature angle threshold are treated as separate geometric features and receive refined meshing at the edge.

- **Low angle (15–30°)** — Captures more edges, finer mesh along features
- **High angle (45–60°)** — Only captures sharp edges, fewer refinement cells

## Surface Groups

For complex geometries with many faces, you can group surfaces:

- Select multiple faces in the 3D viewer (Shift + click)
- Assign them all to the same surface name
- They will be treated as a single boundary patch in simulation and export

## Surface Types in Export

When you export a mesh, each named surface becomes a boundary patch with a type:

| Surface Type | Description | Used For |
|-------------|-------------|----------|
| **Wall** | No-slip solid boundary | Car body, pipe walls, ground |
| **Inlet** | Flow entry | Duct entrance, wind tunnel inlet |
| **Outlet** | Flow exit | Duct exit, wind tunnel outlet |
| **Symmetry** | Mirror plane | Half-domain simulations |
| **Far-field** | Distant boundary | Top, sides of external domain |

The export format assigns appropriate type codes (e.g., wall=3, inlet=4 in Fluent format).

## Auto-Detection

Studio can automatically identify and name common boundary types:

- **Domain boundaries** — Inlet, outlet, top, sides, ground are named based on position
- **Geometry surfaces** — CAD face names from STEP files are preserved
- **Wheel detection** — Wheel-like surfaces are identified for rotating wall conditions

Use the AI Assistant to trigger auto-detection: *"Detect and name the surfaces on my geometry"*
