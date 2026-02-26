# Boundary Conditions

Boundary conditions define the physical behavior at each surface of your mesh. Correct boundary conditions are critical for obtaining meaningful simulation results.

## Automatic Detection

Studio automatically assigns boundary conditions based on surface names:

| Surface Name Contains | Assigned Type | Default Values |
|----------------------|---------------|----------------|
| `inlet` | Velocity inlet | Must specify velocity |
| `outlet` | Pressure outlet | 0 Pa gauge |
| `wall`, `body`, `car`, `wing` | No-slip wall | Zero velocity at surface |
| `symmetry` | Symmetry | — |
| `ground` | Moving wall | Velocity matches freestream |
| `top`, `side`, `farfield` | Slip wall | — |

You can override any auto-detected condition in the Simulation tab.

## Inlet Conditions

### Velocity Inlet

The most common inlet type. Specify the flow velocity entering the domain.

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Velocity** | Flow speed magnitude and direction | 30 m/s in X-direction |
| **Turbulence intensity** | Incoming turbulence level as a percentage | 1–5% for external, 5–10% for internal |
| **Turbulent viscosity ratio** | Ratio of turbulent to molecular viscosity | 5–100 |

```{admonition} Turbulence Intensity Guide
:class: tip

| Application | Typical TI |
|------------|-----------|
| Wind tunnel (low turbulence) | 0.5 – 1% |
| External flow (atmospheric) | 1 – 5% |
| Internal flow (duct, pipe) | 5 – 10% |
| Highly turbulent environments | 10 – 20% |
```

The turbulence quantities (k, ω, ε) are automatically computed from the turbulence intensity and viscosity ratio — you don't need to calculate these manually.

## Outlet Conditions

### Pressure Outlet

Sets a fixed static pressure at the boundary. This is the standard outlet condition for most incompressible flow problems.

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| **Static pressure** | Gauge pressure at the outlet | 0 Pa |

```{note}
For incompressible flow (the default in Gradient Dynamics), absolute pressure doesn't matter — only pressure differences. Setting the outlet to 0 Pa gauge is standard practice.
```

## Wall Conditions

### No-Slip Wall

The default wall condition. Fluid velocity is zero at the surface (the fluid "sticks" to the wall).

**Use for:** Solid surfaces — car bodies, pipe walls, wing surfaces, buildings

### Moving Wall

A wall with a prescribed velocity. The fluid matches this velocity at the surface.

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Wall velocity** | Velocity vector of the wall surface | Ground moving at freestream speed |

**Use for:**
- **Ground plane** in vehicle aerodynamics — the ground moves at the same speed as the incoming airflow to simulate a car moving through still air
- **Rotating walls** — wheels, rotating cylinders

### Slip Wall

Zero shear stress at the surface — the fluid slides freely along the wall.

**Use for:** Far-field boundaries (top, sides of external domain), symmetry-like conditions where you don't want to enforce exact symmetry

## Symmetry

Mirrors the flow field across the boundary. No flow crosses the symmetry plane, and all gradients normal to the plane are zero.

**Use for:** Symmetric geometries where you mesh only half (or quarter) of the domain to reduce cell count and compute cost.

```{admonition} Symmetry Assumptions
:class: warning
Only use symmetry if your flow is truly symmetric. Bluff body flows, for example, may have asymmetric vortex shedding that a symmetry condition would suppress. For RANS, symmetry is generally safe for geometrically symmetric configurations.
```

## Boundary Condition Summary by Application

### External Vehicle Aerodynamics

| Surface | Type | Value |
|---------|------|-------|
| `inlet` | Velocity inlet | Freestream speed (e.g., 30 m/s) |
| `outlet` | Pressure outlet | 0 Pa |
| `car_body` | No-slip wall | — |
| `ground` | Moving wall | Freestream speed |
| `wheels` | Rotating wall | Angular velocity |
| `top`, `sides` | Slip wall | — |
| `symmetry` | Symmetry | — (if half-model) |

### Internal Pipe Flow

| Surface | Type | Value |
|---------|------|-------|
| `inlet` | Velocity inlet | Bulk velocity |
| `outlet` | Pressure outlet | 0 Pa |
| `pipe_wall` | No-slip wall | — |

### Wind Engineering

| Surface | Type | Value |
|---------|------|-------|
| `inlet` | Velocity inlet | Wind speed |
| `outlet` | Pressure outlet | 0 Pa |
| `building` | No-slip wall | — |
| `ground` | No-slip wall | — |
| `top`, `sides` | Slip wall | — |
