import os

path = os.path.join("data", "geo.geojson")

remote_url = (
    "https://raw.githubusercontent.com/cividi/frictionless-geojson/main/data/geo.geojson"
)

geo = [
    {
        "id": 1,
        "name": "Polygon",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [8.47771167755127, 47.38199192001289],
                    [8.495779037475586, 47.38199192001289],
                    [8.495779037475586, 47.39091206104779],
                    [8.47771167755127, 47.39091206104779],
                    [8.47771167755127, 47.38199192001289],
                ]
            ],
        },
    },
    {
        "id": 2,
        "name": "LineString",
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [8.47771167755127, 47.38199192001289],
                [8.495779037475586, 47.38199192001289],
            ],
        },
    },
    {
        "id": 3,
        "name": "Point",
        "geometry": {
            "type": "Point",
            "coordinates": [8.47771167755127, 47.38199192001289],
        },
    },
]


raw_geojson = """{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "id": 1,
        "name": "Polygon"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [8.47771167755127, 47.38199192001289],
            [8.495779037475586, 47.38199192001289],
            [8.495779037475586, 47.39091206104779],
            [8.47771167755127, 47.39091206104779],
            [8.47771167755127, 47.38199192001289]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 2,
        "name": "LineString"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [8.47771167755127, 47.38199192001289],
          [8.495779037475586, 47.38199192001289]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 3,
        "name": "Point"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [8.47771167755127, 47.38199192001289]
      }
    }
  ]
}"""
