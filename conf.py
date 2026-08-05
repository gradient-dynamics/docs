from __future__ import annotations

project = "Gradient Dynamics"
author = "Gradient Dynamics"
copyright = "2026, Gradient Dynamics Ltd."
release = "2026.08"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "README.md",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
]
myst_heading_anchors = 3

html_theme = "furo"
html_title = "Gradient Dynamics Documentation"
html_logo = "_static/logo/GD_WordMark_PNG-06.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_show_sphinx = False

html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_buttons": [],
    "light_css_variables": {
        "color-brand-primary": "#1f5f99",
        "color-brand-content": "#256fb2",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f6f8fb",
        "color-foreground-primary": "#172033",
        "color-foreground-secondary": "#34445a",
        "color-foreground-muted": "#68778a",
        "color-border-primary": "#dbe3ec",
        "color-border-secondary": "#edf1f5",
        "color-sidebar-background": "#0d1117",
        "color-sidebar-background-border": "#30363d",
        "color-sidebar-brand-text": "#e6edf3",
        "color-sidebar-caption-text": "#8fc4ff",
        "color-sidebar-link-text": "#c9d1d9",
        "color-sidebar-item-background--current": "rgba(83, 155, 245, 0.16)",
        "color-sidebar-item-expander-background": "rgba(83, 155, 245, 0.10)",
        "color-code-background": "#f4f7fa",
        "color-code-foreground": "#172033",
        "color-admonition-background": "#f6f9fc",
        "color-card-background": "#ffffff",
        "color-card-border": "#dbe3ec",
        "font-stack": "Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "font-stack--headings": "'Space Grotesk', Inter, ui-sans-serif, system-ui, sans-serif",
        "font-stack--monospace": "'SFMono-Regular', Consolas, 'Liberation Mono', monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#8fc4ff",
        "color-brand-content": "#8fc4ff",
        "color-background-primary": "#0d1117",
        "color-background-secondary": "#161b22",
        "color-foreground-primary": "#e6edf3",
        "color-foreground-secondary": "#c9d1d9",
        "color-foreground-muted": "#8b949e",
        "color-border-primary": "#30363d",
        "color-border-secondary": "#21262d",
        "color-sidebar-background": "#0d1117",
        "color-sidebar-background-border": "#30363d",
        "color-sidebar-brand-text": "#e6edf3",
        "color-sidebar-caption-text": "#8fc4ff",
        "color-sidebar-link-text": "#c9d1d9",
        "color-sidebar-item-background--current": "rgba(83, 155, 245, 0.16)",
        "color-sidebar-item-expander-background": "rgba(83, 155, 245, 0.10)",
        "color-code-background": "#161b22",
        "color-code-foreground": "#e6edf3",
        "color-admonition-background": "#161b22",
        "color-card-background": "#10161d",
        "color-card-border": "#30363d",
    },
}

pygments_style = "sphinx"
pygments_dark_style = "github-dark"
