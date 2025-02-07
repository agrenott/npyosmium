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
 * [Pybind11](https://github.com/pybind/pybind11) >= 2.2
 * [expat](https://libexpat.github.io/)
 * [libz](https://www.zlib.net/)
 * [libbz2](https://www.sourceware.org/bzip2/)
 * [Boost](https://www.boost.org/) variant and iterator >= 1.41
 * [Python Requests](https://docs.python-requests.org/en/master/)
 * Python setuptools
 * a recent C++ compiler (Clang 3.4+, GCC 4.8+)

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

    pip install [--user] .

#### Using conda

(Tested on MacOS)
```
conda create -p .venv -c conda-forge  python=3.9 clang cmake boost
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

The test suite can be run with:

    pytest test


## Documentation

To build the documentation you need [Sphinx](http://sphinx-doc.org/)
and the [autoprogram extension](https://pythonhosted.org/sphinxcontrib-autoprogram/)
On Debian/Ubuntu install `python-sphinx sphinxcontrib-autoprogram`
or `python3-sphinx python3-sphinxcontrib.autoprogram`.

First compile the bindings as described above and then run:

    cd doc
    make html

For building the man pages for the tools run:

    cd doc
    make man

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
