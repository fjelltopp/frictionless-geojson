from __future__ import annotations

import json
import tempfile

from frictionless import errors
from frictionless.exception import FrictionlessException
from frictionless.formats.inline import InlineControl
from frictionless.platform import platform
from frictionless.resources import TableResource
from frictionless.system import Parser, system

from .control import GeoJsonControl


class GeoJsonParser(Parser):
    """GeoJSON parser implementation."""

    requires_loader = True
    supported_types = [
        "array",
        "boolean",
        "geojson",
        "integer",
        "object",
        "string",
        "year",
    ]

    # Read

    def convert_geojson_object_to_row(self, source):
        for feature in source:
            yield {**feature["properties"], "geometry": feature["geometry"]}

    def read_cell_stream_create(self):
        path = "features.item"
        control = GeoJsonControl.from_dialect(self.resource.dialect)
        if control.property is not None:
            path = "%s.features.item" % control.property
        source = platform.ijson.items(self.loader.byte_stream, path, use_float=True)
        preparsed = self.convert_geojson_object_to_row(source)
        inline_control = InlineControl(keys=control.keys)
        with TableResource(
            data=preparsed, format="inline", control=inline_control
        ) as resource:
            try:
                yield next(resource.cell_stream)  # type: ignore
            except StopIteration:
                note = (
                    f'cannot extract GeoJSON tabular data from "{self.resource.normpath}"'
                )
                raise FrictionlessException(errors.SourceError(note=note))
            inline_control = InlineControl.from_dialect(resource.dialect)
            if inline_control.keyed:
                control.keyed = True
            yield from resource.cell_stream

    # Write

    def write_row_stream(self, source: TableResource):
        data = {
            "type": "FeatureCollection",
            "features": [],
        }
        control = GeoJsonControl.from_dialect(self.resource.dialect)
        with source:
            if self.resource.dialect.header and not control.keyed:
                data["features"].append(source.schema.field_names)
            for row in source.row_stream:
                item = {"type": "Feature", "properties": {}, "geometry": {}}
                cells = row.to_list(json=True)
                cell_items = dict(zip(row.field_names, cells))
                item["geometry"] = cell_items["geometry"]
                item["properties"] = {
                    k: v for k, v in cell_items.items() if k != "geometry"
                }
                data["features"].append(item)
        with tempfile.NamedTemporaryFile("wt", delete=False) as file:
            json.dump(data, file, indent=2)
        loader = system.create_loader(self.resource)
        loader.write_byte_stream(file.name)
