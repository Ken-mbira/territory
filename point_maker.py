from pykml import parser
from shapely import LineString, Point, Polygon
from shapely.geometry import mapping
import simplekml

def main():
    line_strings = []

    with open('new_territories/territory_4.kml') as f:
        doc = parser.parse(f).getroot().Document

    for pm in doc.Placemark:
        if hasattr(pm, "LineString"):
            # get the coordinates string and split into tuples
            coords = pm.LineString.coordinates.text.split()

            # convert the tuples into a list of floats and build LineStrings
            line = LineString([tuple(map(float, c.split(','))) for c in coords])
            line_strings.append(line)

    polygon_points = []

    for line in line_strings:
        if not polygon_points:
            polygon_points.extend(list(line.coords))

        else:
            if polygon_points[-1] == line.coords[0]:
                polygon_points.extend(list(line.coords)[1:])
            elif polygon_points[-1] == line.coords[-1]:
                polygon_points.extend(list(line.coords)[::-1][1:])
            else:
                polygon_points.extend(list(line.coords))


    polygon = Polygon(polygon_points)

    kml = simplekml.Kml()

    kml_coordinates = [(x, y) for x, y, z in polygon.exterior.coords]

    pol = kml.newpolygon(name='A polygon', outerboundaryis=kml_coordinates)

    kml.save('output.kml')

    with open('coordinates.txt','w') as f:
        for coord in polygon_points:
            f.write(f"{coord[0]},{coord[1]}\n")


if __name__ == '__main__':
    main()