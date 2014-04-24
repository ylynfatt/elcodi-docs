# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('_exts'))

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
    'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig',
    'sensio.sphinx.refinclude', 'sensio.sphinx.configurationblock', 'sensio.sphinx.phpcode']

source_suffix = '.rst'
master_doc = 'index'
project = 'Elcodi'
copyright = u'2014, Elcodi.com'
version = '0.1.0'
release = '0.1.0'
exclude_patterns = []

# -- Options for HTML output ---------------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".

html_title = "Elcodi documentation"
html_short_title = "Elcodi"
htmlhelp_basename = 'Elcodidoc'
man_pages = [
    ('index', 'elcodi', u'Elcodi Documentation',
     [u'Elcodi.com'], 1)
]

# Guzzle theme https://github.com/guzzle/guzzle_sphinx_theme
import guzzle_sphinx_theme

# Uses a Guzzle style Pygments theme
# pygments_style = 'guzzle_sphinx_theme.GuzzleStyle'

# Adds an HTML table visitor to apply Bootstrap table classes
html_translator_class = 'guzzle_sphinx_theme.HTMLTranslator'
html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    "project_nav_name": "Elcodi",
    "github_user": "elcodi",
    "github_repo": "elcodi",
    "disqus_comments_shortname": "elcodi"
}

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**':       ['localtoc.html', 'searchbox.html']
}

# templates_path = ['_templates']

# End of Guzzle theme specific config

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['php-standalone'] = PhpLexer(startinline=True)
lexers['php-symfony'] = PhpLexer(startinline=True)

primary_domain = 'php'

# set url for API links
api_url = 'http://api.symfony.com/master/%s'

