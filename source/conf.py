# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TechiePV Learning'
copyright = '2024, Pruthvi Vikram'
author = 'Pruthvi Vikram'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinx_togglebutton',
    'sphinxcontrib.details.directive',
    ]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
# html_theme = 'press'
# html_theme = 'groundwork'
html_static_path = ['_static']

html_static_path = [
    '_static/css/dropdown-rst.css',
    ]
