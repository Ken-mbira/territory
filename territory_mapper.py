from shapely.geometry import LineString, Polygon
from shapely.ops import unary_union
from pykml import parser
import simplekml

def main():

    line_strings = []

    with open('new_territories/territory_1.kml', 'r') as f:
        doc = parser.parse(f).getroot().Document

    for pm in doc.Placemark:
        if hasattr(pm, 'LineString'):
            # get the coordinates string and split into tuples
            coords = pm.LineString.coordinates.text.split()

            # convert the tuples into a list of floats and build LineStrings
            line = LineString([tuple(map(float, c.split(','))) for c in coords])

            # now you can do something with the line
            line_strings.append(line)

    merged = unary_union(line_strings)

    if merged.geom_type == 'LineString':
        poly = Polygon(merged)

    elif merged.geom_type == 'MultiLineString':
        # Assuming merged is a list of LineString objects
        lines = [line for line in merged.geoms if line.is_valid]

        # Now find the longest line
        longest_line = max(lines, key=lambda line: line.length)

        poly = Polygon(longest_line)
    else:
        raise ValueError(f"Unexpected geometry type: {merged.geom_type}")
    
    kml = simplekml.Kml()

    exterior_coords = poly.exterior.coords[:]

    # create a new polygon in KML
    pol = kml.newpolygon(name="A Polygon")

    # set the polygon's outer boundary
    pol.outerboundaryis = exterior_coords

    # save the KML
    kml.save("test_territory.kml")

if __name__ == '__main__':
    main()