# import cv2
import numpy as np
from object_detector import *

img = cv2.imread("phone.jpeg")
# Load Object Detector

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

# Draw objects boundaries

for cnt in contours:
    # Get rectangle when draw polylines
    rectangle = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rectangle

    # Draw point center of object with color orange and size 2 pixels
    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)

    #
    box = cv2.boxPoints(rectangle)
    # Làm tròn số
    box = np.int0(box)

    # Vẽ Khung(contours) bao quanh object (polylines)
    cv2.polylines(img, [cnt], True, (255, 0, 0), 2)


cv2.imshow("Image", img)
cv2.waitKey(0)
