"""Unrefined data sources.

This is meant as a stopgap solution while deciding on a useful metadata format.

Usage
-----
`available_data()` returns the list of all available datasets.

`load_data("name")` loads the Pandas dataframe of dataset `"name"`.

`get_loader` and `register_loader` are used internally to work with loader functions.
"""

from . import fpp3  # noqa
from .registry import available_data, get_loader, load_data, register_loader  # noqa
