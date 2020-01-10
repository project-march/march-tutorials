import os
import sys

# Retrieve branch name
if os.getenv('CI'):
    branch_name = os.environ['TRAVIS_BRANCH']
else:
    import pygit2
    branch_name = pygit2.Repository('.').head.shorthand

sys.path += [os.path.abspath('_scripts')]

extensions = ['sphinx.ext.extlinks',
              'sphinx.ext.todo',
              'tutorialformatter']

todo_include_todos = True

# The master toctree document.
master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

project = u'march_tutorials'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'Melodic'
# The full version, including alpha/beta/rc tags.
release = 'Melodic'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Name of the style used to generate the html documentation
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    "display_github": True,
    "github_user": "project-march",
    "github_repo": "tutorials",
    "github_version": branch_name,
    "conf_py_path": "",
    "source_suffix": source_suffix,
    "css_files": ['_static/override.css'],
    "favicon": "favicon.ico",
    "logo": "logo.png"
}

# Global substitutions
rst_prolog = """
.. |march| replace:: March exoskeleton
"""

# Links
ros_distro = 'melodic'
extlinks = {'codedir': ('https://github.com/' + html_context["github_user"] + '/tutorials/tree/' + html_context["github_version"] + '/doc/%s', ''),
            'rootdir': ('https://github.com/' + html_context["github_user"] + '/tutorials/tree/' + html_context["github_version"] + '/%s', ''),
            'hardware-interface': ('https://github.com/' + html_context["github_user"] + '/hardware-interface/tree/develop/%s', ''),
            'input-device': ('https://github.com/' + html_context["github_user"] + '/input-device/tree/develop/%s', ''),
            'march': ('https://github.com/' + html_context["github_user"] + '/march/tree/develop/%s', ''),
            'monitor': ('https://github.com/' + html_context["github_user"] + '/monitor/tree/develop/%s', ''),
            'state-machine': ('https://github.com/' + html_context["github_user"] + '/state-machine/tree/develop/%s', ''),
            'simulation': ('https://github.com/' + html_context["github_user"] + '/simulation/tree/develop/%s', ''),
            'gait-files': ('https://github.com/' + html_context["github_user"] + '/gait-files/tree/develop/%s', ''),
            'ethercat-slaves': ('https://github.com/' + html_context["github_user"] + '/ethercat-slaves/tree/develop/%s', ''),
            'gait-generation': ('https://github.com/' + html_context["github_user"] + '/gait-generation/tree/develop/%s', ''),
            'march_website': ('http://projectmarch.nl', '')}

# Output file base name for HTML help builder.
htmlhelp_basename = 'MarchDocumentation'
