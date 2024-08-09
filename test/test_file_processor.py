# SPDX-License-Identifier: BSD
#
# This file is part of Pyosmium.
#
# Copyright (C) 2024 Sarah Hoffmann.
import pytest
import osmium as o

@pytest.mark.parametrize('init', [None, 1])
def test_file_processor_bad_init(init):
    with pytest.raises(TypeError):
        o.FileProcessor(init)

def test_simple_generator(opl_buffer):
    count = 0
    for obj in o.FileProcessor(opl_buffer('n1 x5 y5')):
        assert obj.type_str() == 'n'
        assert obj.id == 1
        count += 1

    assert count == 1

def test_generator_with_location(opl_buffer):
    data = opl_buffer("""\
              n1 x10 y20
              n2 x11 y21
              w45 Nn1,n2
              """)

    count = 0
    for obj in o.FileProcessor(data).with_locations():
        count += 1
        if obj.type_str() == 'w':
            assert len(obj.nodes) == 2
            assert [n.ref for n in obj.nodes] == [1, 2]
            assert [n.location.lon for n in obj.nodes] == [10, 11]
            assert [n.location.lat for n in obj.nodes] == [20, 21]

    assert count == 3

def test_generator_with_areas(opl_buffer):
    data = opl_buffer("""\
            n10 x3 y3
            n11 x3 y3.01
            n12 x3.01 y3.01
            n13 x3.01 y3
            w12 Nn10,n11,n12,n13,n10 Tbuilding=yes
            """)

    count = 0
    for obj in o.FileProcessor(data).with_areas():
        if obj.type_str() == 'a':
            count += 1
            assert obj.from_way()
            assert obj.orig_id() == 12

    assert count == 1

def test_generator_with_filter(opl_buffer):
    data = opl_buffer("""\
            n10 x3 y3
            n11 x3 y3.01 Tfoo=bar
            """)

    count = 0
    for obj in o.FileProcessor(data).with_filter(o.filter.EmptyTagFilter()):
        count += 1
        assert obj.type_str() == 'n'
        assert obj.id == 11

    assert count == 1

def test_file_processor_header(tmp_path):
    fn = tmp_path / 'empty.xml'
    fn.write_text("""<?xml version='1.0' encoding='UTF-8'?>
    <osm version="0.6" generator="test-pyosmium" timestamp="2014-08-26T20:22:02Z">
         <bounds minlat="-90" minlon="-180" maxlat="90" maxlon="180"/>
    </osm>
    """)

    h = o.FileProcessor(fn).header

    assert not h.has_multiple_object_versions
    assert h.box().valid()
    assert h.box().size() == 64800.0

def test_file_processor_access_nodestore(opl_buffer):
    fp = o.FileProcessor(opl_buffer('n56 x3 y-3'))\
          .with_locations(o.index.create_map('sparse_mem_map'))

    for _ in fp:
        pass

    assert fp.node_location_storage.get(56).lat == -3
    assert fp.node_location_storage.get(56).lon == 3

def test_file_processor_bad_location_type(opl_buffer):
    with pytest.raises(TypeError, match='LocationTable'):
        o.FileProcessor(opl_buffer('n56 x3 y-3')).with_locations(67)
