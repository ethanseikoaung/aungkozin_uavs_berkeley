import cv2
import numpy as np

image_path = "D:\Downloads\opencv_test_projects\Starship_-_Flight_13_(Sunset).jpg"
# Read the image
image = cv2.imread(image_path)

#Reducing the size of the image by 70% to make it fit on the screen
scale_percent = 25 # percent of original size
width = int(image.shape[1] * scale_percent / 100) # Calculate the new width
height = int(image.shape[0] * scale_percent / 100) # Calculate the new height
dim = (width, height) # Create a tuple for the new dimensions
resized_image = cv2.resize(image, dim)

print(resized_image.shape) # Print the shape of the image (height, width, channels)
print(resized_image[0,0]) # Print the pixel value at the top-left corner of the image

cv2.imshow('Image', resized_image) # 'Image' is the window name

px = resized_image[100, 100]
print("BGR:", px)

hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

lower = np.array([100, 50, 50]) # Lower bound of the color range in HSV
upper = np.array([180, 50, 100]) # Upper bound of the color
mask = cv2.inRange(hsv, lower, upper) # Create a mask for the specified color range
cv2.imshow('Mask', mask) # Display the mask
cv2.waitKey(0) # Wait for a key press to close the windows

