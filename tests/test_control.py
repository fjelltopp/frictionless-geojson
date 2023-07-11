from frictionless.resources import TableResource

from frictionless_geojson.control import GeoJsonControl

# General


def test_geojson_dialect():
    with TableResource(path="data/geo.geojson") as resource:
        assert isinstance(resource.dialect.get_control("geojson"), GeoJsonControl)
