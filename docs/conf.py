import sys
import os

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.sphinx']

autodoc_default_options = {'members': None} # None here means "yes"

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# If true, Sphinx will warn about all references where the target
# cannot be found.
nitpicky = True
