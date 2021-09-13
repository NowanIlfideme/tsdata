# `tsdata`: Time Series Datasets in Python

This repository is a collection of time series datasets.

The `tsdata` package itself contains a way of loading these into Pandas.

**NOTE**: The PyPI name is `py-tsdata` due to confict with a removed package.

**NOTE**: This package currently only includes the bare requirements.
However, I will keep adding data and functionality over time.

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

Currently only "raw" datasets are implemented.

You can see available datasets and load them directly into Pandas:

```python
>>> from tsdata.raw import available_data, load_data
>>> available_data()[:1]
['LakeHuron']
>>> load_data("LakeHuron").iloc[:2]
                   Time       Demand  Temperature        Date  Holiday
0  2011-12-31T13:00:00Z  4382.825174        21.40  2012-01-01     True
1  2011-12-31T13:30:00Z  4263.365526        21.05  2012-01-01     True
```

In the future, these will be available in `pandas` and `xarray` structures with proper indexes set.

## Contributing

If you have time series datasets you would like to add (that you have the rights
to contibute), please create a pull request!
