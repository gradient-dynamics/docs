# Workspace tour

Studio separates organisation-level work from project-level engineering while
keeping navigation consistent.

## Dashboard

The dashboard is the entry point for an organisation. Create a project, search
or sort existing work, review recent activity, and open the usage and member
management area. Project cards show the project type and current activity so
you can return to active work quickly.

## Project workspace

Each project contains its engineering assets and job history. The main areas
are:

| Area | Purpose |
|---|---|
| **Feature tree** | Navigate imported geometry, regions, surfaces, meshes, simulations and results. |
| **3D viewer** | Select and inspect geometry, mesh zones, boundaries and result fields. |
| **Setup panel** | Configure the active preprocessing, meshing, physics or output task. |
| **Job panel** | Follow queued, running, completed and failed jobs with live stage information. |
| **History** | Reopen previous meshes and simulations, preserving traceability between revisions. |

## Project lifecycle

1. Create a project for a single engineering question or design family.
2. Upload geometry and confirm units, orientation and topology.
3. Create named regions and surfaces.
4. Generate and review a mesh.
5. Create a simulation configuration from that mesh.
6. Run FluxCore and monitor the requested outputs.
7. Open the solution in post-processing and record the result.

Studio preserves the relationship between these resources so a solution can
always be traced back to the mesh and settings that produced it.
