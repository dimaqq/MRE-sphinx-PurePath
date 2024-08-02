# ruff: noqa
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# Pull in fix from https://github.com/sphinx-doc/sphinx/pull/11222/files to fix
# "invalid signature for autoattribute ('ops.pebble::ServiceDict.backoff-delay')"
import re  # noqa: E402
import sphinx.ext.autodoc  # noqa: E402

# Add custom Sphinx extensions as needed.
# This array contains recommended extensions that should be used.
# NOTE: The following extensions are handled automatically and do
# not need to be added here: myst_parser, sphinx_copybutton, sphinx_design,
# sphinx_reredirects, sphinxcontrib.jquery, sphinxext.opengraph
custom_extensions = [
    'sphinx_tabs.tabs',
    'canonical.youtube-links',
    'canonical.related-links',
    'canonical.custom-rst-roles',
    'canonical.terminal-output',
    'notfound.extension',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    ]

autoclass_content = 'class'

autodoc_member_order = 'alphabetical'

autodoc_default_options = {
    'members': None,            # None here means "yes"
    'undoc-members': None,
    'show-inheritance': None,
}

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# If true, Sphinx will warn about all references where the target
# cannot be found.
nitpicky = True
