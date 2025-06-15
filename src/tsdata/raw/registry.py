"""Data registry. This is very much a work-in-progress."""

from collections.abc import Callable
from functools import partial
from typing import TypeVar, overload

import pandas as pd

__all__ = ["Loader", "available_data", "get_loader", "load_data", "register_loader"]

Loader = Callable[[], pd.DataFrame]

__DATA_LOADERS__: dict[str, Callable] = {}


def available_data() -> list[str]:
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


TLoader = TypeVar("TLoader", bound=Loader)


@overload
def register_loader(name_or_func: str) -> Callable[[TLoader], TLoader]: ...


@overload
def register_loader(name_or_func: TLoader, *, name: str | None = None) -> TLoader: ...


def register_loader(
    name_or_func: str | Loader, *, name: str | None = None
) -> Loader | Callable[[Loader], Loader]:
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
    global __DATA_LOADERS__

    if isinstance(name_or_func, str):
        name = name_or_func
        return partial(register_loader, name=name)  # type: ignore

    if callable(name_or_func):
        # FIXME: Check signature for a legal loader
        if name is None:
            name = name_or_func.__qualname__
        func = name_or_func

        if name in __DATA_LOADERS__.keys():
            raise ValueError(f"Attempted to redefine loader for {name!r}.")

        __DATA_LOADERS__[name] = func

        return func

    raise TypeError(f"Expected str or callable, got {name_or_func!r}.")
