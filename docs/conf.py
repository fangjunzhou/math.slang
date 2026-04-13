from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_SRC = ROOT / "libs" / "glm_slang" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

project = "glm.slang"
author = "glm.slang contributors"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

myst_enable_extensions = ["colon_fence"]
myst_fence_as_directive = {"automodule"}

templates_path = ["_templates"]
exclude_patterns: list[str] = ["_build"]

html_theme = "furo"

root_doc = "index"

autodoc_mock_imports = ["pyglm", "slangpy", "spm_slang"]
autosummary_generate = True
