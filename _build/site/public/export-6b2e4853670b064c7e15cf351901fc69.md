# Mesh Export

Once your mesh is generated and quality-checked, export it in your solver's format from the **Export** tab.

## Supported Export Formats

| Format | Extension | Solver Compatibility |
|--------|-----------|---------------------|
| **OpenFOAM** | polyMesh directory | OpenFOAM, foam-extend |
| **ANSYS Fluent** | .msh | ANSYS Fluent, ANSYS CFX |
| **CGNS** | .cgns | Many commercial and open-source solvers |
| **VTU** | .vtu | ParaView, VTK-based tools |
| **VTK Legacy** | .vtk | ParaView, legacy VTK tools |
| **Gmsh** | .msh | Gmsh, ElmerFEM, Code_Saturne |
| **Nastran** | .bdf | NASTRAN, structural analysis tools |

```{note}
The **Free** tier is limited to VTU export only. All other formats require a **Starter** tier or higher subscription.
```

## Format Details

### OpenFOAM

Exports a complete `polyMesh` directory structure:

```
polyMesh/
├── points        # Node coordinates
├── faces         # Face definitions
├── owner         # Face-to-cell ownership
├── neighbour     # Face neighbor cells
├── boundary      # Boundary patch definitions
└── cellZones     # Region zone definitions (multi-region)
```

- Boundary patches are named according to your surface names
- Multi-region meshes include `cellZones` and `regionProperties` files
- Ready to drop into an OpenFOAM case directory

### ANSYS Fluent

Exports a `.msh` file with:

- Proper zone type assignment (Fluid = type 1, Solid = type 17)
- Named boundary patches matching your surface names
- Wall, inlet, outlet zone types automatically set

### CGNS

Cross-platform CFD format using HDF5:

- Supports multi-zone meshes
- Used as the default for CFD projects within Gradient Dynamics
- Compatible with a wide range of solvers

### VTU (VTK XML)

Modern VTK format for visualization and post-processing:

- Full polyhedral cell support
- Compact XML format
- Directly openable in ParaView

### Gmsh

Gmsh mesh format for further mesh editing:

- Useful if you need to modify the mesh topology
- Compatible with Gmsh's mesh editing and refinement tools

### Nastran

Bulk Data File (.bdf) format for structural analysis:

- Used with NASTRAN, MSC Patran, and similar FEA tools
- Appropriate for structural/thermal meshes (Solid Body domain type)

## Export Options

Depending on the format, you may have additional options:

| Option | Description | Formats |
|--------|-------------|---------|
| **Binary** | Compress output for smaller file size | VTU, Fluent |
| **Include patches** | Export boundary patches as separate files | VTU (VTP), OpenFOAM |
| **Include zones** | Include cell zone information | Fluent, OpenFOAM, CGNS |

## Downloading

After selecting your format and options:

1. Click **Export**
2. The export is prepared (may take a moment for large meshes)
3. A download link appears — click to download the mesh files

For OpenFOAM format, the files are bundled into a ZIP archive.

## Using Exported Meshes

### In OpenFOAM

```
myCase/
├── 0/           # Initial conditions
├── constant/
│   └── polyMesh/  ← Extract here
├── system/
│   ├── controlDict
│   ├── fvSchemes
│   └── fvSolution
```

### In ANSYS Fluent

1. Open Fluent
2. File → Read → Mesh → Select the .msh file
3. Check mesh quality and zones in the console
4. Proceed with case setup

### In ParaView

1. Open ParaView
2. File → Open → Select the .vtu file
3. Click Apply to load
4. Use filters for visualization
