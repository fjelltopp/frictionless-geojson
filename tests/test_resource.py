from frictionless import Resource

from .helpers import geo, path

# General


def test_resource():
    resource = Resource(path)
    assert resource.name == "geo"
    assert resource.path == path
    assert resource.data is None
    assert resource.type == "table"
    assert resource.scheme == "file"
    assert resource.format == "geojson"
    assert resource.innerpath is None
    assert resource.compression is None
    assert resource.memory is False
    assert resource.remote is False
    assert resource.multipart is False
    assert resource.basepath is None
    assert resource.read_rows() == geo
