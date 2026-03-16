# Example: Aircraft Wing Analysis

This example demonstrates an external aerodynamics analysis of an aircraft wing section — computing lift and drag, visualizing the pressure coefficient distribution, and examining flow patterns.

## Objective

- Generate a mesh around a wing geometry
- Run a RANS simulation at a given angle of attack
- Compute lift and drag coefficients (Cl, Cd)
- Visualize pressure coefficient (Cp) distribution on the wing surface
- Examine tip vortex structure (for 3D wings)

## Step 1: Create a Meshing Project

1. **Dashboard** → **New Project** → **Meshing**
2. Name: "Wing Analysis"
3. Upload your wing geometry (STEP recommended)

## Step 2: Domain Configuration

In the **Setup** tab:

1. Select **External Flow** domain type
2. Choose **Box** domain shape (or **C-Domain** for 2D-like airfoil sections)
3. Configure domain dimensions:

| Parameter | Value | Reasoning |
|-----------|-------|-----------|
| Upstream | 5× chord length | Adequate approach distance |
| Downstream | 10× chord length | Capture the full wake |
| Span direction | 3× semi-span (or periodic for infinite wing) | Avoid tip effects on boundaries |
| Above/Below | 5× chord length | Prevent blockage |

For a **half-wing with symmetry:**
- Enable **symmetry plane** at the wing root
- This halves the domain and cell count

## Step 3: Refinement Zones

### Leading Edge Zone
- **Shape:** Box
- **Position:** Enclosing the leading edge, extending 0.1× chord upstream
- **Cell size:** 4× finer than base mesh
- **Purpose:** Capture the stagnation point and leading edge suction peak

### Trailing Edge / Wake Zone
- **Shape:** Box
- **Position:** Behind the trailing edge, extending 2× chord downstream
- **Cell size:** 3× finer than base mesh
- **Purpose:** Resolve the wake and any trailing edge separation

### Tip Region (3D wings)
- **Shape:** Cylinder
- **Position:** Around the wing tip
- **Cell size:** 3× finer than base mesh
- **Purpose:** Capture the tip vortex structure

## Step 4: Surface Naming

| Surface | Name |
|---------|------|
| Wing upper surface | `wing_upper` or `wing` |
| Wing lower surface | `wing_lower` or `wing` |
| Far-field boundaries | `inlet`, `outlet`, `farfield` |
| Symmetry plane | `symmetry` |

## Step 5: Mesh Settings

| Parameter | Value (for ~1 m chord) |
|-----------|------------------------|
| Target cell size | 0.05 m |
| Min cell size | 0.002 m |
| Refinement levels | 10 |
| Boundary layers | Enabled |
| Number of layers | 12 |
| First layer height | 0.00005 m (y+ ≈ 1 for resolved BL) |
| Growth rate | 1.15 |

```{tip}
For wing analysis, a resolved boundary layer (y+ ≈ 1) provides more accurate lift and drag predictions than wall functions (y+ ≈ 30). Use more boundary layers (12–15) with a smaller first layer height.
```

## Step 6: Generate Mesh and Create CFD Project

1. Generate the mesh (expect 5–20 million cells for a medium-resolution wing)
2. Create a new **CFD project** using this mesh

## Step 7: Simulation Setup

| Setting | Value |
|---------|-------|
| Turbulence model | k-ω SST |
| Inlet velocity | Set to achieve desired Reynolds number. For Re = 6M at 1 m chord: ~88 m/s |
| Angle of attack | Set via velocity direction components (e.g., Ux = V cos(α), Uz = V sin(α)) |
| Outlet | Pressure outlet, 0 Pa |
| Wing surface | No-slip wall |
| Far-field | Slip wall |
| Symmetry | Symmetry condition |
| Turbulence intensity | 0.1% (clean wind tunnel) |
| Max iterations | 1500 |

### Setting Angle of Attack

To simulate at α = 5° with freestream velocity V = 88 m/s:

- **Ux** = 88 × cos(5°) = 87.66 m/s
- **Uz** = 88 × sin(5°) = 7.67 m/s

Set these as the inlet velocity components.

## Step 8: Results Analysis

### Lift and Drag Coefficients

1. **Forces** tool → Select wing surface
2. Reference values:
   - Reference velocity: Freestream speed
   - Reference area: Wing planform area (chord × span)
3. Read Cl and Cd

| Validation | NACA 0012 at Re=6M, α=5° |
|-----------|---------------------------|
| Expected Cl | ~0.55 |
| Expected Cd | ~0.008 |

### Pressure Coefficient Distribution

1. Color the wing surface by **Pressure**
2. Look for:
   - **Suction peak** near the leading edge on the upper surface (low Cp)
   - **Pressure recovery** toward the trailing edge
   - **Stagnation point** on the lower surface near the leading edge (Cp ≈ 1)

### Flow Visualization

- **Slice plane** at mid-span, colored by velocity → Shows the flow acceleration over the upper surface and the wake
- **Streamlines** seeded upstream → Shows how flow divides at the stagnation point and flows over/under the wing
- **Isosurface** of low pressure near the wing tip → Reveals the tip vortex core

### Span-wise Analysis

For a 3D wing, use **line probes** at different span stations to compare:
- Cp distribution at root, mid-span, and tip
- How the lift distribution varies along the span
- Where stall initiates (typically from the tip inward)

## Angle of Attack Sweep

To generate a lift curve (Cl vs. α):

1. Run simulations at several angles (e.g., 0°, 2°, 5°, 8°, 10°, 12°)
2. Record Cl and Cd from each run
3. Plot Cl vs. α — the slope should be approximately 2π per radian in the linear region
4. Identify the stall angle where Cl drops sharply

```{admonition} Stall Prediction
:class: note
RANS models (especially k-ω SST) predict stall onset reasonably well but tend to over-predict the maximum Cl. For accurate post-stall behavior, consider LES or DES (available on Pro tier and above).
```
