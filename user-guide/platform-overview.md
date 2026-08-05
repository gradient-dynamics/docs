# Platform overview

Gradient Dynamics is a cloud simulation platform built around two connected
products:

- **Studio** is the browser workspace where engineers prepare geometry, build
  meshes, configure cases, monitor runs, review results and collaborate.
- **FluxCore** is the GPU-native simulation engine that executes fluid and
  coupled thermal workloads behind Studio.

The platform keeps project data, compute and results together. A project is a
traceable engineering record rather than a loose collection of local files.
Geometry revisions, meshes, run settings, logs and outputs remain associated
with the decision they support.

## Core resources

The product is organised around a small set of engineering resources.

| Resource | Purpose |
|---|---|
| **Organisation** | The shared workspace, members, access, storage and compute usage for a team. |
| **Project** | A product, design question, validation exercise or study campaign. |
| **Geometry** | The imported CAD or surface description and its prepared revisions. |
| **Mesh** | The discretised fluid and solid regions, named boundaries and quality record. |
| **Simulation** | Physics, material, boundary-condition and run configuration applied to a mesh. |
| **Solution** | Fields, histories, force or thermal outputs, files and visualisations produced by a run. |

This resource model is also the foundation of the forthcoming public API.

## What runs in the browser

Studio provides interactive tools for geometry inspection, setup and results
review. Heavy meshing and simulation work runs on managed compute. You can
close the browser after submitting a job and return to its project later; the
project keeps the job state, logs and generated assets.

## What the platform manages

Gradient Dynamics manages solver environments, accelerator provisioning,
execution queues, result persistence and supported software versions. Your
team manages the engineering intent: geometry, operating conditions, material
properties, refinement, outputs and acceptance criteria.

```{important}
Cloud execution removes infrastructure work, not engineering responsibility.
Always review geometry, mesh quality, boundary conditions, convergence and
validation evidence before using a result for a design decision.
```
