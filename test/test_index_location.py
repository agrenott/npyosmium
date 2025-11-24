# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2025 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.
import pytest

import npyosmium


def test_list_types():
    ml = npyosmium.index.map_types()
    assert isinstance(ml, list)
    assert ml


@pytest.mark.parametrize('use_get', [True, False])
@pytest.mark.parametrize('use_set', [True, False])
def test_set_get(use_set, use_get):
    table = npyosmium.index.create_map("flex_mem")
    if use_set:
        table.set(4, npyosmium.osm.Location(3.4, -5.6))
    else:
        table[4] = npyosmium.osm.Location(3.4, -5.6)
    if use_get:
        loc = table.get(4)
    else:
        loc = table[4]
    assert loc.lon == pytest.approx(3.4)
    assert loc.lat == pytest.approx(-5.6)


def test_get_unset():
    table = npyosmium.index.create_map("flex_mem")
    with pytest.raises(KeyError):
        table.get(56)


def test_array_get_unset():
    table = npyosmium.index.create_map("flex_mem")
    with pytest.raises(KeyError):
        table[56]


def test_set_negative():
    table = npyosmium.index.create_map("flex_mem")
    with pytest.raises(TypeError):
        table.set(-4, npyosmium.osm.Location(3.4, -5.6))


def test_array_set_negative():
    table = npyosmium.index.create_map("flex_mem")
    with pytest.raises(TypeError):
        table[-4] = npyosmium.osm.Location(3.4, -5.6)


def test_used_memory():
    table = npyosmium.index.create_map("flex_mem")
    table.set(4, npyosmium.osm.Location(3.4, -5.6))

    assert table.used_memory() > 0


def test_clear():
    table = npyosmium.index.create_map("flex_mem")
    table.set(593, npyosmium.osm.Location(0.35, 45.3))
    table.get(593)
    table.clear()
    with pytest.raises(KeyError):
        table.get(593)
