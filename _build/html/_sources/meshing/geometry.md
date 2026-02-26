# Geometry

Before generating a mesh, you need to upload and validate your CAD geometry. Gradient Dynamics supports a range of industry-standard formats and provides automatic analysis and repair tools.

## Supported Formats

| Format | Extensions | Best For |
|--------|-----------|----------|
| **STEP** | .step, .stp | CAD assemblies with full topology — **recommended** |
| **IGES** | .iges, .igs | Legacy CAD exchange |
| **STL** | .stl | Surface meshes, 3D scans |
| **OBJ** | .obj | Polygon meshes |

```{admonition} Recommendation
:class: tip
Use **STEP** format whenever possible. STEP files preserve face topology, edge features, and multi-body assembly information. This enables per-surface mesh controls, automatic face detection, and better geometry repair.
```

## Uploading Geometry

1. Open your project workspace
2. Navigate to the **Setup** tab
3. Click **Upload Geometry**
4. Select your file — it will appear in the 3D viewer once processed

For STEP/IGES files, Studio automatically detects:
- Individual **solid bodies** in multi-body assemblies
- Named **faces** and **edges** from the CAD model
- Geometric **bounding dimensions** for automatic domain sizing

## Geometry Analysis

After upload, navigate to the **Geometry** tab to run analysis. Studio checks for:

### Watertightness
The surface must be completely closed (no gaps or holes) for volume mesh generation. Open surfaces will cause the mesher to fail or produce incorrect results.

### Manifold Status
Every edge should be shared by exactly two faces. Non-manifold edges (shared by 3+ faces) or non-manifold vertices indicate topology problems.

### Degenerate Elements
Extremely small or zero-area triangles/faces that can cause meshing failures.

## Geometry Repair

If issues are detected, Studio offers automatic repair options:

### Vertex Welding
For STL/OBJ files, vertices that are close together but not connected are merged. This fixes gaps caused by floating-point precision issues in mesh exports.

- Adjustable welding tolerance
- Preview the welded vs. original mesh to verify results

### Hole Filling
Small holes in the surface are automatically detected and patched with new triangles.

### Non-Manifold Edge Repair
Duplicate or overlapping faces near non-manifold edges are resolved.

### CAD Healing (STEP/IGES)
For CAD files, a deeper level of repair operates on the boundary representation (B-Rep):

- **Sewing** — Stitches adjacent faces that have small gaps between them
- **Gap filling** — Closes gaps between face edges
- **Tolerance adjustment** — Relaxes geometric tolerances to connect near-miss edges

```{tip}
The AI Assistant can analyze your geometry and recommend the best repair strategy. Just ask: *"Check if my geometry is ready for meshing"*
```

## Multi-Body Assemblies

When you upload a multi-body STEP file, Studio detects each solid body automatically. This is useful for:

- **Multi-region meshing** — Each body becomes a separate cell zone (e.g., fluid + solid regions for conjugate heat transfer)
- **Per-body mesh controls** — Different mesh sizes for different parts
- **Interface detection** — Touching bodies are automatically identified for region coupling

## Special Feature Detection

Studio can automatically detect certain geometric features:

- **Wheels** — Identifies wheel-like geometry on vehicles for rotating wall boundary conditions and MRF zones
- **Rotating features** — Detects axially symmetric bodies that may be fans, impellers, or propellers
- **Surface faces** — Groups faces by orientation and curvature for automatic surface naming

These detections can be triggered from the Geometry tab or via the AI Assistant.

## Viewer Controls

In the 3D viewer, you can interact with your geometry using:

| Action | Control |
|--------|---------|
| Rotate | Left-click drag |
| Pan | Right-click drag or Shift + left-click |
| Zoom | Scroll wheel |
| Select face | Click on a surface |
| Camera presets | Front / Back / Left / Right / Top / Bottom / Iso buttons |
| Display mode | Solid, Wireframe, Translucent, or Solid + Wireframe |
