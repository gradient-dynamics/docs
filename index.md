---
html_theme.sidebar_secondary.remove: true
---

# Gradient Dynamics

<div class="gd-hero">
  <div class="gd-hero__eyebrow">GPU-native engineering simulation</div>
  <h2>From geometry to engineering insight, in one browser workspace.</h2>
  <p>Gradient Dynamics Studio brings preprocessing, prism–octree meshing, FluxCore simulation and interactive post-processing together for engineering teams.</p>
  <div class="gd-hero__actions">
    <a class="gd-button gd-button--primary" href="getting-started/quick-start.html">Start your first project</a>
    <a class="gd-button gd-button--secondary" href="studio/fluxcore.html">Explore FluxCore</a>
  </div>
</div>

<div class="gd-stat-rail">
  <div><strong>Browser based</strong><span>No local solver stack to maintain</span></div>
  <div><strong>GPU native</strong><span>FluxCore is designed for accelerator hardware</span></div>
  <div><strong>Team ready</strong><span>Projects, members, storage and usage in one workspace</span></div>
</div>

## Build, run and understand

::::{grid} 1 2 3 3
:gutter: 3

:::{grid-item-card} Prepare and mesh
:link: studio/preprocessing
:link-type: doc

Import geometry, define engineering regions and build production meshes with boundary-layer control.
:::

:::{grid-item-card} Simulate with FluxCore
:link: studio/fluxcore
:link-type: doc

Run fast, production-scale fluid and thermal workflows on GPU-native compute.
:::

:::{grid-item-card} Validate decisions
:link: knowledge-base/validation-studies
:link-type: doc

Review transparent validation studies, comparison data and practical guidance.
:::

::::

```{toctree}
:maxdepth: 2
:hidden:

Getting Started <getting-started/index>
User Guide <user-guide/index>
Studio <studio/index>
API Reference <api-reference/index>
Release Notes <release-notes/index>
Knowledge Base <knowledge-base/index>
```
