from __future__ import annotations

from typing import List, Optional

import attrs

from frictionless.dialect import Control


@attrs.define(kw_only=True, repr=False)
class GeoJsonControl(Control):
    """GeoJson control representation.

    Control class to set params for GeoJSON reader/writer class.

    """

    type = "geojson"

    keys: Optional[List[str]] = None
    """
    Specifies the keys/columns to read from the resource.
    For example: keys=["id","name"].
    """

    keyed: bool = False
    """
    If set to True, It returns the data as key:value pair. Default value is False.
    """

    property: Optional[str] = None
    """
    This property specifies the path to the attribute in a geojson file, it it has
    nested fields.
    """

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "keys": {"type": "array", "items": {"type": "string"}},
            "keyed": {"type": "boolean"},
            "property": {"type": "string"},
        },
    }
