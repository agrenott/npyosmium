# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2025 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.

from npyosmium.osm._osm import ALL as ALL
from npyosmium.osm._osm import AREA as AREA
from npyosmium.osm._osm import CHANGESET as CHANGESET
from npyosmium.osm._osm import NODE as NODE
from npyosmium.osm._osm import NOTHING as NOTHING
from npyosmium.osm._osm import OBJECT as OBJECT
from npyosmium.osm._osm import RELATION as RELATION
from npyosmium.osm._osm import WAY as WAY
from npyosmium.osm._osm import Box as Box
from npyosmium.osm._osm import Location as Location
from npyosmium.osm._osm import osm_entity_bits as osm_entity_bits
from npyosmium.osm.mutable import (
                              create_mutable_node,
                              create_mutable_relation,
                              create_mutable_way,
)
from npyosmium.osm.types import Area as Area
from npyosmium.osm.types import Changeset as Changeset
from npyosmium.osm.types import InnerRing as InnerRing
from npyosmium.osm.types import Node as Node
from npyosmium.osm.types import NodeRef as NodeRef
from npyosmium.osm.types import NodeRefList as NodeRefList
from npyosmium.osm.types import OSMObject as OSMObject
from npyosmium.osm.types import OuterRing as OuterRing
from npyosmium.osm.types import Relation as Relation
from npyosmium.osm.types import RelationMember as RelationMember
from npyosmium.osm.types import RelationMemberList as RelationMemberList
from npyosmium.osm.types import Tag as Tag
from npyosmium.osm.types import TagList as TagList
from npyosmium.osm.types import Way as Way
from npyosmium.osm.types import WayNodeList as WayNodeList

setattr(Location, '__repr__',
        lambda loc: f'npyosmium.osm.Location(x={loc.x!r}, y={loc.y!r})'
                    if loc.valid() else 'npyosmium.osm.Location()')
setattr(Location, '__str__',
        lambda loc: f'{loc.lon_without_check():.7f}/{loc.lat_without_check():.7f}'
                    if loc.valid() else 'invalid')

setattr(Box, '__repr__',
        lambda b: f"npyosmium.osm.Box(bottom_left={b.bottom_left!r}, top_right={b.top_right!r})")
setattr(Box, '__str__', lambda b: f'({b.bottom_left!s} {b.top_right!s})')
