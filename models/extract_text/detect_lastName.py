import argparse

import cv2
import numpy as np
import pytesseract
# import the necessary packages
from imutils.object_detection import non_max_suppression

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
                help="path to input image")
ap.add_argument("-east", "--east", type=str,
                help="path to input EAST text detector")
ap.add_argument("-c", "--min-confidence", type=float, default=0.5,
                help="minimum probability required to inspect a region")
ap.add_argument("-w", "--width", type=int, default=320,
                help="nearest multiple of 32 for resized width")
ap.add_argument("-e", "--height", type=int, default=320,
                help="nearest multiple of 32 for resized height")
ap.add_argument("-p", "--padding", type=float, default=0.0,
                help="amount of padding to add to each border of ROI")
ap.add_argument("-l", "--language", type=str, default='eng',
                help="Tesseract language")
ap.add_argument("-o", "--oem", type=float, default=1,
                help="OCR Engine Mode")
ap.add_argument("-psm", "--psm", type=float, default=6,
                help="Page Segmentation Mode")

args = vars(ap.parse_args())
image = cv2.imread(args["image"])
orig = image.copy()

# Define the coordinates for each zone: (startX, startY, endX, endY)
first_name_coords = (787, 315, 1313, 406)  # Coordinates for the last name zone
last_name_coords = (793, 467, 1206, 537)  # Coordinates for the first name zone

# Extract text from defined zones using the coordinates
last_name_roi = orig[last_name_coords[1]:last_name_coords[3], last_name_coords[0]:last_name_coords[2]]
first_name_roi = orig[first_name_coords[1]:first_name_coords[3], first_name_coords[0]:first_name_coords[2]]

# Apply Tesseract OCR to each defined zone
lang = args["language"]
oem = args["oem"]
psm = args["psm"]
config = (f"-l {lang} --oem {oem} --psm {psm}")
lastName = pytesseract.image_to_string(last_name_roi, config=config)
firstName = pytesseract.image_to_string(first_name_roi, config=config)

# Print or process the extracted text from each zone
print("Last Name:", lastName)
print("First Name:", firstName)
