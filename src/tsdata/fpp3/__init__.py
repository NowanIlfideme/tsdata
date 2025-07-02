"""Loads data exported from Forecasting: Principles and Practice, 3rd Edition.

This module is automatically generated from available CSV files.

See Also
--------
https://otexts.com/fpp3/
"""

from pathlib import Path

import pandas as pd

from tsdata._loader.as_pandas import PandasRawDatasetCollection

raw = PandasRawDatasetCollection(dir=Path(__file__).parent)


def __getattr__(name: str) -> pd.DataFrame:
    if name in raw.keys():
        return raw[name]
    try:
        return globals()[name]
    except KeyError:
        raise AttributeError(name)
