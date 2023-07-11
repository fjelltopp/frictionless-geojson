[![Build](https://img.shields.io/github/workflow/status/fjelltopp/frictionless-geojson/main/main)](https://github.com/fjelltopp/frictionless-geojson/actions)
[![Coverage](https://img.shields.io/codecov/c/github/fjelltopp/frictionless-geojson/main)](https://codecov.io/gh/fjelltopp/frictionless-geojson)
<!-- [![Registry](https://img.shields.io/pypi/v/frictionless_geojson.svg)](https://pypi.python.org/pypi/frictionless_geojson) -->
[![Codebase](https://img.shields.io/badge/github-main-brightgreen)](https://github.com/fjelltopp/frictionless-geojson)

# Frictionless GeoJSON

An extension to add [GeoJSON](https://geojson.org/geojson-spec.html) read and write support in [frictionless-py](https://framework.frictionlessdata.io).

Based on https://github.com/cividi/frictionless-geojson and https://github.com/frictionlessdata/framework/tree/main/frictionless/formats/json.

## Installation

Currently installation is only by cloning the repo and installing locally.
We will add a pip package when the extension is more mature.

```sh
git clone git@github.com:fjelltopp/frictionless-geojson.git
python -m pip install frictionless-geojson
```

## Dev version

```sh
python --version # should be > 3.8

# download project
git clone git@github.com:fjelltopp/frictionless-geojson.git
cd frictionless-geojson

# Load dynamic dev version
python -m pip install -e .
```

## Example - load GeoJSON and convert to CSV

```python
from frictionless import Resource
from pprint import pprint

# Load GeoJSON
data = Resource('<PATH-TO-GEOJSON>.geojson')

# Print out data
pprint(data.read_rows())

# Write CSV to disk - generates _geom column with WKT geometry
data.write('<PATH-TO-CSV>.csv')
```
