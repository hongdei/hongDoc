# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
import sphinx_rtd_theme

project = 'Sphinx'
copyright = '2024, hongDoc'
author = 'hongDoc'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


sys.stdout.reconfigure(encoding='utf-8')

extensions = []

templates_path = ['_templates']
extensions = ['recommonmark','sphinx_markdown_tables'] 

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['sphinx_rtd_theme.get_html_theme_path()']