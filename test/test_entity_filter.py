# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2025 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.
import pytest
from helpers import CountingHandler

import npyosmium


@pytest.mark.parametrize('ent,cnt', [(npyosmium.osm.NODE, (1, 0, 0)),
                                     (npyosmium.osm.NODE | npyosmium.osm.WAY, (1, 1, 0)),
                                     (npyosmium.osm.ALL, (1, 1, 1))])
def test_entity_filter_simple(opl_reader, ent, cnt):
    data = """\
           n1 Ttype=node
           w1 Ttype=way
           r1 Ttype=rel
           """

    processed = CountingHandler()

    npyosmium.apply(opl_reader(data), npyosmium.filter.EntityFilter(ent), processed)

    assert list(cnt) == processed.counts[:3]
