# Domain Setup

The **domain** defines the region of space that will be meshed. Different simulation types require different domain configurations. Domain setup is done in the **Setup** tab of your project workspace.

## Domain Types

### External Flow

For simulating flow **around** an object — vehicles, aircraft, buildings, bluff bodies.

Studio generates a Cartesian bounding box (wind tunnel) around your geometry with configurable padding:

| Parameter | Description | Default |
|-----------|-------------|---------|
| **Upstream** | Distance ahead of geometry | 1.5× geometry length |
| **Downstream** | Distance behind geometry (wake capture) | 3.0× geometry length |
| **Side (left/right)** | Lateral distance | 1.5× geometry width |
| **Top** | Distance above | 2.0× geometry height |
| **Bottom** | Distance below | 0× (geometry on ground) |

**Options:**
- **Ground plane** — Places the geometry on a flat ground surface. Essential for vehicle aerodynamics where ground effect matters.
- **Symmetry plane** — Meshes only half the domain and mirrors results. Halves compute cost for symmetric geometries.

```{tip}
For vehicle aerodynamics, use a ground plane and ensure the bottom padding is 0 so the car sits on the ground. For aircraft, increase the bottom padding to avoid ground interference.
```

**How it works in the backend:**

When you select External Flow, the mesher:
1. Constructs the Cartesian domain bounding box from the padding parameters
2. Loads the uploaded geometry as a closed surface
3. Runs a fluid/solid classification step — the geometry surface defines the interior (solid) region, and the volume between the geometry and the domain box is the fluid region
4. Applies the block AMR hierarchy to the fluid region, refining near the geometry surface using cut-cells
5. Named selections for domain boundary faces (inlet, outlet, top, sides) are assigned automatically based on their position relative to the flow direction

### Internal Flow

For simulating flow **inside** a geometry — pipes, ducts, manifolds, enclosures, HVAC systems.

The domain is defined by the interior volume of your geometry. Studio automatically:

- Identifies the fluid volume enclosed by the surfaces
- Detects inlet and outlet faces (the open ends of the geometry)
- Sizes the mesh based on the smallest internal dimension

**How it works in the backend:**

When you select Internal Flow:
1. The mesher computes the enclosed interior volume of the uploaded geometry
2. Inlet and outlet surfaces are identified as open faces (holes in the surface) or by named selections you assign in the Surfaces tab
3. The Cartesian block AMR grid is constructed to fill the interior volume
4. Cut-cells are formed where the Cartesian grid intersects the interior walls
5. Interior wall surfaces automatically become wall-type boundary patches

```{note}
For internal flow geometries, **the geometry must be watertight** except at the intended inlet and outlet openings. Any gap in the surface other than at inlets/outlets will allow fluid to escape the domain and cause the mesher to fail to identify the correct interior.
```

### Rotating Machinery

For rotating equipment — fans, pumps, turbines, compressors, propellers.

This domain type creates:

- A **rotating zone** around the moving geometry (MRF — Multiple Reference Frame)
- A **stationary zone** for the surrounding fluid
- An **interface** between the zones

Configure the rotation axis, speed (RPM), and zone dimensions in the Setup tab.

**How it works in the backend:**

The rotating zone is meshed as a cylindrical sub-domain, and the AMR block hierarchy is constructed independently within each zone. At the rotating/stationary interface, a non-conformal interface is created — values are interpolated across the zone boundary using an area-weighted flux exchange. This approach is used for steady-state simulations (frozen-rotor). For transient sliding mesh, the interface is updated each time step.

### Conjugate Heat Transfer (CHT)

For problems involving heat exchange between fluid and solid regions — heat sinks, cold plates, electronics cooling.

CHT domain setup requires:

- At least two regions (one fluid, one solid)
- Properly defined interfaces between touching regions
- Material properties for each region

### Solid Body

For meshing the interior of a solid geometry — used for thermal analysis or structural simulations without fluid flow.

## Domain Shapes

The enclosing domain can take different shapes depending on your application:

| Shape | Best For |
|-------|----------|
| **Box** | Vehicle aerodynamics, buildings, general external flow |
| **Cylinder** | Axisymmetric bodies, rotors, vertical structures |
| **C-Domain** | Airfoils and 2D-like aerodynamics |
| **O-Domain** | Cylinders, cables, circular cross-sections |

## Configuring the Domain

### Automatic Sizing

When you select a domain type, Studio automatically sizes the domain based on your geometry's bounding box. The defaults work well for most cases.

### Manual Adjustment

You can adjust the domain in two ways:

1. **Numerical input** — Enter exact dimensions in the Setup panel
2. **3D viewer** — Drag the domain box handles directly in the viewer

### Domain Visualization

The domain boundary appears as a semi-transparent box in the 3D viewer. You can:

- See the geometry positioned within the domain
- Verify adequate clearance on all sides
- Check that the domain is large enough to avoid boundary interference

```{admonition} Domain Size Guidelines
:class: note

**Too small:** Boundary effects contaminate the solution. Flow doesn't develop properly before hitting the outlet.

**Too large:** Wastes cells on far-field regions, increasing compute cost without improving accuracy near the geometry.

The defaults strike a good balance for most applications. Increase downstream distance for bluff bodies with large wakes.
```

## Named Selections

Named selections (also called boundary patches) are how Studio identifies different surface regions for boundary condition assignment. When you generate a mesh, every face on the domain boundary belongs to a named selection.

Studio automatically creates named selections for domain boundaries:

| Named Selection | External Flow | Internal Flow |
|----------------|--------------|---------------|
| `inlet` | Upstream face of the domain box | Open inlet face(s) of the geometry |
| `outlet` | Downstream face of the domain box | Open outlet face(s) of the geometry |
| `top` | Top face of the domain box | — |
| `side_left`, `side_right` | Side faces | — |
| `ground` | Bottom face (if ground plane enabled) | — |
| `symmetry` | Symmetry cut plane (if enabled) | — |
| Geometry surfaces | Automatically from CAD face names | Interior walls |

You can view and rename all named selections in the **Surfaces** tab. See [Surfaces](surfaces.md) for full details.

## Meshing Time

Once you click **Generate Mesh**, the job is dispatched to cloud GPUs. Typical generation times:

| Mesh Size | Typical Time |
|-----------|-------------|
| < 5 million cells | 1 – 3 minutes |
| 5 – 20 million cells | 3 – 8 minutes |
| 20 – 100 million cells | 8 – 30 minutes |
| > 100 million cells | 30 minutes – 1 hour |

These are approximate. Actual time depends on:

- **Geometry complexity** — More surface features and curvature require more cut-cell processing
- **AMR depth** — More refinement levels increase both cell count and the number of block classification operations
- **Number of refinement zones** — Each zone adds an additional refinement pass
- **Domain size** — Larger domains with more coarse-level blocks take longer to initialize

```{tip}
For a rough estimate: expect **1–10 million cells per minute** of meshing time, with complex high-AMR meshes at the lower end and simple geometries at the upper end.
```

You can monitor meshing progress and intermediate cell counts in the **Logs** panel.
