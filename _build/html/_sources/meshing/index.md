# Meshing

Meshing converts geometry into the computational cells used by Gradient Dynamics solvers and supported export workflows. Studio is designed to guide this process from geometry upload through mesh quality review.

## Available Mesh Types

Gradient Dynamics supports two meshing types:

| Mesh Type | Best For | Notes |
|-----------|----------|-------|
| **Structured** | Fast setup, repeatable workflows, external and internal flow, thermal studies, and common multiphysics projects. | Recommended starting point for most Studio users. |
| **Unstructured** | Complex topology, interoperability, imported-mesh workflows, and cases that require flexible element layouts. | Use when the project requirements call for an unstructured mesh. |

## Meshing Workflow

1. Upload geometry in a supported CAD or surface format.
2. Check geometry health and repair issues that would prevent volume meshing.
3. Define the domain, named surfaces, and regions.
4. Choose structured or unstructured meshing.
5. Set resolution, boundary-layer, and local refinement controls.
6. Generate the mesh and review quality before simulation.

## Topics

- [Geometry](geometry.md)
- [Domain Setup](domain-setup.md)
- [Mesh Settings](mesh-settings.md)
- [Near-Wall Resolution](boundary-layers.md)
- [Refinement Zones](refinement-zones.md)
- [Surfaces](surfaces.md)
- [Multi-Region Meshing](multi-region.md)
- [Conformal vs Non-Conformal Meshes](conformal-nonconformal.md)
- [Mesh Quality](mesh-quality.md)
