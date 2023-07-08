from pykml import parser
from shapely import LineString, Point
from shapely.ops import nearest_points

def main():
    line_strings = []
    joins = []

    with open('new_territories/territory_1.kml') as f:
        doc = parser.parse(f).getroot().Document

    for pm in doc.Placemark:
        if hasattr(pm, "LineString"):
            # get the coordinates string and split into tuples
            coords = pm.LineString.coordinates.text.split()

            # convert the tuples into a list of floats and build LineStrings
            line = LineString([tuple(map(float, c.split(','))) for c in coords])
            line_strings.append(line)

        if hasattr(pm, "Point"):
            coords = pm.Point.coordinates
            coords_text = coords.text.strip()

            lon, lat, *_ = map(float, coords_text.split(','))

            point = Point(lon, lat)
            joins.append(point)

    for i, line in enumerate(line_strings):
        for j, join in enumerate(joins):
            p1, p2 = nearest_points(line, join)
            print(p1)

if __name__ == '__main__':
    main()