# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = "test-tools"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.prefecttask",
    "sphinxcontrib.prefectviz",
    "sphinx_copybutton",  # adds a copy button to code snippets
    "sphinx_inline_tabs",  # adds a ``tab`` directive to build tabbed content
    "myst_nb",  # adds support for (myst) markdown, python notebooks and myst-flavoured jupytext files
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for Extensions -------------------------------------------------

# [sphinx_copybutton]

# Strip most common input-prompt symbols from code before copying it
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# [myst_nb]

# The logic for executing notebooks. Here we cache outputs.
jupyter_execute_notebooks = "cache"

# The maximum time (in seconds) each notebook cell is allowed to run.
execution_timeout = 30

# Merge stderr and stdout in a single stream.
nb_merge_streams = True

# Designate additional file types to be converted to notebooks.
# Here we add support for traditional jupytext percent notebook format
nb_custom_formats = {".pct.py": ["jupytext.reads", {"fmt": "py:percent"}]}

# A sample of MyST-Parser configuration options for MyST markdown files.
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/dev", None),
    "requests": ("https://docs.python-requests.org/en/latest/", None),
    "openeye": ("https://docs.eyesopen.com/python_modules/cookbook/python/", None),
    "rdkit": ("https://www.rdkit.org/docs/", None),
}

# source_parsers = {".rst": "restructuredtext", ".txt": "markdown", ".md": "markdown"}

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_material"

# A dictionary of options that influence the look and feel of the selected theme.
# These are theme-specific. Refer to your ``html_theme`` documentation for guidance.
html_theme_options = {
    "nav_title": "TEST-TOOLS",
    "repo_name": "test-tools",
    "globaltoc_depth": 1,
    "globaltoc_collapse": True,
    "globaltoc_includehidden": True,
    "color_primary": "deep-orange",
    "color_accent": "orange",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "master_doc": False,
    "version_dropdown": False,
}

# The list of sidebars to include. Refer to your ``html_theme`` documentation for guidance on which are available.
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# The title for the HTML documentation generated with Sphinx’s own templates. It is shown in your browser's tab.
html_title = "Docs | test-tools"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# A list of CSS files to pass into the template engine's context for all pages.
# The filename is relative to the ``html_static_path`` option.
html_css_files = ["stylesheets/custom.css"]

# If true (and html_copy_source is true as well), links to the reST sources will be added to the sidebar. The default is True.
html_show_sourcelink = False

# If true, “Created using Sphinx” is shown in the HTML footer. The default is True.
html_show_sphinx = False
