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
>>> "Tourism" in raw
True
>>> raw["Tourism"].head(2)
   Quarter    Region            State   Purpose       Trips
0  1998 Q1  Adelaide  South Australia  Business  135.077690
1  1998 Q2  Adelaide  South Australia  Business  109.987316
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
