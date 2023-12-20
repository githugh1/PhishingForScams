# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PhishingForScams'
copyright = '2023, sulphurcrested, githugh1, lbdoak'
author = 'sulphurcrested, githugh1, lbdoak'
version = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# NOTE: more extensions configuration below!
extensions = [
                'autodoc2',
                'sphinx.ext.intersphinx',
                'sphinx.ext.duration',
                'sphinx.ext.doctest',
                'sphinx.ext.autosummary',
                'sphinx.ext.viewcode',
                'autoapi.extension'
            ]

autodoc2_packages = [
    '../src'
]
autodoc2_render_plugin = "myst"
# Document Python Code
autoapi_type = 'python'
autoapi_dirs = ['../../src', '../../tests']


templates_path = ['_templates']
exclude_patterns = [
    '**/.*',
    'venv/*',
    'kafka/*',
    '**__pycache__/*'
]



# -- Using Markdown as default ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/markdown.html
# myst config:
# https://myst-parser.readthedocs.io/en/latest/configuration.html#sphinx-config-options

extensions = extensions + ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
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
    "tasklist",
]
myst_heading_anchors = 6

# -- Napolean for NumPy and Google style docstrings -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

extensions = extensions + ['sphinx.ext.napoleon']
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



# -- Reference Mapping -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/referencing.html
# https://docs.readthedocs.io/en/stable/guides/intersphinx.html
# reStructuredText Examples:
# - :ref:`sphinx:ref-role`
# - :ref:`:ref: role <sphinx:ref-role>`
# - :doc:`sphinx:usage/extensions/intersphinx`
# - :doc:`Intersphinx <sphinx:usage/extensions/intersphinx>`
# MyST (Markdown) Examples:
# - {ref}`sphinx:ref-role`
# - {ref}`:ref: role <sphinx:ref-role>`
# - {doc}`sphinx:usage/extensions/intersphinx`
# - {doc}`Intersphinx <sphinx:usage/extensions/intersphinx>`


intersphinx_mapping = {
                        'python': ('https://docs.python.org/3', None),
                        'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
                       }

# We recommend adding the following config value.
# Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.
# This behavior has unintended side-effects, namely that documentations local references can
# suddenly resolve to an external location.
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]