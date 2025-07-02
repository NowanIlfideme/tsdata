"""Basic tests for importability."""


def test_import_basic():
    """This tests whether the `tsdata` package is importable and can import a single dataset."""
    from tsdata import fpp3  # noqa

    assert len(fpp3.raw) > 0
    assert "LakeHuron" in fpp3.raw
    fpp3.raw["LakeHuron"]


def test_import_all_raw():
    """This tests whether the `tsdata` package loads all datasets."""
    import pandas as pd

    from tsdata import fpp3, fpppy

    for raw in [fpp3.raw, fpppy.raw]:
        assert len(raw) > 0
        for ds_name in raw:
            df = raw[ds_name]
            assert isinstance(df, pd.DataFrame)
