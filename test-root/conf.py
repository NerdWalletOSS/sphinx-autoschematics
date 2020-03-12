import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

extensions = ["autoschematics", "sphinx.ext.autodoc"]

source_suffix = ".rst"
master_doc = "index"
