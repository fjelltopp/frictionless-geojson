from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from frictionless.system import Plugin

from .control import GeoJsonControl
from .parser import GeoJsonParser

if TYPE_CHECKING:
    from frictionless.resource import Resource


class GeoJsonPlugin(Plugin):
    """Plugin for GeoJSON"""

    # Hooks

    def create_parser(self, resource: Resource):
        if resource.format == "geojson":
            return GeoJsonParser(resource)

    def detect_resource(self, resource: Resource):
        if resource.format == "geojson":
            resource.mediatype = "application/geo+json"
            resource.datatype = "table"

    def select_control_class(self, type: Optional[str] = None):
        if type == "geojson":
            return GeoJsonControl
