import sys

import npyosmium

if len(sys.argv) != 3:
    print("Usage: python create_nodecache.py <osm file> <node cache>")
    exit(-1)

reader = npyosmium.io.Reader(sys.argv[1], npyosmium.osm.osm_entity_bits.NODE)

idx = npyosmium.index.create_map("sparse_file_array," + sys.argv[2])
lh = npyosmium.NodeLocationsForWays(idx)

npyosmium.apply(reader, lh)

reader.close()
