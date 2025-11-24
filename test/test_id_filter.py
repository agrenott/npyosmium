# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2025 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.
import pytest
from helpers import IDCollector

import npyosmium


def test_id_filter_bad_argument():
    with pytest.raises(TypeError):
        npyosmium.filter.IdFilter(None)


def test_id_filter_simple(opl_reader):
    data = """\
           n1
           n2
           n4
           n200
           """

    ids = IDCollector()

    npyosmium.apply(opl_reader(data), npyosmium.filter.IdFilter([2, 5, 200, 201]), ids)

    assert ids.nodes == [2, 200]
