"""Data registry. This is very much a work-in-progress."""

from typing import Callable, Dict, List, Union

import pandas as pd

__all__ = ["Loader", "available_data", "get_loader", "load_data", "register_loader"]

Loader = Callable[[], pd.DataFrame]

__DATA_LOADERS__: Dict[str, Callable] = {}


def available_data() -> List[str]:
    """Returns all available datasets."""
    global __DATA_LOADERS__
    return list(sorted(__DATA_LOADERS__.keys()))


def get_loader(name: str) -> Loader:
    """Finds the loader for a given dataset name."""
    global __DATA_LOADERS__
    try:
        return __DATA_LOADERS__[name]
    except KeyError as e:
        raise KeyError(f"No data loader found for {name!r}") from e


def load_data(name: str) -> pd.DataFrame:
    """Loads the data for a given dataset name."""
    loader = get_loader(name)
    return loader()


def register_loader(name_or_func: Union[str, Loader]) -> Callable[[Loader], Loader]:
    """Decorator factory to register a data loader for a particular named dataset.

    Usage
    -----
    Use this as a decorator factory:

    ```
    @register_loader("my_dataset")
    def _func() -> pd.DataFrame:
        ...
    ```

    You can also use this without the call, in which case it will use the function name:

    ```
    @register_loader
    def my_dataset() -> pd.DataFrame:
        ...
    ```

    Both cases will register as: `df = load_data("my_dataset")`
    """

    if isinstance(name_or_func, str):
        name = name_or_func
        is_func = False
    elif callable(name_or_func):
        # FIXME: Check signature for a legal loader
        name = name_or_func.__qualname__
        is_func = True
    else:
        raise TypeError(f"Expected str or callable, got {name_or_func!r}.")

    def register(func: Loader) -> Loader:
        """Registers a function as a loader for a particular dataset."""
        global __DATA_LOADERS__

        if name in __DATA_LOADERS__.keys():
            raise ValueError(f"Attempted to redefine loader for {name!r}.")

        __DATA_LOADERS__[name] = func

        return func

    if is_func:
        return register(name_or_func)
    return register
