# Refinement Zones

Refinement zones allow you to increase mesh resolution in specific regions of the domain without refining the entire mesh. This is essential for capturing flow features like wakes, separation zones, and shear layers.

## Why Use Refinement Zones?

The base mesh resolution applies uniformly across the domain, but many flow features are localized:

- **Wake behind a vehicle** — Needs finer cells to resolve turbulent structures
- **Separation region** around a wing — Needs resolution to capture recirculation
- **Gap between components** — Needs fine cells to resolve flow through narrow passages
- **Jet or exhaust plume** — Needs fine cells along the jet path

Refinement zones concentrate AMR block refinement where it matters most, keeping the total cell count manageable.

## How Zones Work with Block AMR

Refinement zones specify a **target AMR level** within a defined region. All AMR blocks that fall within the zone are refined to at least this level, regardless of their proximity to a geometry surface. This integrates seamlessly with the block AMR hierarchy — there is no separate treatment for zone boundaries.

```{tip}
Zone refinement and surface refinement combine automatically. Blocks inside a zone near a geometry surface will be refined to the maximum of the zone level and the surface refinement level.
```

## Zone Shapes

### Box

A rectangular region defined by center position and dimensions (length × width × height).

**Best for:**
- Vehicle wakes (elongated box behind the car)
- Ground effect regions (flat box under the vehicle)
- Rectangular flow passages

### Cylinder

A cylindrical region defined by center, axis direction, radius, and length.

**Best for:**
- Rotating zones (fans, wheels, propellers)
- Jet flows and exhaust plumes
- Pipe sections requiring higher resolution

### Sphere

A spherical region defined by center and radius.

**Best for:**
- Point sources or sinks
- Localized regions of interest
- Probe locations where you want high resolution

## Adding Refinement Zones

1. In the **Setup** tab, click **Add Refinement Zone**
2. Select the zone shape (Box, Cylinder, or Sphere)
3. Position and size the zone using either:
   - **3D viewer** — Drag the zone handles to position and resize
   - **Numerical input** — Enter exact coordinates and dimensions in the panel
4. Set the **refinement level** — this sets the minimum AMR level within the zone

## Setting the Refinement Level

Each zone specifies a minimum AMR level for blocks within it. The level should be:

- **Higher** than the coarse background AMR level (otherwise the zone has no effect)
- **Proportional** to the feature size you want to capture
- **Not excessively higher** than the surrounding level — the AMR block hierarchy transitions smoothly between levels, but very large jumps increase cell count significantly

```{admonition} Sizing Guideline
:class: tip
Each AMR level doubles resolution in each dimension, so 2 extra levels = 4× finer cells. For wake capture, 1–2 additional AMR levels beyond the background is usually sufficient. For tight gaps or critical geometry features, 2–3 additional levels may be needed.
```

## Common Refinement Strategies

### Vehicle Aerodynamics

| Zone | Shape | Position | Additional AMR Levels |
|------|-------|----------|-----------------------|
| **Wake zone** | Box | Behind vehicle, 2–3× car length | +1–2 |
| **Underbody zone** | Box | Under vehicle, ground to floor | +1 |
| **Wheel zones** | Cylinder | Around each wheel | +2 |
| **Front zone** | Box | Ahead of vehicle, 0.5× length | +1 |

### Airfoil / Wing

| Zone | Shape | Position | Additional AMR Levels |
|------|-------|----------|-----------------------|
| **Leading edge** | Box | Extends upstream of LE | +2 |
| **Trailing edge** | Box | Behind TE, 1–2× chord | +2 |
| **Suction side** | Box | Above airfoil | +1 |

### Internal Flow

| Zone | Shape | Position | Additional AMR Levels |
|------|-------|----------|-----------------------|
| **Bend region** | Box/Cylinder | Around pipe bends | +1–2 |
| **Constriction** | Cylinder | At flow restrictions | +2 |
| **Mixing zone** | Box | Downstream of junctions | +1 |

## Managing Zones

- **Edit** — Click a zone in the feature tree or 3D viewer to modify its properties
- **Delete** — Remove zones you no longer need
- **Toggle visibility** — Show/hide zones in the 3D viewer for clarity

Multiple refinement zones can overlap. Where zones overlap, the **highest** AMR level (finest resolution) takes precedence.
