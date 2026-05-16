# Conformal vs Non-Conformal Meshes

Conformal and non-conformal describe how cells connect across region interfaces. This matters for multi-region simulations, conjugate heat transfer, rotating machinery, and imported meshes.

## Conformal Meshes

A **conformal mesh** has matching faces across an interface. Cells on one side line up with cells on the other side.

**Use when:**

- You need the most direct region-to-region transfer.
- Fluid and solid regions share clean, matching CAD interfaces.
- A verification or validation workflow requires matched interfaces.

**Benefits:**

- Strong interface accuracy.
- Straightforward quality checks.
- Often preferred for final conjugate heat transfer studies when the geometry supports it.

## Non-Conformal Meshes

A **non-conformal mesh** has mismatched faces across an interface. This is common when two regions use different local resolutions, when imported meshes do not align exactly, or when rotating and stationary regions meet.

**Use when:**

- Different regions need different mesh sizes.
- Geometry is complex or imported from separate sources.
- Rotating machinery or sliding interfaces are part of the workflow.
- The case requires unstructured or mixed-topology flexibility.

**Trade-offs:**

- More flexible setup.
- More care needed around interface quality.
- Interface size jumps should be kept moderate.

## Studio Behaviour

Studio detects the interface type during setup and prepares the appropriate simulation settings. For most users, automatic handling is recommended. Manual overrides should be used only when you have a specific validation requirement or have been advised by support.

## Multi-Region Guidance

For conjugate heat transfer and other coupled cases:

- Use a single clean CAD assembly where possible.
- Keep cell sizes similar across important interfaces.
- Avoid tiny gaps, overlaps, and sliver regions at shared faces.
- Review interface quality before running the simulation.
- Keep the same interface strategy across design comparisons.

```{admonition} CHT recommendation
:class: tip
For final heat-transfer studies, use conformal interfaces where practical and verify that temperature and heat-flux monitors are stable.
```

## Scenarios at a Glance

| Scenario | Typical Setup | Interface Type |
|----------|---------------|----------------|
| Single-region external aerodynamics | One fluid region | Conformal |
| Internal pipe flow | One connected fluid region | Conformal |
| CHT with matched fluid-solid faces | Multi-body CAD with aligned interfaces | Conformal |
| CHT with different region sizes | Region-specific mesh sizes | Non-conformal |
| Fan or pump steady analysis | Rotating and stationary zones | Non-conformal |
| Imported mesh workflow | Depends on imported connectivity | Conformal or non-conformal |
