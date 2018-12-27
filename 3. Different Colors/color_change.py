
# Python program to read image 
  
# Import cv2 module 
import cv2 
  
# Reads the image 
img = cv2.imread('content_cc_dog1.png') 

# Shows the image
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'Original Image', (10,20), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('image', img)  
cv2.waitKey(0)

# Convert to YCrCb color space 
img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) 
  
# Shows the image
cv2.putText(img, 'YCrCb color space', (10,20), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('image', img)  
cv2.waitKey(0)

# Convert to HSV color space 
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Shows the image
cv2.putText(img, 'HSV color space', (10,20), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('image', img)  
  
cv2.waitKey(0)

# Converts to LAB color space 
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
  
# Shows the image
cv2.putText(img, 'LAB color space', (10,20), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('image', img)  
  
cv2.waitKey(0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.putText(img, 'EdgeMap color space', (10,20), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
cv2.imshow('EdgeMap', laplacian)  
  
cv2.waitKey(0)

cv2.destroyAllWindows()
