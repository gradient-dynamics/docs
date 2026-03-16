# Projects

Projects are the top-level organizational unit in Gradient Dynamics Studio. Every piece of work — geometry, meshes, simulations, results — lives within a project.

## Project Types

### Meshing Projects

Meshing projects focus on generating high-quality computational meshes. Use these when you:

- Want fine-grained control over mesh topology and quality before linking to a simulation
- Need to review and approve mesh quality as a separate step from simulation
- Are generating meshes to share across multiple CFD projects

**Available workflow stages:** Geometry → Domain Setup → Mesh Settings → Surfaces → Regions → Quality

### CFD Projects

CFD projects provide the full simulation workflow. Use these when you want to run simulations directly in Gradient Dynamics.

**Available workflow stages:** Geometry → Mesh → Simulation Setup → Run → Post-Processing

## Creating a Project

1. From the **Dashboard**, click **New Project**
2. Choose the project type: **Meshing** or **CFD**
3. Enter a project name and optional description
4. Click **Create**

## Dashboard

The dashboard displays all your projects as cards showing:

- Project name and type (Meshing / CFD)
- Creation date
- Last modified date

Use the filter buttons to show only **Meshing** or **CFD** projects.

## Project Limits

The number of projects you can create depends on your subscription tier:

All subscription tiers have **unlimited projects**.

See [Subscription Tiers](/reference/subscription-tiers.md) for full tier details.
