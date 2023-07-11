from frictionless import system

from .plugin import GeoJsonPlugin
from .settings import VERSION as __version__

system.register("geojson", GeoJsonPlugin())
