# FluxCore objects

```{py:module} gradientdynamics.fluxcore
:no-index:
```

FluxCore objects describe the physical intent, boundary conditions, run
controls and requested engineering outputs of a simulation. Internal numerical
methods are selected and managed by FluxCore.

FluxCore is a full GPU-native CFD and multiphysics solver. Its GPU-native
linear-system subsystem solves the large sparse systems produced throughout
the nonlinear fluid, turbulence, energy and multi-region workflow. See
[Advanced solver controls](advanced-controls.md) for the public stability,
convergence, transient, thermal and compute policies.

## Simulation type

````{py:class} SimulationType

Supported public simulation families.

```{py:attribute} RANS
:value: "rans"

Steady turbulent fluid flow.
```

```{py:attribute} URANS
:value: "urans"

Time-resolved turbulent fluid flow.
```

```{py:attribute} CHT
:value: "cht"

Coupled fluid and solid heat transfer.
```
````

## Fluid

````{py:class} Fluid(*, density: float, dynamic_viscosity: float, specific_heat: float | None = None, thermal_conductivity: float | None = None)

Fluid properties in SI units.

```{py:method} air(*, temperature: float, pressure: float = 101325.0) -> Fluid
:classmethod:

Create an air model evaluated at the supplied thermodynamic state.
```

```{py:attribute} density
:type: float
```

```{py:attribute} dynamic_viscosity
:type: float
```

```{py:attribute} specific_heat
:type: float | None
```

```{py:attribute} thermal_conductivity
:type: float | None
```
````

## Boundary conditions

Boundary objects are mapped to names present in
{py:attr}`gradientdynamics.Mesh.boundaries`. Unknown names and incompatible
types are rejected before compute allocation.

````{py:class} Inlet(*, velocity: tuple[float, float, float], temperature: float | None = None, turbulence_intensity: float | None = None)

Velocity inlet with optional thermal and turbulence state.

```{py:attribute} velocity
:type: tuple[float, float, float]
```

```{py:attribute} temperature
:type: float | None
```
````

````{py:class} Outlet(*, pressure: float = 101325.0)

Static-pressure outlet.

```{py:attribute} pressure
:type: float
```
````

````{py:class} Wall(*, thermal: str = "adiabatic", temperature: float | None = None)

No-slip wall with an adiabatic or prescribed-temperature thermal condition.

```{py:method} adiabatic() -> Wall
:classmethod:

Create an adiabatic no-slip wall.
```

```{py:method} fixed_temperature(temperature: float) -> Wall
:classmethod:

Create a no-slip wall at a prescribed temperature.
```
````

````{py:class} RotatingWall(*, axis: tuple[float, float, float], origin: tuple[float, float, float], angular_speed: float, thermal: str = "adiabatic")

Wall rotating about an axis. Angular speed is in radians per second.
````

````{py:class} Symmetry()

Zero-normal-flux symmetry boundary.
````

````{py:class} Farfield(*, velocity: tuple[float, float, float], pressure: float = 101325.0, temperature: float = 300.0)

External-flow farfield state.
````

````{py:class} Periodic(*, pair: str, transform: Rotation | Translation)

Periodic boundary paired with another named patch. Both patches must be
conformal under the supplied transform.
````

## Run control

````{py:class} RunControl(*, iterations: int | None = None, residual_target: float | None = None, time_step: float | None = None, duration: float | None = None, output_interval: int | None = None)

Convenience factory for common run budgets. Use {py:class}`SteadyTimeControls`
or {py:class}`PhysicalTimeControls` when configuring pseudo-time methods,
inner iterations, physical-time order or separate output clocks.

```{py:method} steady(*, iterations: int = 2000, residual_target: float = 1e-6, output_interval: int = 100) -> RunControl
:classmethod:

Create controls for a steady simulation.
```

```{py:method} transient(*, time_step: float, duration: float, output_interval: int = 1) -> RunControl
:classmethod:

Create controls for a time-resolved simulation.
```
````

See {doc}`time-integration` for fixed and adaptive pseudo-time methods,
physical-time controls and inner convergence, and {doc}`output-controls` for
per-pseudo-step and per-physical-step output scheduling.

## Force outputs

````{py:class} ReferenceValues(*, area: float, velocity: float, density: float, moment_lengths: tuple[float, float, float] | None = None)

Reference quantities used to nondimensionalise forces and moments.
````

````{py:class} ForceOutput(*, name: str, surfaces: Sequence[str], drag_direction: tuple[float, float, float], lift_direction: tuple[float, float, float] | None = None, moment_center: tuple[float, float, float] | None = None, reference_values: ReferenceValues | None = None)

Named integrated force and moment request.

```{py:method} drag(*, name: str, surfaces: Sequence[str], direction: tuple[float, float, float] = (1.0, 0.0, 0.0), reference_values: ReferenceValues | None = None) -> ForceOutput
:classmethod:

Create a drag-oriented force request.
```
````

## Simulation configuration

````{py:class} SimulationConfig(*, simulation_type: SimulationType, fluid: Fluid, boundaries: Mapping[str, BoundaryCondition], run_control: RunControl | SteadyTimeControls | PhysicalTimeControls, outputs: Sequence[OutputRequest] = (), turbulence_model: TurbulenceModel | KOmegaSST | SpalartAllmaras | None = None, materials: Mapping[str, Material] | None = None, advanced: AdvancedControls | None = None)

Complete validated FluxCore request.

```{py:attribute} simulation_type
:type: SimulationType
```

```{py:attribute} fluid
:type: Fluid
```

```{py:attribute} boundaries
:type: Mapping[str, BoundaryCondition]
```

```{py:attribute} run_control
:type: RunControl | SteadyTimeControls | PhysicalTimeControls

Steady pseudo-time or physical-time advancement policy.
```

```{py:attribute} outputs
:type: Sequence[OutputRequest]
```

```{py:attribute} advanced
:type: AdvancedControls | None

Optional expert control surface. Omit it to use validated automatic policies.
```

```{py:method} rans(*, fluid: Fluid, boundaries: Mapping[str, BoundaryCondition], outputs: Sequence[OutputRequest] = (), run_control: RunControl | SteadyTimeControls | None = None, turbulence_model: TurbulenceModel | KOmegaSST | SpalartAllmaras = KOmegaSST(), advanced: AdvancedControls | None = None) -> SimulationConfig
:classmethod:

Create a steady turbulent-flow configuration.
```

```{py:method} urans(*, fluid: Fluid, boundaries: Mapping[str, BoundaryCondition], run_control: RunControl | PhysicalTimeControls, outputs: Sequence[OutputRequest] = (), turbulence_model: TurbulenceModel | KOmegaSST | SpalartAllmaras = KOmegaSST(), advanced: AdvancedControls | None = None) -> SimulationConfig
:classmethod:

Create a time-resolved turbulent-flow configuration.

DES and DDES are enabled by attaching {py:class}`DES` or {py:class}`DDES` to
the selected turbulence-model object. A physical-time run control is required.
```

```{py:method} cht(*, fluid: Fluid, materials: Mapping[str, Material], boundaries: Mapping[str, BoundaryCondition], run_control: RunControl | None = None, outputs: Sequence[OutputRequest] = (), advanced: AdvancedControls | None = None) -> SimulationConfig
:classmethod:

Create a multi-region conjugate heat-transfer configuration.
```

```{py:method} model_dump() -> dict[str, Any]

Return a JSON-compatible configuration for review and audit.
```
````

## Complete example

```python
from gradientdynamics.fluxcore import (
    Farfield,
    Fluid,
    ForceOutput,
    ReferenceValues,
    RunControl,
    SimulationConfig,
    Wall,
)

reference = ReferenceValues(
    area=2.2,
    velocity=25.0,
    density=1.184,
    moment_lengths=(2.8, 1.6, 2.8),
)

config = SimulationConfig.rans(
    fluid=Fluid.air(temperature=300.0),
    turbulence_model="k_omega_sst",
    boundaries={
        "farfield": Farfield(velocity=(25.0, 0.0, 0.0)),
        "vehicle_body": Wall.adiabatic(),
        "wheels": Wall.adiabatic(),
    },
    run_control=RunControl.steady(
        iterations=2500,
        residual_target=1e-6,
        output_interval=100,
    ),
    outputs=[
        ForceOutput.drag(
            name="vehicle_loads",
            surfaces=["vehicle_body", "wheels"],
            reference_values=reference,
        )
    ],
)

simulation = mesh.simulations.create(config)
solution = simulation.run().wait().result()
```

Unknown, retired or conflicting fields are rejected before compute allocation.
FluxCore validates mesh references, boundary names, region definitions,
required time controls and requested outputs while keeping its implementation
architecture private.
