import cv2
import numpy as np

# 1. Read your beautiful rose image from Google Drive
image_path = 'test.JPG'
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not read test.JPG. Please make sure the image exists!")
else:
    # 2. Convert BGR to HSV color space
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 3. Define HSV ranges for detecting red color
    lower_red1 = np.array([0, 50, 40])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 40])
    upper_red2 = np.array([180, 255, 255])
    
    # 4. Create masks for red color ranges
    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    red_mask = mask1 + mask2
    
    # 5. Extract red color components from the rose
    detected_color = cv2.bitwise_and(img, img, mask=red_mask)
    
    # 6. Save the processed image with CAPITAL extension
    cv2.imwrite('output_rose.JPG', detected_color)
    print("Success! The processed image has been saved as 'output_rose.JPG'")
