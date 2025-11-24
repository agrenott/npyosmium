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
 * [Boost](https://www.boost.org/) variant and iterator >= 1.70
 * [Python Requests](https://docs.python-requests.org/)
 * [scikit-build-core](https://scikit-build-core.readthedocs.io)
 * a C++17-compatible compiler (Clang 13+, GCC 10+ are supported)

### Compiling from Source

Make sure to install the development packages for expat, libz, libbz2
and boost.

The appropriate versions for Libosmium and Protozero will be downloaded into
the `contrib` directory when building the source package:

    python3 -m build -s

Alternatively, provide custom locations for these libraries by setting
`Libosmium_ROOT` and `Protozero_ROOT`.

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
### Compiling for Development

To compile during development, you can use the experimental
[Editable install mode](https://scikit-build-core.readthedocs.io/en/latest/configuration/index.html#editable-installs)
of scikit-build-core:

Create a virtualenv with scikit-build-core and pybind11 preinstalled:

    virtualenv /tmp/dev-venv
    /tmp/dev-venv/bin/pip install scikit-build-core pybind11

Now compile pyosmium with:

    /tmp/dev-venv/bin/pip install --no-build-isolation --config-settings=editable.rebuild=true -Cbuild-dir=/tmp/build -ve.


## Examples

The `example` directory contains small examples on how to use the library.
They are mostly ports of the examples in Libosmium and osmium-contrib.


## Testing

There is a small test suite in the test directory. This provides unit
test for the python bindings, it is not meant to be a test suite for Libosmium.

Testing requires `pytest` and `pytest-httpserver` and optionally
pytest-run-parallel and shapely. Install those into your dev environment:

    /tmp/dev-venv/bin/pip install --no-build-isolation --config-settings=editable.rebuild=true -Cbuild-dir=build -ve.[tests]

The test suite can be run with:

    /tmp/dev-venv/bin/pytest test

To test parallel execution on free-threaded Python, run:

    /tmp/dev-venv/bin/pytest test --parallel-threads 10 --iterations 100

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

Pregenerated man pages for the tools are available in `docs/man`. For rebuilding
the man pages run:

    cd docs
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

Upstream: Sarah Hoffmann (lonvia@denofr.de) and others. See commit logs for a full
list.
Fork and numpy interface: Aurélien Grenotton (agrenott@gmail.com)
