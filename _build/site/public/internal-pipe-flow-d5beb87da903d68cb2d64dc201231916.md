# Example: Internal Pipe Flow

This example demonstrates simulating turbulent flow through a pipe system with bends. You'll calculate pressure drop, visualize velocity profiles, and examine secondary flow patterns at bends.

## Objective

- Generate a mesh inside a pipe geometry with boundary layers
- Run a RANS simulation for turbulent pipe flow
- Calculate total pressure drop across the system
- Visualize velocity profiles and secondary flows at bends

## Step 1: Create a Meshing Project

1. **Dashboard** → **New Project** → **Meshing**
2. Name: "Pipe Flow Analysis"
3. Upload your pipe geometry (STEP preferred for clean face identification)

## Step 2: Geometry Check

Internal flow geometries need special attention:

- The geometry defines the **fluid volume** (the inside of the pipe)
- Inlet and outlet faces must be identifiable (flat faces at pipe ends)
- The pipe wall must be a closed, connected surface

If your CAD file is a solid pipe (not the fluid volume), you'll need to extract the internal volume in your CAD software before uploading.

## Step 3: Domain Configuration

In the **Setup** tab:

1. Select **Internal Flow** domain type
2. Studio detects the fluid volume inside the geometry
3. Inlet and outlet faces are identified automatically (or select them manually)

```{tip}
For straight pipes, add a development length of 10× pipe diameter upstream of any features of interest. This allows the flow to become fully developed before reaching the bend or restriction.
```

## Step 4: Surface Naming

| Surface | Name | Type |
|---------|------|------|
| Pipe entrance | `inlet` | Velocity inlet |
| Pipe exit | `outlet` | Pressure outlet |
| Pipe wall | `pipe_wall` | No-slip wall |

## Step 5: Mesh Settings

For a pipe with diameter D:

| Parameter | Value |
|-----------|-------|
| Target cell size | D / 20 |
| Min cell size | D / 100 |
| Refinement levels | 8 |
| Boundary layers | Enabled |
| Number of layers | 10 |
| First layer height | Based on y+ target |
| Growth rate | 1.2 |

### Sizing Example (50 mm diameter pipe)

| Parameter | Value |
|-----------|-------|
| Target cell size | 2.5 mm |
| Min cell size | 0.5 mm |
| BL first layer | 0.05 mm (y+ ≈ 30 at 5 m/s) |
| BL layers | 10 |

### Bend Refinement

Add a refinement zone around each pipe bend:

- **Shape:** Cylinder (aligned with bend axis)
- **Radius:** 1.5× pipe radius
- **Extends:** 2× diameter before and after the bend centerline
- **Cell size:** 2× finer than base mesh

## Step 6: Generate Mesh and Create CFD Project

1. Generate the mesh (expect 1–5 million cells for a medium pipe system)
2. Create a new **CFD project** using this mesh

## Step 7: Simulation Setup

| Setting | Value |
|---------|-------|
| Turbulence model | k-ω SST or k-ε |
| Inlet velocity | Bulk velocity (e.g., 5 m/s) |
| Outlet pressure | 0 Pa |
| Pipe wall | No-slip wall |
| Turbulence intensity | 5% (typical for pipe flow) |
| Turbulent viscosity ratio | 10 |
| Max iterations | 800 |

### Reynolds Number Check

Calculate the Reynolds number to confirm turbulent flow:

```
Re = (ρ × V × D) / μ
```

For water at 20°C (ρ = 998 kg/m³, μ = 0.001 Pa·s) in a 50 mm pipe at 5 m/s:

```
Re = (998 × 5 × 0.05) / 0.001 = 249,500 (fully turbulent)
```

Turbulent pipe flow requires Re > ~4,000.

## Step 8: Results Analysis

### Pressure Drop

1. Use the **Probe** tool to measure pressure at the inlet and outlet
2. Pressure drop = P_inlet - P_outlet
3. Compare with the Darcy-Weisbach equation for validation:

```
ΔP = f × (L/D) × (ρV²/2)
```

Where f is the friction factor from the Moody chart.

### Velocity Profiles

1. Add **slice planes** perpendicular to the pipe axis at locations of interest:
   - Upstream of bend (fully developed profile)
   - At the bend (distorted profile)
   - Downstream of bend (recovery)
2. Color by velocity magnitude

**What to look for:**
- Fully developed flow shows a symmetric profile (parabolic-like for turbulent flow)
- At bends, the maximum velocity shifts toward the outer wall
- Recovery length downstream is typically 10–20 diameters

### Secondary Flow at Bends

1. Add a **slice plane** at the bend cross-section, colored by through-plane velocity
2. Add **streamlines** to visualize Dean vortices (counter-rotating vortex pairs)
3. These secondary flows are driven by centrifugal effects at the bend

### Wall Shear Stress

1. Color the `pipe_wall` surface by velocity gradient
2. High shear regions appear at the outer wall of bends
3. Low shear regions (potential for separation) appear at the inner wall

## Validation Reference

For a smooth straight pipe at Re = 100,000:

| Quantity | Expected Value |
|----------|----------------|
| Friction factor (f) | ~0.018 (Moody chart) |
| Centerline velocity | ~1.23 × bulk velocity |
| Skin friction Cf | ~0.0045 |

```{admonition} Pipe Flow Tip
:class: tip
If your results show an asymmetric profile in a straight section, the mesh may be too coarse or the inlet development length too short. Increase the upstream straight section to at least 10D.
```
