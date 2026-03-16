# Conformal vs Non-Conformal Meshes

Understanding the difference between conformal and non-conformal mesh connectivity is important for multi-region setups, rotating machinery, and getting the most out of the solver. This page explains what each means, how the solver detects and handles them, and when each is appropriate.

## What Is a Conformal Mesh?

A **conformal mesh** has exactly one shared face between every pair of adjacent cells. All cell faces line up perfectly across region boundaries — each face on one side has a matching face on the other side with 1:1 correspondence.

```
Conformal interface:

  Region A  |  Region B
  __________|__________
  |    |    ||    |    |
  |    |    ||    |    |
  |____|____||____|____|
              ↑
         Faces match 1:1
```

**Properties:**
- Faces on both sides of a boundary are identical in size and position
- No interpolation needed at the interface — values transfer directly
- Most numerically accurate at interfaces
- Easier to achieve on simple geometries with matched CAD faces

## What Is a Non-Conformal Mesh?

A **non-conformal mesh** has mismatched faces across a boundary. One cell may share parts of its face with multiple cells on the other side — this is common with block AMR meshes at refinement level boundaries, hanging nodes, and size transitions.

```
Non-conformal interface:

  Region A (coarse)  |  Region B (fine)
  ___________________|_________________
  |                  ||    |    |    |
  |                  ||    |    |    |
  |__________________||____|____|____|
                       ↑
         One large face ↔ multiple small faces
         Requires interpolation
```

**Properties:**
- Cells of different sizes meet at a boundary — one large face corresponds to multiple small faces
- Values are interpolated across mismatched faces (area-weighted averaging)
- Slightly less accurate at the interface than conformal
- Essential for block AMR meshes and multi-region setups with different cell sizes

## How the Solver Detects Mesh Type

When a simulation is submitted, the solver automatically analyses the mesh connectivity and classifies it:

**Detection logic:**
- Counts the number of unique cell-pair connections vs. the total number of internal faces
- If more than ~1% of faces share a cell pair that already has another face (duplicate pairs), the mesh is classified as **non-conformal / polyhedral**
- Otherwise it is classified as **conformal**

This detection is entirely automatic — you don't need to specify the mesh type manually. The solver uses this classification to choose the appropriate numerical treatment.

```{admonition} What you'll see in the logs
:class: note
After the solver initialises, the logs will report either:

`Polyhedral mesh mode ENABLED` — non-conformal mode active

If no such message appears, the solver is running in standard conformal mode.
```

## Solver Modes

| Mode | When Active | Treatment |
|------|------------|-----------|
| **Conformal (auto)** | Mesh detected as conformal (duplicate_ratio ≈ 0) | Standard finite volume — direct face flux computation, no interpolation overhead |
| **Non-conformal / Polyhedral (auto)** | Mesh detected as non-conformal | Cell-pair aggregation — multiple faces between the same cell pair are grouped and fluxes are summed |
| **Conformal (forced)** | `mesh_mode: conformal` in settings | Forces conformal path regardless of mesh |
| **Polyhedral (forced)** | `mesh_mode: polyhedral` in settings | Forces polyhedral path regardless of mesh |

For most users, **auto mode is correct** and no manual override is needed.

## Which Meshes Are Conformal?

| Mesh Type | Typical Classification | Notes |
|-----------|----------------------|-------|
| Cartesian cut-cell block AMR (single region) | **Conformal** | Standard Gradient Dynamics mesh with no multi-region boundaries |
| Block AMR with matched multi-region interfaces | **Conformal** | Regions share exact face geometry at their boundary |
| Block AMR with refinement level transitions | **Non-conformal** | Different AMR levels create hanging nodes at block boundaries |
| Multi-region with different cell sizes | **Non-conformal** | Mismatched faces at the region interface |
| Rotating MRF zone | **Non-conformal** | Rotating/stationary interface cannot be conformal |
| Sliding mesh (transient rotating) | **Non-conformal** | Interface slides — faces never align exactly |

## Multi-Region Interfaces

When you set up a multi-region mesh (CHT, rotating machinery, porous zones), the interface between regions can be either conformal or non-conformal depending on how the geometry is set up and how the mesh sizes compare.

### Conformal Interface

Achieved when:
- The two regions share an exactly matching face topology (imported as touching bodies in a single STEP file)
- Both regions use the same or very similar cell sizes at the interface
- The **Conformal** option is selected in the Interface settings

**Advantages:**
- Most accurate thermal or flow coupling
- No interpolation error at the interface
- Better convergence for CHT problems

### Non-Conformal Interface

Occurs when:
- The two regions have significantly different cell sizes (e.g., coarse solid + fine fluid)
- Geometry was imported as separate files with slight positional mismatches
- Different mesh topologies on each side

**Advantages:**
- More flexible — doesn't require matched geometry
- Allows very different resolutions on each side
- Necessary for rotating zones (MRF, sliding mesh)

```{admonition} CHT recommendation
:class: tip
For conjugate heat transfer, use **conformal interfaces** where possible. Import your geometry as a single multi-body STEP file with touching faces, and set both regions to similar cell sizes at the wall. This gives the most accurate heat flux prediction at the fluid-solid boundary.
```

## Impact on Solver Accuracy and Stability

### Conformal meshes

- Full second-order accuracy at interfaces
- No additional interpolation error
- Fastest solver — no cell-pair aggregation overhead
- Preferred for production CHT and internal flow

### Non-conformal meshes

- Small interpolation error at non-conformal faces (proportional to the size mismatch)
- The solver uses area-weighted averaging to transfer fluxes across mismatched faces
- Slightly more expensive per iteration
- Works well when size mismatch is moderate (< 4:1)

```{admonition} Mesh quality and stability
:class: warning
Solver instability in multi-region cases is more often caused by **poor mesh quality near the interface** (large cell size jumps, sliver cells at the boundary) than by the conformal/non-conformal classification itself. If you see residuals oscillating or pressure clipping in the logs, check the mesh quality report at the interface region before changing the mesh mode.

Key things to check:
- Cell size ratio across the interface — aim for < 4:1
- Skewness near the interface — target < 0.85
- Non-orthogonality at interface faces — target < 70°
```

## Scenarios at a Glance

| Scenario | Recommended Setup | Conformal? |
|----------|------------------|------------|
| Single-region external aero | Default Cartesian block AMR mesh | Conformal |
| Internal pipe flow | Default Cartesian block AMR mesh | Conformal |
| CHT heat sink (same cell size at wall) | Multi-body STEP, matched sizing | Conformal |
| CHT heat sink (different region sizes) | Multi-body STEP, auto interface | Non-conformal |
| Fan / pump (steady MRF) | Rotating zone + frozen rotor interface | Non-conformal |
| Fan / pump (transient sliding mesh) | Sliding mesh interface | Non-conformal |
| Porous media zone | Auto-detected at zone boundary | Non-conformal |
| Periodic sector model | Periodic interface | Non-conformal |
