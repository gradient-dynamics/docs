# Mesh Quality

After mesh generation, the **Mesh Quality** tab displays comprehensive quality metrics. Good mesh quality is essential for solver stability and accurate results.

## Quality Metrics

### Skewness

Measures how much a cell deviates from its ideal shape (e.g., a perfect hexahedron or tetrahedron).

| Range | Rating | Impact |
|-------|--------|--------|
| 0.0 – 0.25 | Excellent | Ideal for all solvers |
| 0.25 – 0.50 | Good | No issues expected |
| 0.50 – 0.85 | Acceptable | May slow convergence slightly |
| 0.85 – 1.0 | Poor | Can cause convergence failure |

```{admonition} Target
:class: tip
Maximum skewness should be below **0.85** throughout the mesh. Cartesian cells in the block AMR hierarchy have zero skewness by construction — poor skewness values only appear at cut-cells adjacent to geometry surfaces.
```

### Non-Orthogonality

The angle between the face normal vector and the vector connecting adjacent cell centers. Lower is better.

| Range | Rating | Impact |
|-------|--------|--------|
| 0° – 45° | Excellent | Fast convergence |
| 45° – 70° | Good | Standard for most solvers |
| 70° – 85° | Acceptable | May need non-orthogonal correctors |
| > 85° | Poor | Solver instability likely |

### Aspect Ratio

The ratio of the longest cell dimension to the shortest.

- **Volume cells:** Should be below 10 for the bulk mesh
- **Near-wall cut-cells:** High aspect ratios are expected and acceptable in cells with aggressive near-wall AMR refinement — this is by design

### Cell Volume

All cells must have positive volume. Negative or zero-volume cells indicate a mesh error and must be resolved before simulation.

## Quality Report

The Mesh Quality tab shows:

1. **Summary statistics** — Total cell count, min/max/mean of each metric
2. **Histograms** — Distribution of cells across quality ranges for each metric
3. **Threshold indicators** — Visual markers showing what percentage of cells fall in each quality category

## Interpreting Results

### Healthy Mesh
- > 95% of cells rated "Excellent" or "Good"
- Maximum skewness < 0.85
- Maximum non-orthogonality < 70°
- No negative volumes

### Marginal Mesh
- 80–95% of cells rated "Excellent" or "Good"
- A small number of poor-quality cells (< 1%)
- May need non-orthogonal correctors enabled in solver settings

### Poor Mesh
- Many cells with high skewness or non-orthogonality
- Likely to cause solver divergence
- Consider adjusting mesh settings and regenerating

## Improving Mesh Quality

If quality is not satisfactory:

| Issue | Solution |
|-------|----------|
| High skewness near geometry | Increase surface refinement AMR level |
| High non-orthogonality at transitions | Increase AMR levels for smoother size transitions between blocks |
| Very small cut-cell volume fraction | Geometry has tiny slivers — simplify or repair the surface |
| Negative volumes | Check geometry for self-intersections and repair |
| Poor quality in narrow gaps | Increase gap refinement AMR level or simplify geometry |

## Quality vs. Cell Count Trade-off

Higher quality generally requires more cells:

- **More AMR levels** → Smoother transitions → Better quality
- **Smaller base cell size** → More uniform sizing → Better quality
- **Higher surface refinement** → Better cut-cell quality near geometry

Balance quality against your cell count budget and available compute credits.

```{tip}
The AI Assistant can interpret your quality report and suggest specific improvements. Ask: *"How can I improve the mesh quality?"*
```
