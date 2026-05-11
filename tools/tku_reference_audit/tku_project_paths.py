from __future__ import annotations

import importlib.util
from pathlib import Path

_core_path = Path(__file__).resolve().parents[1] / "tku_project_paths.py"
_spec = importlib.util.spec_from_file_location("_tku_project_paths_core", _core_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Unable to load TKU path helper from {_core_path}")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

for _name in _module.__all__:
    globals()[_name] = getattr(_module, _name)

__all__ = list(_module.__all__)
