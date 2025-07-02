"""Load as a pandas dataframe."""

from pathlib import Path

import pandas as pd

from .base import FileDatasetCollection


class PandasRawDatasetCollection(FileDatasetCollection[pd.DataFrame]):
    """Load files from CSV or Parquet files, without post-processing."""

    @classmethod
    def supported_file_types(cls) -> set[str]:
        """File types supported by this Pandas type."""
        return {"csv", "parquet"}

    def load_file(self, path: Path) -> pd.DataFrame:
        """Load a file."""
        match path.suffix:
            case ".csv":
                return pd.read_csv(path, index_col=False, header="infer")
            case ".parquet":
                return pd.read_parquet(path)
            case _:
                raise ValueError(f"Unsupported file type: {path.suffix}")
