# Supported Formats

## Geometry Input Formats

| Format | Extensions | Features |
|--------|-----------|----------|
| **STEP** | .step, .stp | Full CAD topology, multi-body assemblies, named faces and edges. **Recommended.** |
| **IGES** | .iges, .igs | Legacy CAD exchange, face topology, multi-body support |
| **STL** | .stl | Triangle surface mesh (ASCII or binary). No topology. |
| **OBJ** | .obj | Polygon surface mesh. No topology. |

### Format Comparison

| Feature | STEP | IGES | STL | OBJ |
|---------|------|------|-----|-----|
| Face topology | Yes | Yes | No | No |
| Multi-body detection | Yes | Yes | No | No |
| Edge/feature detection | Yes | Partial | No | No |
| Per-face mesh controls | Yes | Yes | No | No |
| CAD healing | Yes | Yes | N/A | N/A |
| File size (typical) | Medium | Medium | Large | Large |

## Simulation Results

Results are available for download and visualization directly in Studio after a simulation completes.

| Format | Description |
|--------|-------------|
| **VTU** | Volumetric solution with all field data (velocity, pressure, turbulence) — open in ParaView for advanced post-processing |
| **Point cloud** | Cell-center values as a point cloud (fallback for complex meshes) |
