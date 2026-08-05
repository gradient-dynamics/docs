# Results, convergence and validation

Simulation confidence comes from several independent checks. No single
residual, contour or comparison is sufficient on its own.

## Convergence

Review residuals alongside physical monitors such as force, pressure loss,
mass flow, heat rate or maximum temperature. A useful steady result normally
shows both numerical contraction and stable engineering outputs. Periodic or
chaotic monitor behaviour can indicate genuinely unsteady physics rather than
a failed run.

## Conservation and consistency

Check mass flow through inlets and outlets, energy balance for thermal cases,
force reference values, units, coordinate systems and sign conventions. Verify
that selected surfaces match the intended component.

## Verification and validation

- **Verification** asks whether the numerical problem is being solved
  consistently. Mesh and time-step sensitivity are central checks.
- **Validation** asks whether the model agrees with physical evidence for the
  intended use. Experiments, trusted benchmarks and established reference
  solutions provide that evidence.

Validation is specific to a regime. Agreement for an attached airfoil does not
automatically establish accuracy for separated automotive flow or conjugate
heat transfer.

## Communicating a result

Record the geometry revision, mesh settings and quality, physics and materials,
boundary conditions, run budget, convergence evidence, output definitions,
reference data and remaining uncertainty. Link the result to the project so a
colleague can reproduce the decision path.

Browse the [validation studies](../knowledge-base/validation-studies.md) for
worked examples of this evidence chain.
