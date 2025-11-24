# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2025 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.
from datetime import datetime
from typing import TYPE_CHECKING, Any, Mapping, Optional, Sequence, Tuple, Union

if TYPE_CHECKING:
    import npyosmium.osm

    OSMObjectLike = Union['OSMObject', npyosmium.osm.OSMObject[Any]]

    TagSequence = Union[npyosmium.osm.TagList, Mapping[str, str], Sequence[Tuple[str, str]]]
    LocationLike = Union[npyosmium.osm.Location, Tuple[float, float]]
    NodeSequence = Union[npyosmium.osm.NodeRefList, Sequence[Union[npyosmium.osm.NodeRef, int]]]
    MemberSequence = Union[npyosmium.osm.RelationMemberList,
                           Sequence[Union[npyosmium.osm.RelationMember, Tuple[str, int, str]]]]


class OSMObject:
    """ Mutable version of [npyosmium.osm.OSMObject][].
    """

    def __init__(self, base: Optional['OSMObjectLike'] = None,
                 id: Optional[int] = None, version: Optional[int] = None,
                 visible: Optional[bool] = None, changeset: Optional[int] = None,
                 timestamp: Optional[datetime] = None, uid: Optional[int] = None,
                 tags: Optional['TagSequence'] = None, user: Optional[str] = None) -> None:
        """ Initialise an object with the following optional
            attributes: `id`, `version`, `visible`, `changeset`, `timestamp`,
            `uid` and `tags`. Timestamps may be strings or datetime objects.
            Tags can be an npyosmium.osm.TagList, a dict-like object
            or a list of tuples, where each tuple contains a (key value) string pair.

            If the `base` parameter is given in the constructor, then the object
            will be initialised first from the attributes of this base object.
        """
        if base is None:
            self.id = id
            self.version = version
            self.visible = visible
            self.changeset = changeset
            self.timestamp = timestamp
            self.uid = uid
            self.tags = tags
            self.user = user
        else:
            self.id = base.id if id is None else id
            self.version = base.version if version is None else version
            self.visible = base.visible if visible is None else visible
            self.changeset = base.changeset if changeset is None else changeset
            self.timestamp = base.timestamp if timestamp is None else timestamp
            self.uid = base.uid if uid is None else uid
            self.tags = base.tags if tags is None else tags
            self.user = base.user if user is None else user


class Node(OSMObject):
    """ The mutable version of [npyosmium.osm.Node][].
    """

    def __init__(self, base: Optional[Union['Node', 'npyosmium.osm.Node']] = None,
                 location: Optional['LocationLike'] = None,
                 **attrs: Any) -> None:
        """ Initialise a node with all optional attributes
            from npyosmium.osm.mutable.OSMObject as well as a `location` attribute.
            This may either be an [npyosmium.osm.Location][] or a tuple of
            lon/lat coordinates.

        """
        OSMObject.__init__(self, base=base, **attrs)
        if base is None:
            self.location = location
        else:
            self.location = location if location is not None else base.location


class Way(OSMObject):
    """ The mutable version of [npyosmium.osm.Way][].
    """

    def __init__(self, base: Optional[Union['Way', 'npyosmium.osm.Way']] = None,
                 nodes: Optional['NodeSequence'] = None, **attrs: Any) -> None:
        """ Initialise a way with all optional attributes
            from npyosmium.osm.mutable.OSMObject as well as a `nodes` attribute.
            This may either be an [npyosmium.osm.NodeRefList][] or a list
            consisting of [npyosmium.osm.NodeRef][] or simple node ids.
        """
        OSMObject.__init__(self, base=base, **attrs)
        if base is None:
            self.nodes = nodes
        else:
            self.nodes = nodes if nodes is not None else base.nodes


class Relation(OSMObject):
    """ The mutable version of [npyosmium.osm.Relation][].
    """

    def __init__(self, base: Optional[Union['Relation', 'npyosmium.osm.Relation']] = None,
                 members: Optional['MemberSequence'] = None, **attrs: Any) -> None:
        """ Initialise a relation with all optional attributes
            from npyosmium.osm.mutable.OSMObject as well as a `members` attribute.
            This may either be an [npyosmium.osm.RelationMemberList][] or
            a list consisting of [npyosmium.osm.RelationMember][] or
            tuples of (type, id, role). The
            member type must be a single character 'n', 'w' or 'r'.
        """
        OSMObject.__init__(self, base=base, **attrs)
        if base is None:
            self.members = members
        else:
            self.members = members if members is not None else base.members


def create_mutable_node(node: Union[Node, 'npyosmium.osm.Node'], **args: Any) -> Node:
    """ Create a mutable node replacing the properties given in the
        named parameters. Note that this function only creates a shallow
        copy which is still bound to the scope of the original object.
    """
    return Node(base=node, **args)


def create_mutable_way(way: Union[Way, 'npyosmium.osm.Way'], **args: Any) -> Way:
    """ Create a mutable way replacing the properties given in the
        named parameters. Note that this function only creates a shallow
        copy which is still bound to the scope of the original object.
    """
    return Way(base=way, **args)


def create_mutable_relation(rel: Union[Relation, 'npyosmium.osm.Relation'], **args: Any) -> Relation:
    """ Create a mutable relation replacing the properties given in the
        named parameters. Note that this function only creates a shallow
        copy which is still bound to the scope of the original object.
    """
    return Relation(base=rel, **args)
