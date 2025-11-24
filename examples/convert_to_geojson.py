"""
Output an OSM file as geojson.

This demonstrates how to use the GeoJSON factory.
"""
import json
import sys

import npyosmium

geojsonfab = npyosmium.geom.GeoJSONFactory()


class GeoJsonWriter(npyosmium.SimpleHandler):

    def __init__(self):
        super().__init__()
        # write the Geojson header
        print('{"type": "FeatureCollection", "features": [')
        self.first = True

    def finish(self):
        print(']}')

    def node(self, n):
        if n.tags:
            self.print_object(geojsonfab.create_point(n), n.tags)

    def way(self, w):
        if w.tags and not w.is_closed():
            self.print_object(geojsonfab.create_linestring(w), w.tags)

    def area(self, a):
        if a.tags:
            self.print_object(geojsonfab.create_multipolygon(a), a.tags)

    def print_object(self, geojson, tags):
        geom = json.loads(geojson)
        if geom:
            feature = {'type': 'Feature', 'geometry': geom, 'properties': dict(tags)}
            if self.first:
                self.first = False
            else:
                print(',')

            print(json.dumps(feature))


def main(osmfile):
    handler = GeoJsonWriter()

    handler.apply_file(osmfile,
                       filters=[npyosmium.filter.EmptyTagFilter().enable_for(npyosmium.osm.NODE)])
    handler.finish()

    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python %s <osmfile>" % sys.argv[0])
        sys.exit(-1)
    sys.exit(main(sys.argv[1]))
