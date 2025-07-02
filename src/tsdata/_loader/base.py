"""Time series data loader."""

from abc import abstractmethod
from collections.abc import Iterator, Mapping
from itertools import chain
from pathlib import Path
from typing import Generic, TypeVar

T = TypeVar("T")


class DatasetCollection(Mapping[str, T]):
    """Lazily-loading dataset collection.

    Mapping between dataset name and the eventual return type.
    """

    @abstractmethod
    def __getitem__(self, key: str) -> T:
        """Load the dataset with the given name."""

    @abstractmethod
    def __len__(self) -> int:
        """The number of datasets available."""

    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        """Iterator over keys."""


class FileDatasetCollection(DatasetCollection[T], Generic[T]):
    """File-based dataset collection."""

    # To override

    @classmethod
    @abstractmethod
    def supported_file_types(self) -> set[str]:
        """File types supported by this dataset type."""

    @abstractmethod
    def load_file(self, path: Path) -> T:
        """Load the file given the path as the given return type."""

    # Ready parts

    def __init__(self, dir: Path | str) -> None:
        """Create the dataset based on the given directory."""
        self.dir = Path(dir).resolve().absolute()

    def __repr__(self) -> str:
        """Recreative string representation."""
        cn = type(self).__qualname__
        d = str(self.dir)
        return f"{cn}({d!r})"

    @property
    def files(self) -> dict[str, Path]:
        """Iterator over all files within the dataset's directory."""
        globs = [self.dir.glob(f"*.{ft}") for ft in self.supported_file_types()]
        files = {x.stem: x for x in chain(*globs)}
        return files

    # Implement mapping interface

    def __iter__(self) -> Iterator[str]:
        """Iterator over keys."""
        return iter(self.files.keys())

    def __len__(self) -> int:
        """Number of avilable files."""
        return len(self.files)

    def __getitem__(self, key: str) -> T:
        """Load file based on key."""
        filepath = self.files[key]
        return self.load_file(filepath)
