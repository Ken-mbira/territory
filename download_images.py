# api_key = AIzaSyA5m5ulxp_BjowWJn_ag3gMkhm0Hxz8hkg

import os
import requests

def remove_altitudes():
    with open('coordinate_inputs.txt') as coordinates_input_file:
        for line in coordinates_input_file:
            line_sections = line.split(',')
            coordinates_without_altitude = f"{line_sections[0]},{line_sections[1]}\n"

            with open('coordinates.txt', 'a') as coordinates_file:
                coordinates_file.write(coordinates_without_altitude)


def download_images(zoom, size, scale=1):
    api_key = "AIzaSyA5m5ulxp_BjowWJn_ag3gMkhm0Hxz8hkg"

    path = "color:purple|weight:10"
    with open('coordinates.txt', 'r') as coordinates_file:
        for line in coordinates_file:
            line = line.removesuffix('\n')
            sections = line.split(",")
            path = f"{path}|{sections[1]},{sections[0]}"

    params = {
        'zoom': zoom,
        'size': f'{size}x{size}',
        'scale': scale,
        'key': api_key,
        'maptype': 'hybrid',
        'path': path
    }

    url = "https://maps.googleapis.com/maps/api/staticmap"

    with open('mid_points.txt', 'r') as mid_points_file:
        file_count = 0

        try:
            os.mkdir(f"map_images")
        except FileExistsError:
            pass

        for point in mid_points_file:
            point.removesuffix("\n")
            coordinates = point.split(",")

            params['center'] = f"{coordinates[0]},{coordinates[1]}"

            response = requests.get(url, params=params)

            if response.status_code == 200:
                file_count += 1
                with open(f"map_images/map_image_{file_count}.png", 'wb') as image_file:
                    image_file.write(response.content)
                    print(f"saved file {file_count}")
            else:
                print(f"failed to save file {file_count}")


def main():
   download_images(18,800) 

if __name__ == '__main__':
    main()