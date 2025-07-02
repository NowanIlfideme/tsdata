# `tsdata`: Time Series Datasets in Python

This repository is a collection of time series datasets.

The `tsdata` package itself contains a way of loading these into Pandas.

**NOTE**: The PyPI name is `py-tsdata` due to confict with a removed package.

## Installing

You can install this as a regular Python package via pip:

```sh
pip install py-tsdata
```

## Quickstart

Check the version of the package after importing it:

```python
>>> import tsdata
>>> print(tsdata.__version__)
0.3.0
```

You can see available datasets and load them directly into Pandas:

```python
>>> from tsdata.fpp3 import raw
>>> "LakeHuron" in raw
True
>>> raw["LakeHuron"].iloc[:2]
                   Time       Demand  Temperature        Date  Holiday
0  2011-12-31T13:00:00Z  4382.825174        21.40  2012-01-01     True
1  2011-12-31T13:30:00Z  4263.365526        21.05  2012-01-01     True
```

## Supported Datasets

The currently support datasets are grouped into the following sources:

- `tsdata.fpppy`, with data from [Forecasting: Principles and Practice, the Pythonic Way](https://otexts.com/fpppy/)
- `tsdata.fpp3`, with data from [Forecasting: Principles and Practice, 3rd Edition](https://otexts.com/fpp3/) (extracted from the R package)

Currently only "raw" datasets are implemented, i.e. as-is.

## Contributing

If you have time series datasets you would like to add (that you have the rights
to contibute), please create a pull request!

Preferred formats are `.parquet` or `.csv`, though if it can be read by Pandas - we can add it.
