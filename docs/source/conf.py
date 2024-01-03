# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# trick to include the project directory to the path!
import os
import sys
project_path = os.path.abspath('../..')
sys.path.insert(0, project_path)

from src import __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PhishingForScams'
copyright = '2023, sulphurcrested, githugh1, lbdoak'
author = 'sulphurcrested, githugh1, lbdoak'
version = __version__
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "autodoc2",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode"
]

templates_path = ['_templates']

exclude_patterns = [
    '**/.*',
    'venv/*',
    'kafka/*',
    '**/__pycache__',
    '**/data',
    '**/dataset'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Autodoc2 ---------------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/config.html
autodoc2_packages = [
    '../../src',
    {
        "path": "../../tests"
    }
    # '../../tests'
]

# creating a specific version directory
autodoc2_output_dir = f"apidocs/{version}"
autodoc2_render_plugin = "myst"

# autodoc2_docstring_parser_regexes = [
#     (r"src", "myst"),
#     (r"tests", "myst")
# ]
# autodoc2_docstrings = "all"
autodoc2_hidden_objects = ['inherited', 'private']
                           

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None)
}
# 0 days for debugging!
intersphinx_cache_limit = 0

# -- Using Markdown as default ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/markdown.html
# myst config:
# https://myst-parser.readthedocs.io/en/latest/configuration.html#sphinx-config-options


myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
]
myst_heading_anchors = 6

myst_substitutions = {
    "LATEST_API_REF": f"[API Reference](./{autodoc2_output_dir}/index)"
}
myst_dmath_double_inline = True

# https://sphinx-tippy.readthedocs.io/en/latest/#configuration

# https://sphinx-togglebutton.readthedocs.io/en/latest/use.html



# ----- Additional Setup ------

import sphinx
from sphinx.addnodes import toctree
from sphinx.util.console import colorize
sphinx_logger = sphinx.util.logging.getLogger(__name__)
message_prefix = colorize("bold", "[PhishingForScams] [Autodoc2] ")
message = lambda x: message_prefix + colorize("darkgreen", x)


def setup(app: Sphinx) -> None:
    app.connect("doctree-read", connect_api, priority=400)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


# This code is taken from AUTOAPI and modified for this use case
# https://github.com/readthedocs/sphinx-autoapi/blob/main/autoapi/extension.py#L152
def connect_api(app, doctree) -> None:
    """Inject Autodoc2 API into the TOC Tree dynamically."""

    if app.env.docname == "index":
        all_docs = set()
        insert = True
        nodes = list(doctree.traverse(toctree))
        toc_entry = f"{autodoc2_output_dir}/index"
        add_entry = (
            nodes
            and autodoc2_output_dir
        )
        if not add_entry:
            return
        # Capture all existing toctree entries
        for node in nodes:
            for entry in node["entries"]:
                all_docs.add(entry[1])
        # Don't insert autoapi it's already present
        for doc in all_docs:
            if doc.find(autodoc2_output_dir) != -1:
                insert = False
        if insert:
            # Insert AutoAPI index
            nodes[-1]["entries"].append((None, toc_entry))
            nodes[-1]["includefiles"].append(toc_entry)
            sphinx_logger.info(message(f"Adding Autodoc2 API TOCTree [{toc_entry}] to Doctree"))
