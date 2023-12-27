import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet('yolo/yolov3.weights', 'yolo/yolov3.cfg')

# Replace 'path_to_image.jpg' with the path to your image file
image_path = 'images/IMG_3565.jpg'

# Load the image
image = cv2.imread(image_path)
height, width = image.shape[:2]
# Check if the image was loaded successfully
if image is None:
    print("Could not read the image")
else:
    print("Image loaded successfully")

# Get image dimensions and prepare it for YOLO network
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

# Set input to the network
net.setInput(blob)

# Perform forward pass and get output layer names
output_layers = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers)

# Process detections
for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:  # Filter out weak predictions
            # Get bounding box coordinates
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Calculate coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            # Draw bounding box and label
            color = (255, 0, 0)  # Change color as needed
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

# Display the output image
cv2.imshow('YOLO Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
