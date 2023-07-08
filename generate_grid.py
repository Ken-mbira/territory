import json
import os

def generate_grid(num_rows, num_cols):

    top_left_corner = []
    bottom_left_corner = []
    top_right_corner = []

    with open('corners.json', 'r') as corners_file:
        corners = json.load(corners_file)
        top_left_corner = corners['top_left_corner']
        bottom_left_corner = corners['bottom_left_corner']
        top_right_corner = corners['top_right_corner']

    lat_step = round((top_left_corner[1] - bottom_left_corner[1]) / num_rows,14)
    long_step = round((top_right_corner[0] - top_left_corner[0]) / num_cols,14)

    try:
        os.remove('mid_points.txt')
    except FileNotFoundError:
        pass

    for i in range(num_cols):
        for j in range(num_rows):
            new_top_left = [(long_step * i) + bottom_left_corner[0],lat_step + -abs((lat_step * j) + bottom_left_corner[1])]
            new_bottom_right = [long_step + (long_step * i) + bottom_left_corner[0],-abs((lat_step * j) + bottom_left_corner[1])]

            midpoint_long = round(abs(new_top_left[0] + new_bottom_right[0])/2,14)
            midpoint_lat = round(-abs(new_top_left[1] + new_bottom_right[1])/2,14)

            with open('mid_points.txt','a') as mid_points_file:
                mid_points_file.write(f"{midpoint_lat}, {midpoint_long}\n")

if __name__ == '__main__':
    num_rows = 5
    num_cols = 6

    generate_grid(num_rows, num_cols)