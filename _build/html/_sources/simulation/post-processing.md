# Post-Processing

After your simulation completes, the **Results** tab provides interactive 3D visualization and analysis tools to extract engineering insight from your data.

## Available Fields

| Field | Symbol | Unit | Description |
|-------|--------|------|-------------|
| **Velocity** | U | m/s | Flow velocity vector |
| **Pressure** | p | Pa | Static pressure |
| **Turbulent kinetic energy** | k | m²/s² | Turbulence intensity measure |
| **Specific dissipation rate** | ω | 1/s | Turbulence frequency (k-ω models) |
| **Dissipation rate** | ε | m²/s³ | Turbulence dissipation (k-ε model) |
| **Turbulent viscosity** | νt | m²/s | Effective turbulent diffusivity |
| **Wall distance** | d | m | Distance from nearest wall |

## Visualization Tools

### Surface Coloring

Color boundary surfaces by any field value:

1. In the Results tab, select a **field** from the dropdown (e.g., Pressure)
2. Surface patches are colored according to the field values
3. Adjust the **colormap** (jet, viridis, coolwarm, etc.)
4. Set the **range** manually or use auto-scaling

**Use for:** Identifying high/low pressure zones, wall shear patterns, temperature distributions

### Slice Planes

Create cross-sectional cuts through the domain to see internal flow structure:

1. Click **Add Slice**
2. Choose the plane orientation (X, Y, or Z normal)
3. Drag the plane position in the 3D viewer or enter a coordinate
4. Select the field to display on the slice
5. The slice shows a colored contour of the field values

**Use for:** Visualizing wake structures, pressure distribution through the domain, internal flow patterns

### Isosurfaces

Create 3D surfaces where a field has a constant value:

1. Click **Add Isosurface**
2. Select the field (e.g., Velocity magnitude)
3. Set the isovalue
4. A 3D surface appears showing all points where the field equals that value

**Use for:** Identifying vortex cores (low pressure isosurfaces), wake boundaries (velocity isosurfaces), recirculation zones

### Streamlines

Trace the path that fluid particles follow through the domain:

1. Click **Add Streamlines**
2. Place seed points or a seeding line/plane in the 3D viewer
3. Streamlines are computed forward (and optionally backward) from the seeds
4. Color streamlines by velocity, pressure, or other fields

**Use for:** Understanding flow paths, identifying recirculation, visualizing how flow moves around geometry

### Glyphs (Vectors)

Display velocity vectors as arrows at discrete points:

1. Click **Add Glyphs**
2. Configure arrow density and scaling
3. Arrows show the direction and magnitude of the velocity field

**Use for:** Understanding flow direction at specific locations, identifying stagnation points and flow turning

## Quantitative Analysis

### Force and Moment Calculation

Calculate aerodynamic forces on selected surfaces:

1. Click **Forces** in the analysis tools
2. Select the surface(s) to calculate forces on (e.g., `car_body`)
3. Set the reference parameters:
   - Reference area (frontal area for drag, planform area for lift)
   - Reference velocity (freestream velocity)
   - Reference length (for moment coefficients)
4. Results show:

| Quantity | Description |
|----------|-------------|
| **Drag force (Fd)** | Force in the freestream direction |
| **Lift force (Fl)** | Force perpendicular to freestream |
| **Side force** | Lateral force |
| **Drag coefficient (Cd)** | Normalized drag |
| **Lift coefficient (Cl)** | Normalized lift |
| **Moment coefficients (Cm)** | Pitching, rolling, yawing moments |

### Point Probes

Query field values at specific locations:

1. Click **Probe**
2. Click a point in the 3D viewer or enter coordinates
3. The field values at that point are displayed

### Line Probes

Extract field values along a line for 1D plotting:

1. Click **Line Probe**
2. Define start and end points
3. A 1D plot shows the selected field value along the line

**Use for:** Comparing velocity profiles at different stations, checking pressure distribution along a surface

## Viewer Controls

### Colormaps

Available colormaps:
- **Jet** — Rainbow (blue → green → yellow → red)
- **Viridis** — Perceptually uniform (dark purple → yellow)
- **Coolwarm** — Diverging (blue → white → red) — good for showing positive/negative
- **Plasma** — Perceptually uniform warm palette
- **Inferno** — Dark to bright warm palette

### Range Control

- **Auto** — Automatically scales to the min/max values in the visible data
- **Manual** — Set custom min/max values to highlight specific ranges
- **Symmetric** — Centers the range around zero (good for diverging quantities like pressure coefficient)

### Display Options

| Option | Description |
|--------|-------------|
| **Mesh wireframe** | Overlay mesh edges on surfaces |
| **Clipping planes** | Cut away parts of the domain |
| **Region toggle** | Show/hide specific boundary patches |
| **Transparency** | Make surfaces translucent |
| **Camera presets** | Front, Back, Left, Right, Top, Bottom, Isometric views |

## Downloading Results

Export your simulation results for further analysis:

- **VTU format** — Complete volumetric solution (open in ParaView for advanced post-processing)
- **Screenshots** — Capture the current view directly from the viewer
