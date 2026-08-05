# Python API reference

<div class="api-status">Design preview · no installable SDK yet</div>

The planned `gradientdynamics` package exposes Studio concepts as typed Python
objects. Projects own versioned geometry, meshes, simulations and solutions;
long-running work returns a job object that can be inspected, waited on or
cancelled.

```{important}
This is a design preview for integration planning. The package name, signatures
and types can change before general availability. Studio remains the supported
self-service interface and no public Python package or credentials are
currently available.
```

## Object-first workflow

```python
from gradientdynamics import Client
from gradientdynamics.fluxcore import (
    Farfield,
    ForceOutput,
    Fluid,
    SimulationConfig,
    Wall,
)
from gradientdynamics.meshing import PrismLayers, PrismOctreeConfig

gd = Client.from_environment()

project = gd.projects.create(name="Road-car baseline")
geometry = project.geometry.upload("drivaer.stl")

mesh_job = geometry.mesh(
    PrismOctreeConfig(
        target_cell_count=12_000_000,
        minimum_spacing=0.002,
        maximum_spacing=0.5,
        prism_layers=PrismLayers(count=12, first_height=0.0002),
    )
)
mesh = mesh_job.wait().result()

simulation = mesh.simulations.create(
    SimulationConfig.rans(
        fluid=Fluid.air(temperature=300.0),
        boundaries={
            "farfield": Farfield(velocity=(30.0, 0.0, 0.0)),
            "vehicle": Wall.adiabatic(),
        },
        outputs=[ForceOutput.drag(name="vehicle_drag", surfaces=["vehicle"])],
    )
)

solution = simulation.run().wait().result()
print(solution.outputs["vehicle_drag"].coefficient)
solution.fields.download("road_car.cgns")
```

The example shows intended object relationships, not currently executable
code.

## Package map

| Namespace | Main objects |
|---|---|
| `gradientdynamics` | {py:class}`Client`, {py:class}`Project`, {py:class}`Geometry`, {py:class}`Mesh`, {py:class}`Simulation`, {py:class}`Solution` |
| `gradientdynamics.meshing` | `PrismOctreeConfig`, `PrismLayers`, `RefinementBox`, `CHTMeshConfig` |
| `gradientdynamics.fluxcore` | `SimulationConfig`, model-specific turbulence, DES/DDES, physical and pseudo-time integration, per-system GPU-native linear policies, multigrid and scheduled outputs |
| `gradientdynamics.jobs` | `Job`, `JobStatus`, progress and cancellation |
| `gradientdynamics.outputs` | `Asset`, `FieldCollection`, `History`, `ForceResult` |
| `gradientdynamics.exceptions` | Typed validation, capacity, resource and execution errors |

## Resource lifecycle

```text
Client
└── Project
    ├── Geometry ──mesh()──────────────▶ Job[Mesh] ──result()──▶ Mesh
    ├── Mesh ──────simulations.create()────────────────────────▶ Simulation
    └── Simulation ──run()─────────────▶ Job[Solution] ────────▶ Solution
                                                               ├── outputs
                                                               ├── histories
                                                               └── fields
```

```{toctree}
:maxdepth: 1

Client and availability <availability>
Core objects <resources>
Meshing objects <meshing>
FluxCore objects <fluxcore>
Advanced solver controls <advanced-controls>
Turbulence, DES and DDES <turbulence>
Physical and pseudo-time <time-integration>
Linear solvers and multigrid <linear-solvers>
Output and monitoring controls <output-controls>
Jobs and status <jobs>
Solutions and outputs <outputs>
Exceptions and limits <errors>
```
