import cv2

# Load the image
image = cv2.imread("images/5.jpg")
clone = image.copy()


# Display the image and define ROIs by clicking on the image
def select_ROI(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False


# Create window and set mouse callback to select ROIs
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", select_ROI)

# Keep selecting ROIs until 'q' is pressed
while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Define zones based on selected ROIs
# Use 'refPt' values to set coordinates: (startX, startY, endX, endY)
last_name_coords = (refPt[0][0], refPt[0][1], refPt[1][0], refPt[1][1])

# Extract text from defined zones using the coordinates
#last_name_roi = clone[last_name_coords[1]:last_name_coords[3], last_name_coords[0]:last_name_coords[2]]

# Apply OCR to the defined zone to extract text
# Use pytesseract or your preferred OCR library
print(last_name_coords)
print("`````````````````````")
##print(last_name_roi)
# Clean up: close windows and release resources
cv2.destroyAllWindows()
