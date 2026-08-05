# FluxCore

FluxCore is Gradient Dynamics' GPU-native CFD and multiphysics solver. It is
designed around accelerator hardware from the foundation so that the complete
production workload—not just isolated kernels—can benefit from modern GPU
compute.

FluxCore is **not** a port, wrapper or GPU rewrite of a legacy SIMPLE or PIMPLE
codebase. It is a novel solver technology developed for scalable, managed cloud
execution and the mesh, physics and output workflows used by Studio.

## More than a demonstrator

FluxCore is built for production three-dimensional engineering cases. It
supports polyhedral volume meshes, viscous and turbulent flow, steady and
time-resolved workflows, rotating zones, complex boundary conditions,
engineering force and moment outputs, thermal transport and multi-region
conjugate heat transfer. It is not a basic explicit two-dimensional solver.

The difficult work is not merely advancing equations quickly. Production CFD
must also load and validate large meshes, preserve conservation on irregular
cells, represent wall-bounded turbulence, handle coupled regions, maintain
robust progress across difficult operating points, expose meaningful
convergence information and produce useful result files. FluxCore treats that
whole execution path as the product.

## GPU-native by design

Studio sends a validated simulation request to managed FluxCore capacity. The
platform prepares the mesh, selects suitable accelerator resources, executes
the run, streams progress, and finalises portable result and restart assets.
Large cases can use multiple GPUs without changing the engineering definition
of the case.

The GPU-native design extends into the linear-system work at the heart of an
industrial CFD calculation. Momentum, turbulence, energy and coupled-region
physics create large sparse systems repeatedly throughout a run. FluxCore's
sophisticated linear-system subsystem is designed for GPU execution as part of
the complete nonlinear simulation—not bolted onto a CPU-era solver as a
separate acceleration library. It manages precision, convergence, recovery and
distributed execution as one coordinated production workload.

This design provides three practical benefits:

- **Fast iteration:** design changes can move from setup to an inspectable
  result sooner.
- **Predictable workflow:** engineers do not manage drivers, message-passing
  libraries, solver builds or cluster queues.
- **Scale without a second toolchain:** the same Studio project model applies
  from evaluation cases to larger production meshes.

Performance depends on mesh topology, physics, requested outputs, convergence
behaviour and accelerator availability. Compare cases using the same mesh,
settings and acceptance criteria when evaluating speed.

## Physics capability

### Aerodynamics and internal flow

Use FluxCore for external aerodynamic loads, underbody and cooling flow,
ducting, pressure loss, mass flow, wakes, fans, pumps and other viscous-flow
applications. Farfield, inlet, outlet, wall, rotating-wall, symmetry and
periodic boundary types cover common engineering configurations.

### Turbulence and wall-bounded flow

RANS models provide the production starting point for turbulent engineering
flow. Time-resolved workflows extend that capability to unsteady wakes and load
histories. Model choice, wall treatment and prism-layer resolution remain a
single engineering decision.

### Rotating machinery

Named rotating cell zones and wall associations represent rotating components
without disconnecting them from the project mesh and output definitions.
Forces and moments can be requested on selected components with explicit axes,
centres and reference values.

### Thermal and conjugate heat transfer

FluxCore couples fluid convection with conduction through multiple solid
regions. The solver maintains the relationship between material zones,
fluid–solid interfaces, heat sources and thermal outputs. Typical uses include
electronics cooling, cold plates, heat sinks, battery modules and thermal
management passages.

### Time-resolved results

Time-resolved simulations can publish a series of accepted physical states at
a chosen cadence. Studio retains the shared topology and field snapshots needed
for animation, statistics and downstream analysis without making the engineer
manage a directory of unrelated files.

## Mesh and boundary support

FluxCore consumes production polyhedral meshes in CGNS and supported OpenFOAM
forms. Prism–octree meshes produced by Studio carry boundary patches, rotating
zones and material regions directly into the simulation setup. Imported meshes
are validated against the same public boundary and zone concepts.

The solver supports named boundary definitions rather than relying on patch
order. Periodic boundaries require an explicit pair and transformation.
Rotating walls use an axis, origin and angular speed. These definitions remain
visible in the Studio setup so they can be reviewed before compute is allocated.

## Engineering outputs

FluxCore can produce:

- volume and boundary field data,
- residual and engineering-monitor histories,
- named force, moment, drag and lift outputs,
- component-specific reference frames and moment centres,
- surface pressure and viscous contributions,
- heat-transfer and temperature quantities,
- transient field series and restart states,
- portable CGNS and VTK-family result assets.

Always define force reference area, velocity, density, directions and moment
lengths explicitly for reportable coefficients. Automatic projected areas are
useful for exploration but are not a universal engineering reference.

## Robustness without exposing internals

FluxCore automatically coordinates stable initialisation, nonlinear progress,
pressure–velocity consistency, distributed mesh communication, turbulence and
thermal coupling, convergence monitoring and result finalisation. These are
carefully engineered parts of the product, but the internal solver architecture
is intentionally not a public tuning surface.

Users control the quantities that determine the physical problem and the
evidence needed to judge it. Studio presents validated defaults, while the
Python API design exposes advanced policy objects for spatial accuracy,
nonlinear progression, linear-system convergence, transient sampling,
checkpointing and GPU selection. Neither surface exposes proprietary algorithm
selection or internal data structures.

See [Advanced solver controls](../api-reference/advanced-controls.md) for the
planned Python interface.

## How to judge a FluxCore run

1. Confirm the mesh, patch names, material regions and interfaces.
2. Check units, properties, operating conditions and reference values.
3. Review residual histories together with forces, flow rates or temperatures.
4. Inspect local fields for separation, recirculation, shocks, thermal plumes or
   other mechanisms relevant to the result.
5. Perform mesh and time-step sensitivity where the decision requires it.
6. Compare against an applicable validation study or trusted reference.

See the [validation knowledge base](../knowledge-base/validation-studies.md) for
published evidence across aerodynamic, internal-flow and thermal cases.
