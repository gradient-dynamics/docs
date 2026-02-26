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

## Mesh Export Formats

| Format | Extension | Solvers | Multi-Region | Tier |
|--------|-----------|---------|-------------|------|
| **VTU** | .vtu | ParaView, VTK tools | No | Free |
| **VTK Legacy** | .vtk | ParaView, legacy tools | No | Starter+ |
| **OpenFOAM** | polyMesh/ | OpenFOAM, foam-extend | Yes | Starter+ |
| **ANSYS Fluent** | .msh | ANSYS Fluent, CFX | Yes | Starter+ |
| **CGNS** | .cgns | Many commercial/OSS solvers | Yes | Starter+ |
| **Gmsh** | .msh | Gmsh, ElmerFEM, Code_Saturne | No | Starter+ |
| **Nastran** | .bdf | NASTRAN, MSC Patran | No | Starter+ |

### OpenFOAM Export Details

```
polyMesh/
├── points        # Vertex coordinates
├── faces         # Face-vertex connectivity
├── owner         # Face owner cell index
├── neighbour     # Face neighbor cell index
├── boundary      # Boundary patch definitions
└── cellZones     # Cell zone definitions (multi-region)
```

For multi-region cases, a `regionProperties` file is also included.

### ANSYS Fluent Export Details

- Binary .msh format
- Zone types: Fluid (1), Solid (17)
- Boundary types assigned from surface naming (wall, inlet, outlet)

### CGNS Export Details

- HDF5-based binary format
- Used as the default for CFD projects within Gradient Dynamics
- Supports multi-zone meshes with proper region labeling

## Simulation Results Format

| Format | Description |
|--------|-------------|
| **VTU** | Volumetric solution with all field data (velocity, pressure, turbulence) |
| **Point cloud** | Cell-center values as a point cloud (fallback for complex meshes) |

Results can be opened in ParaView for advanced post-processing beyond what's available in the browser.
