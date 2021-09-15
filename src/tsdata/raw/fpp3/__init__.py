"""Loads data exported from Forecasting: Principles and Practice, 3rd Edition.

This module is automatically generated from available CSV files.
"""

from pathlib import Path
from typing import Dict

import pandas as pd

from ..registry import Loader, register_loader

__all__ = []
_funcs: Dict[str, Loader] = {}

for _filename in Path(__file__).parent.glob("*.csv"):
    _name = _filename.stem
    __all__.append(_name)

    @register_loader(_name)
    def _loader_i(_fn=_filename) -> pd.DataFrame:
        return pd.read_csv(_fn)

    _loader_i.__qualname__ = _loader_i.__name__ = _name
    _funcs[_name] = _loader_i


def __getattr__(name: str):
    if name in _funcs.keys():
        return _funcs[name]
    try:
        return globals()[name]
    except KeyError:
        raise AttributeError(name)
