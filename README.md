# npyosmium

Fork of [pyosmium](https://github.com/osmcode/pyosmium), including (only one for the time being) efficient numpy interface.

# pyosmium

Provides Python bindings for the [Libosmium](https://github.com/osmcode/libosmium) C++
library, a library for working with OpenStreetMap data in a fast and flexible
manner.

[![Github Actions Build Status](https://github.com/agrenott/npyosmium/workflows/CI/badge.svg)](https://github.com/agrenott/nyosmium/actions?query=workflow%3ACI)
[![PyPI version](https://badge.fury.io/py/npyosmium.svg)](https://badge.fury.io/py/npyosmium)

## Installation

npyosmium works with Python >= 3.8. Pypy is known to not work.

### Using Pip

The recommended way to install npyosmium is via pip:

    pip install npyosmium

We provide binary wheels for Linux and Windows 64 for all actively
maintained Python versions.

For other versions, a source wheel is provided. Make sure to install all
external dependencies first. On Debian/Ubuntu-like systems, the following
command installs all required packages:

    sudo apt-get install build-essential cmake libboost-dev \
                         libexpat1-dev zlib1g-dev libbz2-dev


### Installing from source

#### Prerequisites

npyosmium has the following dependencies:

 * [libosmium](https://github.com/osmcode/libosmium) >= 2.16.0
 * [protozero](https://github.com/mapbox/protozero)
 * [cmake](https://cmake.org/)
 * [Pybind11](https://github.com/pybind/pybind11) >= 2.7
 * [expat](https://libexpat.github.io/)
 * [libz](https://www.zlib.net/)
 * [libbz2](https://www.sourceware.org/bzip2/)
 * [Boost](https://www.boost.org/) variant and iterator >= 1.41
 * [Python Requests](https://docs.python-requests.org/en/master/)
 * Python setuptools
 * [Requests](https://requests.readthedocs.io)
 * a C++17-compatible compiler (Clang 7+, GCC 8+)

### Compiling from Source

For libosmium, protozero and pybind11 source code, npyosmium uses git submodules in `contrib/`.

```
git submodule init
git submodule update
```

You can also set custom locations with `LIBOSMIUM_PREFIX`, `PROTOZERO_PREFIX` and
`PYBIND11_PREFIX` respectively.


To use a custom boost installation, set `BOOST_PREFIX`.

To compile the bindings during development, you can use
[build](https://pypa-build.readthedocs.io/en/stable/).
On Debian/Ubuntu-like systems, install `python3-build`, then
run:

```
sudo apt install build-essential cmake libsparsehash-dev libexpat1-dev libboost-dev zlib1g-dev libbz2-dev liblz4-dev
pip install build
python3 -m build -w
```

To compile and install the bindings, run

    pip install .

#### Using conda

(Tested on MacOS)
```
conda create -p .venv -c conda-forge  python=3.10 clang cmake boost
conda activate .venv/
pip install build pytest shapely
# Resume cloning and build as described earlier
```

## Examples

The `example` directory contains small examples on how to use the library.
They are mostly ports of the examples in Libosmium and osmium-contrib.


## Testing

There is a small test suite in the test directory. This provides unit
test for the python bindings, it is not meant to be a test suite for Libosmium.

Testing requires `pytest` and `pytest-httpserver`. On Debian/Ubuntu install
the dependencies with:

    sudo apt-get install python3-pytest python3-pytest-httpserver

or install them with pip using:

    pip install npyosmium[tests]

The test suite can be run with:

    pytest test

### CI/CD

Relying on [act](https://nektosact.com/introduction.html) to test GitHub actions locally (to some extent).
Install:
- act
- GitHub CLI (gh)
- [gh-act extension](https://github.com/nektos/gh-act): `gh extension install nektos/gh-act`

Then to test a single matrix combination:
```
act --artifact-server-path /tmp/artifacts --concurrent-jobs 1 --matrix os:ubuntu-22.04 --matrix 'cibw_build:cp310-*' pull_request
```

## Documentation

To build the documentation you need [mkdocs](https://www.mkdocs.org/)
with the [mkdocstrings](https://mkdocstrings.github.io/)
and [jupyter](https://github.com/danielfrg/mkdocs-jupyter) extensions
and the [material theme](https://squidfunk.github.io/mkdocs-material/).

All necessary packages can be installed via pip:

    pip install npyosmium[docs]

To build the documentation run:

    mkdocs build

or to few it locally, you can use:

    mkdocs serve

For building the man pages for the tools run:

    cd docs
    make man

The man pages can be found in docs/man.

## Bugs and Questions

If you find bugs or have feature requests, please report those in the
[github issue tracker](https://github.com/agrenott/npyosmium/issues/).

For general questions about using pyosmium you can use the
[OSM development mailing list](https://lists.openstreetmap.org/listinfo/dev)
or ask on [OSM help](https://help.openstreetmap.org/).

## License

npyosmium is available under the BSD 2-Clause License. See LICENSE.TXT.

## Authors

Sarah Hoffmann (lonvia@denofr.de), Aurélien Grenotton (agrenott@gmail.com)
