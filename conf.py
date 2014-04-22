# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('_exts'))

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
    'sensio.sphinx.refinclude', 'sensio.sphinx.configurationblock', 'sensio.sphinx.phpcode']

source_suffix = '.rst'
master_doc = 'index'
project = 'Elcodi'
copyright = u'2014, Elcodi.com'
version = ''
release = ''
exclude_patterns = []
html_theme = 'default'
htmlhelp_basename = 'Elcodidoc'
man_pages = [
    ('index', 'elcodi', u'Elcodi Documentation',
     [u'Elcodi.com'], 1)
]
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['php-standalone'] = PhpLexer(startinline=True)
lexers['php-symfony'] = PhpLexer(startinline=True)

primary_domain = 'php'

# set url for API links
api_url = 'http://api.symfony.com/master/%s'

