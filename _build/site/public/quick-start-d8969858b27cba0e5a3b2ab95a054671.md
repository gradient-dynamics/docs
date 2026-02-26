# Quick Start

This guide walks you through creating your first meshing and CFD project in Gradient Dynamics Studio. By the end, you'll have generated a mesh around a geometry and run a simple aerodynamic simulation.

## Step 1: Sign In

Open Gradient Dynamics Studio in your browser and sign in with your account. You'll land on the **Dashboard**, which shows all your projects.

## Step 2: Create a Meshing Project

1. Click **New Project** on the dashboard
2. Select **Meshing** as the project type
3. Give your project a name (e.g., "My First Mesh")
4. Click **Create**

You'll be taken to the project workspace.

## Step 3: Upload Geometry

1. In the **Setup** tab, click **Upload Geometry**
2. Select your CAD file — supported formats are:
   - **STEP** (.step, .stp) — recommended for best feature preservation
   - **IGES** (.iges, .igs)
   - **STL** (.stl)
   - **OBJ** (.obj)
3. Your geometry will appear in the 3D viewer

```{tip}
STEP files preserve the most geometric detail (faces, edges, topology). Use STEP whenever possible for the best meshing results.
```

## Step 4: Check Geometry Health

Navigate to the **Geometry** tab. Studio automatically analyzes your geometry for:

- **Watertightness** — Is the surface fully closed?
- **Manifold status** — Are there non-manifold edges or vertices?
- **Topology issues** — Degenerate faces, self-intersections

If issues are found, use the **Repair** options (vertex welding, hole filling) or ask the AI Assistant for help.

## Step 5: Configure the Domain

Back in the **Setup** tab:

1. **Select a domain type:**
   - **External** — Flow around an object (vehicles, aircraft, buildings)
   - **Internal** — Flow inside a geometry (pipes, ducts, enclosures)
   - **Rotating** — Turbomachinery (fans, pumps, turbines)

2. For **External** domains, a bounding box automatically appears around your geometry in the 3D viewer. Adjust the padding distances (upstream, downstream, sides, top) or use the defaults.

3. Optionally enable **ground plane** for vehicle aerodynamics.

## Step 6: Set Mesh Parameters

Navigate to the **Mesh Settings** tab:

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| **Target cell size** | Base cell size in the domain | 0.01 – 1.0 m |
| **Min cell size** | Smallest allowed cell | 0.001 – 0.1 m |
| **Refinement levels** | Octree refinement depth | 6 – 12 |

### Enable Boundary Layers (recommended for CFD)

Boundary layers are critical for capturing near-wall flow physics:

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| **Number of layers** | Prism layers on wall surfaces | 5 – 15 |
| **First layer height** | Controls y+ value | 0.00001 – 0.001 m |
| **Growth rate** | Layer thickness expansion | 1.15 – 1.2 |

```{tip}
Use the **y+ calculator** to determine the correct first layer height for your flow conditions. For standard RANS with k-ω SST, target y+ ≈ 30.
```

## Step 7: Add Refinement Zones (Optional)

In the **Setup** tab, add refinement zones to capture flow features:

- **Box** — Rectangular region (good for wakes, ground effects)
- **Cylinder** — Cylindrical region (good for rotating zones, jet flows)
- **Sphere** — Spherical region (good for point sources, probes)

Drag and resize zones directly in the 3D viewer or enter exact coordinates.

## Step 8: Name Surfaces

In the **Surfaces** tab, assign names to boundary patches:

1. Click on a surface in the 3D viewer to select it
2. Give it a descriptive name: `inlet`, `outlet`, `wall`, `car_body`, `ground`, etc.
3. These names carry through to your exported mesh and simulation setup

## Step 9: Generate the Mesh

1. Click **Generate Mesh**
2. The job is submitted to cloud GPUs
3. Monitor progress in the **Logs** panel
4. Once complete, the mesh appears in the 3D viewer

Review mesh quality in the **Mesh Quality** tab — check skewness, aspect ratio, and non-orthogonality histograms.

## Step 10: Export or Simulate

You can now:

- **Export** the mesh in the **Export** tab (OpenFOAM, Fluent, CGNS, VTU, Gmsh, Nastran)
- **Create a CFD project** to run a simulation using this mesh

---

## Running a CFD Simulation

### Create a CFD Project

1. Return to the Dashboard and click **New Project**
2. Select **CFD** as the project type
3. Select the mesh you generated (or upload one)

### Configure the Simulation

In the **Simulation** tab:

1. **Turbulence model** — Select k-ω SST (recommended for most external flows)
2. **Boundary conditions** — Studio auto-detects boundaries from your named surfaces:
   - Set inlet velocity (e.g., 30 m/s)
   - Set outlet pressure (typically 0 Pa gauge)
   - Walls are automatically set as no-slip
3. **Solver settings** — SIMPLE algorithm with default relaxation factors works for most cases
4. **Max iterations** — 500–2000 for steady-state RANS

### Run the Simulation

1. Click **Run Simulation** — the credit cost estimate is shown before you confirm
2. Monitor **live residuals** in the convergence plot
3. Watch for residuals dropping below your convergence criteria

### View Results

Once complete, switch to the **Results** tab:

- **Surface coloring** — Color boundaries by pressure, velocity, or turbulence fields
- **Slice planes** — Cut through the domain to see internal flow structure
- **Streamlines** — Trace flow paths through the domain
- **Forces** — Calculate drag, lift, and moment coefficients

---

## Using the AI Assistant

At any point, open the **AI Assistant** panel and ask questions in natural language:

> "Set up an external aerodynamics mesh for this car geometry"

> "What boundary layer settings should I use for highway speed?"

> "Run a simulation at 60 mph with k-omega SST"

The assistant analyzes your geometry, suggests configurations, and can directly apply settings with your confirmation. See [AI Assistant Overview](/agent/overview.md) for a full guide.
