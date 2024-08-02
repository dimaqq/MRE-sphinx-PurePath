import sys
import os

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.sphinx']

autodoc_default_options = {'members': None} # None here means "yes"

# FIXME: I'm stuck here
# without python mapping, both 3.12.3 and 3.12.4 fail on overload arg type **specifically**
# with the mapping, 3.12.3 is OK, but 3.12.4 fails
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# If true, Sphinx will warn about all references where the target
# cannot be found.
nitpicky = True
