import cv2

image = cv2.imread("images/IMG_3564.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]



# Display the processed image
cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
