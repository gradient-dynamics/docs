# Meshing

Meshing converts geometry into the computational cells used by Gradient Dynamics solvers and supported export workflows. Studio is designed to guide this process from geometry upload through mesh quality review.

## Available Mesh Types

Gradient Dynamics supports two meshing types:

| Mesh Type | Best For | Notes |
|-----------|----------|-------|
| **Unstructured** | Production CFD, complex topology, boundary-layer workflows, interoperability, imported-mesh workflows, and cases that require flexible element layouts. | Recommended starting point for most Studio users. |
| **Structured** | Fast setup, repeatable workflows, geometry screening, parametric studies, and cases where a structured approach fits the solver and validation target. | Use when automation, repeatability, or structured-mesh requirements are the priority. |

## Meshing Workflow

1. Upload geometry in a supported CAD or surface format.
2. Check geometry health and repair issues that would prevent volume meshing.
3. Define the domain, named surfaces, and regions.
4. Choose unstructured or structured meshing.
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

```{toctree}
:maxdepth: 1
:hidden:

Geometry <geometry>
Domain setup <domain-setup>
Mesh settings <mesh-settings>
Near-wall resolution <boundary-layers>
Refinement zones <refinement-zones>
Surfaces <surfaces>
Multi-region meshing <multi-region>
Conformal and non-conformal meshes <conformal-nonconformal>
Mesh quality <mesh-quality>
Export <export>
```
