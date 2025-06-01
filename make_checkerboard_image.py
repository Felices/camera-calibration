import numpy as np
import cv2

SQUARE_CM = 1  # Square size in cm
MIN_BORDER_CM = 0.1 # min_border size in cm. OpenCV requires the checkerboard to have a white border.
SCREEN_SIZE_CM = np.array([13,6]) # Screen height and width in cm
SCREEN_PPI = 385 # Points-per-inch resolution of the screen. Google "<device model> PPI" to find this.
CHECKERBOARD_PATH = 'checkerboard.png'  # Path to calibration images

INCHES_TO_CM = 2.54

if __name__ == "__main__":
    # Make blank white image
    px_per_cm = int(SCREEN_PPI / INCHES_TO_CM)
    
    image_squares = np.floor((SCREEN_SIZE_CM - MIN_BORDER_CM * 2) / SQUARE_CM).astype(int)
    
    border_cm = (SCREEN_SIZE_CM - image_squares * SQUARE_CM) / 2
    border_px = border_cm * px_per_cm
    square_px = SQUARE_CM * px_per_cm

    image = np.ones(SCREEN_SIZE_CM * px_per_cm) * 255 
    # Calculate the square size in pixels
    for row in range(0, image_squares[0]):
        first_black_square = 0
        if row % 2 == 1:
            first_black_square = 1
    
        for col in range(first_black_square, image_squares[1], 2):
            top_left = (np.array([col, row]) * square_px + border_px).astype(int)
            bottom_right = (top_left + square_px)
            image = cv2.rectangle(image, top_left, bottom_right.astype(int), (0,0,0), -1)

    cv2.imwrite(CHECKERBOARD_PATH, image)

    inner_corners = image_squares - 1
    print(f"Checkerboard saved to {CHECKERBOARD_PATH}")
    print(f"Inner corners: {inner_corners[0]}x{inner_corners[1]}")

