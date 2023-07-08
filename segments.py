import csv
from shapely import wkt
from shapely.geometry import LineString, MultiPoint
import simplekml

def main():
    coordinate_mapping = {}


    with open ('source_territories.csv', newline='') as source_territories:
        reader = csv.DictReader(source_territories)
        for row in reader:
            coordinate_values = []
            loaded_val = wkt.loads(row['WKT'])

            try:
                coordinate_values = list(loaded_val.coords)
            except NotImplementedError:
                coordinate_values = list(loaded_val.exterior.coords)

            coordinate_mapping[row['name']] = coordinate_values

    with open('list_of_territories.csv', newline='') as territories:
        reader = csv.reader(territories)
        for i, territory in enumerate(reader):
            lines = [item.strip() for item in territory[1][1:-1].split(',')]
            bounding_intersections = []

            for i, line in enumerate(lines):
                for j, line_2 in enumerate(lines):
                    if i != j:
                        linestring_one = LineString(tuple(coordinate_mapping[line]))
                        linestring_two = LineString(tuple(coordinate_mapping[line_2]))
                        linestring_two_buffered = linestring_two.buffer(0.2)
                        if linestring_one.intersects(linestring_two_buffered):
                            intersection = linestring_one.intersection(linestring_two)

                            print(intersection)
            
            print(f"=============territory {i+1}=================")

            # kml = simplekml.Kml()

            # for line in lines:
            #     coordinate_list = coordinate_mapping[line]
            #     kml.newlinestring(name=line, coords=coordinate_list)

            # kml.save(f"new_territories/territory_{i}.kml")

                


if __name__ == '__main__':
    main()