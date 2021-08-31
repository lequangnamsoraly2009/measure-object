# import cv2
from object_detector import *

img = cv2.imread("phone.jpeg")
# Load Object Detector

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

# Draw objects boundaries

for cnt in contours:
    # Vẽ Khung bao quanh object (polylines)
    cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

    # Get rectangle when draw polylines

cv2.imshow("Image", img)
cv2.waitKey(0)
