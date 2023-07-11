import pytest
from frictionless.resources import TableResource

from .helpers import geo, path, raw_geojson, remote_url

# Parser
# Read


def test_geojson_parser():
    with TableResource(path=path) as resource:
        assert resource.header == ["id", "name", "geometry"]
        assert resource.read_rows() == geo


def test_geojson_parser_from_buffer():
    data = raw_geojson.encode("utf-8")
    with TableResource(data=data, format="geojson") as resource:
        assert resource.header == ["id", "name", "geometry"]
        assert resource.read_rows() == geo


@pytest.mark.vcr
def test_json_parser_from_remote():
    with TableResource(path=remote_url) as resource:
        assert resource.header == ["id", "name", "geometry"]
        assert resource.read_rows() == geo


# Write


def test_geojson_parser_write_csv(tmpdir):
    source = TableResource(path=path)
    target = TableResource(path=str(tmpdir.join("geo.csv")))
    source.write(target)
    with target:
        assert target.header == ["id", "name", "geometry"]
        assert target.read_rows() == geo


def test_geojson_parser_write_geojson(tmpdir):
    source = TableResource(path=path)
    target = TableResource(path=str(tmpdir.join("geo.geojson")))
    source.write(target)
    with target:
        assert target.header == ["id", "name", "geometry"]
        assert target.read_rows() == geo
