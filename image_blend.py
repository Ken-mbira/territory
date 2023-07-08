import os

from PIL import Image


def main(row_count, column_count, row_overlap, column_overlap, image_width, image_height):
    main_image = Image.new(
        "RGB", 
        (
            (image_width + (column_overlap * (column_count - 1))), 
            (image_height + (row_overlap * (row_count - 1)))
        ),
        (255,255,255)
    )

    current_position_x = 0 # current position on x axis

    current_image_number = 1

    for j in range(1,(column_count + 1)):
        new_image = Image.new(
            "RGB",
            (
                image_width,
                (image_height + (row_overlap * (row_count - 1)))
            ),
            (255,255,255)
        )
        
        current_position_y = 0 # current position on y axis

        countdown_image_number = current_image_number + (row_count - 1)

        for i in range(1,(row_count + 1)):
            current_image = Image.open(f"map_images/map_image_{countdown_image_number}.png")
            countdown_image_number = countdown_image_number - 1

            current_image_number = current_image_number + 1

            position_y = (0, current_position_y)
            current_position_y = current_position_y + row_overlap

            new_image.paste(current_image,position_y)

        position_x = (current_position_x,0)
        current_position_x = current_position_x + column_overlap

        main_image.paste(new_image, position_x)

    main_image.save("test_overlay.png")


if __name__ == '__main__':
    row_count = 5
    column_count = 6

    row_overlap = 187
    column_overlap = 455

    image_width = 640
    image_height = 640

    main(row_count, column_count, row_overlap, column_overlap, image_width, image_height)