# The simulation workflow

A reliable simulation is a chain of decisions. Studio keeps those decisions in
one project so each result can be traced back to its inputs.

## 1. Frame the engineering question

Start with the quantity you need to decide: drag, pressure loss, mass flow,
temperature, heat-transfer coefficient, force, moment, or a qualitative flow
feature. Define an acceptance tolerance before choosing a mesh size or run
budget.

## 2. Prepare geometry

Remove detail that cannot affect the target quantity, preserve the features
that control flow or heat transfer, check scale and orientation, and create
stable names for all boundaries that need physics or outputs.

## 3. Define the domain and regions

Create an external, internal or multi-region domain. Identify fluid volumes,
solid materials, rotating regions, symmetry planes, inlets, outlets, walls and
interfaces.

## 4. Build the mesh

Choose a target resolution, refine areas with strong gradients, and resolve
near-wall flow with prism layers where required. Review cell count and quality
before spending compute on a simulation.

## 5. Configure physics

Select steady or time-resolved flow, material properties, turbulence treatment,
thermal coupling, rotating zones, boundary conditions and engineering outputs.

## 6. Run and monitor

Watch the job stage, residual trends and physical monitors. A run is not
converged merely because it reached its iteration limit.

## 7. Post-process and compare

Inspect the fields that explain the integral result. Compare revisions using
consistent reference values, colour ranges, cuts and output definitions.

## 8. Establish confidence

Check conservation and physical plausibility, perform a mesh or time-step
sensitivity study where necessary, and compare against trusted data. Record the
accepted configuration in the project.
