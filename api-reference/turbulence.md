# Turbulence models

```{py:currentmodule} gradientdynamics.fluxcore
```

Turbulence is configured with model-specific Python objects. Each object
exposes only controls meaningful to that model, so invalid combinations are
rejected before a job is submitted.

## Enumerations

````{py:class} TurbulenceModel

Supported turbulence-model families.

```{py:attribute} LAMINAR
:value: "laminar"
```

```{py:attribute} K_OMEGA_SST
:value: "k_omega_sst"
```

```{py:attribute} SPALART_ALLMARAS
:value: "spalart_allmaras"
```
````

````{py:class} WallTreatment

Near-wall modelling policy.

```{py:attribute} LOW_RE
:value: "low_re"

Resolve the viscous sublayer. Use a mesh with appropriate first-cell height.
```

```{py:attribute} WALL_FUNCTION
:value: "wall_function"

Apply a wall-modelled treatment for meshes designed around wall functions.
```

```{py:attribute} AUTOMATIC
:value: "automatic"

Select a compatible treatment from mesh resolution and boundary metadata.
```
````

## RANS models

````{py:class} KOmegaSST(*, wall_treatment: WallTreatment | str = "low_re", inlet_intensity: float = 0.01, inlet_viscosity_ratio: float = 10.0, production_limiter: float | None = None, turbulent_prandtl: float = 0.85, minimum_tke: float | None = None, minimum_specific_dissipation: float | None = None, scale_resolving: DES | DDES | None = None)

Two-equation shear-stress-transport turbulence model.

```{py:attribute} inlet_intensity
:type: float

Freestream turbulence intensity as a fraction.
```

```{py:attribute} inlet_viscosity_ratio
:type: float

Freestream turbulent-to-molecular viscosity ratio.
```

```{py:attribute} production_limiter
:type: float | None

Optional upper limiter for turbulent production. Omit for the validated model
default.
```

```{py:attribute} scale_resolving
:type: DES | DDES | None

Optional detached-eddy formulation. Requires physical-time advancement.
```
````

````{py:class} SpalartAllmaras(*, wall_treatment: WallTreatment | str = "low_re", inlet_modified_viscosity_ratio: float = 3.0, formulation: str = "standard", minimum_working_variable: float | None = None, production_limiter: float | None = None, scale_resolving: DES | DDES | None = None)

One-equation turbulence model with optional detached-eddy behaviour.

```{py:attribute} inlet_modified_viscosity_ratio
:type: float

Freestream modified turbulent-viscosity ratio.
```

```{py:attribute} formulation
:type: Literal["standard", "negative"]

Working-variable formulation. The negative variant permits controlled negative
values during difficult startup transients.
```

```{py:attribute} scale_resolving
:type: DES | DDES | None

Optional detached-eddy formulation. Requires physical-time advancement.
```
````

## Scale-resolving modes

````{py:class} DES(*, constant: float | None = None, length_scale: str = "cell_volume", low_dissipation: bool = True, limiter_relaxation: float = 1.0)

Detached Eddy Simulation configuration for supported turbulence models.

```{py:attribute} constant
:type: float | None

Optional model constant override. Omit to use the validated constant for the
selected turbulence family.
```

```{py:attribute} length_scale
:type: Literal["cell_volume", "maximum_edge"]

Grid length used by the scale-resolving model.
```

```{py:attribute} low_dissipation
:type: bool

Use the time-resolved spatial policy intended to preserve resolved turbulent
structures.
```
````

````{py:class} DDES(*, constants: Mapping[str, float] | None = None, length_scale: str = "cell_volume", shielding: str = "automatic", shielding_strength: float = 1.0, low_dissipation: bool = True, limiter_relaxation: float = 1.0)

Delayed Detached Eddy Simulation configuration with near-wall shielding.

```{py:attribute} constants
:type: Mapping[str, float] | None

Optional model-family constants. Unspecified entries use validated defaults.
```

```{py:attribute} shielding
:type: Literal["automatic", "standard", "strong"]

Near-wall shielding policy used to protect attached boundary layers from
premature grid-induced mode switching.
```

```{py:attribute} shielding_strength
:type: float

Multiplier applied to the selected shielding policy.
```
````

```{important}
DES and DDES require {py:class}`PhysicalTimeControls`. FluxCore rejects these
modes for a steady RANS configuration because the resolved turbulent content
must evolve in physical time.
```

## DDES example

```python
from gradientdynamics.fluxcore import DDES, KOmegaSST, WallTreatment

turbulence = KOmegaSST(
    wall_treatment=WallTreatment.LOW_RE,
    inlet_intensity=0.005,
    inlet_viscosity_ratio=5.0,
    scale_resolving=DDES(
        length_scale="cell_volume",
        shielding="automatic",
        low_dissipation=True,
    ),
)
```
