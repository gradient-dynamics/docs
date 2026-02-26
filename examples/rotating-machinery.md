# Example: Rotating Machinery (Fan / Pump)

This example demonstrates simulating a rotating fan or pump impeller using the Multiple Reference Frame (MRF) approach. MRF is a steady-state approximation that avoids the cost of a full transient simulation.

## Objective

- Generate a multi-region mesh with rotating and stationary zones
- Run an MRF simulation of a fan or pump
- Analyze performance (pressure rise, mass flow, efficiency)
- Visualize flow patterns through the rotor

## Background: MRF Approach

The **Multiple Reference Frame** method:

1. Divides the domain into a **rotating zone** (containing the impeller) and a **stationary zone** (inlet/outlet ducts)
2. Solves the flow equations in a rotating reference frame within the rotating zone (adding Coriolis and centrifugal source terms)
3. Uses a **frozen rotor interface** to couple the rotating and stationary zones

This gives a steady-state approximation of the time-averaged rotating flow. It's fast (single steady solve) but doesn't capture blade-passing transient effects.

```{note}
MRF is best for design-point analysis and comparative studies. For detailed transient analysis (noise, vibration, blade-to-blade interaction), use transient sliding mesh (available on Pro tier and above).
```

## Step 1: Create a Meshing Project

1. **Dashboard** → **New Project** → **Meshing**
2. Name: "Fan Simulation"
3. Upload your fan/pump geometry (STEP format)

## Step 2: Domain Configuration

1. Select **Rotating Machinery** domain type
2. Studio creates two zones:
   - **Rotating zone** — Cylindrical region around the impeller
   - **Stationary zone** — Surrounding duct/enclosure

### Rotating Zone Setup

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Rotation axis** | Direction of rotation | Z-axis: [0, 0, 1] |
| **Rotation origin** | Center of rotation | [0, 0, 0] |
| **RPM** | Rotational speed | 3000 RPM |
| **Zone shape** | Cylindrical region enclosing the rotor | Radius slightly larger than blade tips |

```{admonition} Zone Sizing
:class: tip
The rotating zone should:
- Fully enclose all rotating parts (blades, hub, shroud)
- Have a small gap (5–10% of blade span) between the blade tips and the zone boundary
- Extend axially to include the blade passages

Do **not** include stationary parts (duct walls, volute) in the rotating zone.
```

## Step 3: Multi-Region Setup

### Regions

| Region | Type | Description |
|--------|------|-------------|
| `rotor` | Rotating (MRF) | Contains the impeller blades |
| `inlet_duct` | Fluid (stationary) | Upstream duct or plenum |
| `outlet_duct` | Fluid (stationary) | Downstream duct or volute |

### Interfaces

| Interface | Between | Type |
|-----------|---------|------|
| `rotor_inlet` | rotor ↔ inlet_duct | Frozen rotor |
| `rotor_outlet` | rotor ↔ outlet_duct | Frozen rotor |

## Step 4: Surface Naming

| Surface | Name | Condition |
|---------|------|-----------|
| Duct entrance | `inlet` | Velocity inlet or total pressure |
| Duct exit | `outlet` | Pressure outlet |
| Blade surfaces | `blades` | No-slip wall (rotating) |
| Hub | `hub` | No-slip wall (rotating) |
| Shroud / duct wall | `shroud` | No-slip wall (stationary) |

## Step 5: Mesh Settings

| Parameter | Value |
|-----------|-------|
| Target cell size | Blade span / 20 |
| Min cell size | Blade span / 100 |
| Refinement levels | 10 |
| BL layers | 8 |
| BL first layer height | Target y+ ≈ 30 for RANS |
| BL growth rate | 1.2 |

### Refinement Zones

| Zone | Location | Purpose |
|------|----------|---------|
| Blade passage | Between blades | Resolve blade-to-blade flow |
| Leading edges | Blade leading edges | Capture flow around blade entry |
| Tip gap | Between blade tips and shroud | Resolve tip leakage flow |

## Step 6: Generate Mesh

Expect 5–20 million cells for a medium-resolution fan simulation. Check:
- Quality in the rotating zone (blade passages should have uniform, fine cells)
- Interface quality (cells should be similar size on both sides)
- Boundary layer quality on blade surfaces

## Step 7: Simulation Setup

| Setting | Value |
|---------|-------|
| Turbulence model | k-ω SST |
| Rotating zone RPM | 3000 RPM (match your design speed) |
| Inlet velocity | Based on operating point (e.g., 5 m/s) |
| Outlet pressure | 0 Pa (or set based on system curve) |
| Turbulence intensity | 3% |
| Max iterations | 1500 |
| Algorithm | SIMPLE |

## Step 8: Results Analysis

### Performance Metrics

1. **Total pressure rise** — Measure total pressure at inlet and outlet:
   ```
   ΔP_total = P_total_outlet - P_total_inlet
   ```
2. **Mass flow rate** — Integrate velocity across the inlet face
3. **Efficiency** — Compare actual pressure rise to ideal:
   ```
   η = (ΔP_total × Q) / (τ × ω)
   ```
   Where Q is volume flow rate, τ is torque on blades, ω is angular velocity

### Flow Through Blade Passages

1. Add a **slice plane** perpendicular to the rotation axis, at mid-blade height
2. Color by **velocity magnitude**
3. Look for:
   - Uniform flow through all passages (good)
   - Separation on blade suction side (may indicate stall)
   - High velocity near blade tips (tip effects)

### Meridional View

1. Add a **slice plane** through the rotation axis (meridional plane)
2. Color by **axial velocity** or **pressure**
3. Shows how the flow develops from inlet through the rotor to the outlet

### Blade Loading

1. Color blade surfaces by **pressure**
2. The **pressure side** (concave) should show higher pressure
3. The **suction side** (convex) should show lower pressure
4. The pressure difference drives the torque and pressure rise

### Tip Flow

1. Add a **slice plane** at the blade tip radius
2. Color by velocity
3. Check for tip leakage flow (flow from pressure to suction side through the tip gap)
4. This is a key source of loss in unshrouded impellers

## Design Point vs. Off-Design

To map a performance curve:

1. Run simulations at several flow rates (vary inlet velocity)
2. Record pressure rise and efficiency at each point
3. Plot ΔP vs. Q (fan curve) and η vs. Q (efficiency curve)
4. Identify the best efficiency point (BEP)

```{admonition} Off-Design Caution
:class: warning
MRF becomes less accurate far from the design point, especially in stalled or highly separated conditions. If you need off-design performance mapping with high accuracy, consider transient sliding mesh simulations.
```
