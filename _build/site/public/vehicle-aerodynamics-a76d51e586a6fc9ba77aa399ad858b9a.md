# Example: Vehicle Aerodynamics

This example demonstrates a complete external aerodynamics workflow — meshing and simulating airflow around a car to calculate drag and lift coefficients and visualize the flow field.

## Objective

- Generate a mesh around a car geometry with boundary layers
- Run a RANS simulation at highway speed (30 m/s / ~110 km/h)
- Calculate drag coefficient (Cd) and lift coefficient (Cl)
- Visualize pressure distribution, wake structure, and streamlines

## Step 1: Create a Meshing Project

1. **Dashboard** → **New Project** → **Meshing**
2. Name: "Car Aerodynamics"
3. Upload your car geometry file (STEP format recommended)

## Step 2: Geometry Check

Navigate to the **Geometry** tab and run analysis:

- Verify the geometry is **watertight** (no gaps)
- Check for **manifold** issues
- If using STL, run **vertex welding** to clean up any gaps

```{tip}
If your car model has open wheel arches or an open underbody, the mesher will struggle. Ensure the geometry is a closed, solid body. The AI Assistant can help identify and fix issues.
```

## Step 3: Domain Configuration

In the **Setup** tab:

1. Select **External Flow** domain type
2. Enable **Ground Plane** — the car should sit on a flat surface
3. Configure the wind tunnel dimensions:

| Parameter | Value | Reasoning |
|-----------|-------|-----------|
| Upstream | 1.5× car length | Allow flow to develop before reaching the car |
| Downstream | 3.0× car length | Capture the full wake structure |
| Sides | 1.5× car width | Avoid blockage effects |
| Top | 2.0× car height | Allow flow over the roof to develop |
| Bottom | 0 (ground plane) | Car sits on the ground |

## Step 4: Refinement Zones

Add refinement zones to capture key flow features:

### Wake Zone
- **Shape:** Box
- **Position:** Behind the car, extending 2× car length downstream
- **Width:** 1.5× car width
- **Height:** 1.5× car height
- **Cell size:** 2× finer than base mesh

### Underbody Zone
- **Shape:** Box (flat)
- **Position:** Under the car, from bumper to bumper
- **Height:** Ground to car floor + 0.1 m
- **Cell size:** 2× finer than base mesh

### Wheel Zones (if applicable)
- **Shape:** Cylinder
- **Position:** Around each wheel
- **Radius:** 1.5× wheel radius
- **Cell size:** 3× finer than base mesh

## Step 5: Surface Naming

In the **Surfaces** tab, name key boundaries:

| Surface | Name | Type |
|---------|------|------|
| Car body | `car_body` | Wall |
| Front wheels | `wheel_front` | Wall (or rotating wall) |
| Rear wheels | `wheel_rear` | Wall (or rotating wall) |
| Wind tunnel inlet | `inlet` | Inlet |
| Wind tunnel outlet | `outlet` | Outlet |
| Ground | `ground` | Moving wall |
| Top | `top` | Slip wall |
| Sides | `side_left`, `side_right` | Slip wall |

## Step 6: Mesh Settings

| Parameter | Value |
|-----------|-------|
| Target cell size | 0.1 m (for a ~4.5 m car) |
| Min cell size | 0.005 m |
| Refinement levels | 8 |
| Boundary layers | Enabled |
| Number of layers | 10 |
| First layer height | 0.001 m (y+ ≈ 30) |
| Growth rate | 1.2 |

## Step 7: Generate Mesh

Click **Generate Mesh** and wait for completion. Typical cell counts:

| Resolution | Approximate Cells |
|-----------|-------------------|
| Coarse | 2 – 5 million |
| Medium | 5 – 15 million |
| Fine | 15 – 50 million |

Check mesh quality in the **Mesh Quality** tab. Target:
- Skewness < 0.85
- Non-orthogonality < 70°

## Step 8: Create a CFD Project

1. Return to **Dashboard** → **New Project** → **CFD**
2. Name: "Car CFD"
3. Select the mesh from your meshing project

## Step 9: Simulation Setup

In the **Simulation** tab:

| Setting | Value |
|---------|-------|
| Turbulence model | k-ω SST |
| Inlet velocity | 30 m/s (X-direction) |
| Outlet pressure | 0 Pa |
| Car body | No-slip wall |
| Ground | Moving wall (30 m/s in X) |
| Top, sides | Slip wall |
| Turbulence intensity | 1% |
| Max iterations | 1000 |

```{admonition} Ground Boundary Condition
:class: important
For vehicle aerodynamics, the **ground must be a moving wall** at the same speed as the freestream. This simulates the car moving through still air, rather than air blowing over a stationary car on a stationary floor (which would create an unrealistic ground boundary layer).
```

## Step 10: Run and Monitor

1. Click **Run Simulation** and confirm
2. Monitor the **residual plot** — look for all residuals dropping below 1e-4
3. Check the **logs** for any warnings

A typical vehicle RANS simulation converges in 300–800 iterations.

## Step 11: Results Analysis

### Drag and Lift Coefficients

1. In the **Results** tab, click **Forces**
2. Select the `car_body` surface
3. Set reference values:
   - Reference velocity: 30 m/s
   - Reference area: Frontal area of the car (approximately width × height, e.g., 2.2 m²)
4. Read off Cd and Cl

| Vehicle Type | Expected Cd Range |
|-------------|------------------|
| Sedan | 0.25 – 0.35 |
| SUV | 0.35 – 0.45 |
| Sports car | 0.28 – 0.35 |
| Truck / Box shape | 0.6 – 0.8 |

### Pressure Distribution

1. Select **Pressure** field
2. Enable surface coloring on `car_body`
3. Look for:
   - **High pressure** (red) at the front stagnation point
   - **Low pressure** (blue) on the roof and sides where flow accelerates
   - **Pressure recovery** toward the rear

### Wake Visualization

1. Add a **slice plane** at Y = 0 (centerline) colored by velocity magnitude
2. The wake behind the car appears as a low-velocity region
3. Add **streamlines** seeded from the inlet to see flow paths around the car

### Underbody Flow

1. Add a horizontal **slice plane** at the underbody height
2. Color by velocity to see flow acceleration under the car
3. This reveals ground effect patterns

## Using the AI Assistant

You can set up this entire example through conversation:

> **You:** "I've uploaded a sedan CAD file. Set up an external aero mesh for highway speed analysis."
>
> **Assistant:** *Analyzes geometry dimensions, suggests domain box, recommends mesh settings, boundary layers, and refinement zones. Presents configuration for your approval.*
>
> **You:** "Run a simulation at 30 m/s with k-omega SST"
>
> **Assistant:** *Configures boundary conditions, sets inlet velocity, applies moving ground, and runs the simulation with your confirmation.*
>
> **You:** "What's the drag coefficient?"
>
> **Assistant:** *Calculates forces on the car body surface and reports Cd and Cl.*
