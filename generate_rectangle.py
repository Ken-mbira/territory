import json

def generate_rectangle():
    with open('coordinates.txt') as coordinates_file:
        coordinates = []
        for coordinate in coordinates_file:
            coordinate = coordinate.removesuffix('\n')
            coordinates.append(coordinate.split(','))

        lats = [coord[1] for coord in coordinates]
        longs = [coord[0] for coord in coordinates]

        max_lat, min_lat = max(lats), min(lats)
        max_long, min_long = max(longs), min(longs)

        bottom_left_corner = [float(min_long),float(max_lat)]
        bottom_right_corner = [float(max_long),float(max_lat)]
        top_left_corner = [float(min_long),float(min_lat)]
        top_right_corner = [float(max_long),float(min_lat)]

        corners_json = {
            "top_left_corner" : top_left_corner,
            "top_right_corner" : top_right_corner,
            "bottom_left_corner" : bottom_left_corner,
            "bottom_right_corner" : bottom_right_corner
        }

        with open('corners.json','w') as json_output_file:
            json.dump(corners_json, json_output_file)


if __name__ == '__main__':
    generate_rectangle()