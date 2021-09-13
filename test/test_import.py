"""Basic tests for importability."""


def test_import_basic():
    """This tests whether the `tsdata` package is importable."""
    import tsdata  # noqa


def test_import_raw():
    """This tests whether the `tsdata` package loads a dataset."""
    from tsdata.raw import available_data, load_data

    assert len(available_data()) > 0
    assert "LakeHuron" in available_data()
    load_data("LakeHuron")
