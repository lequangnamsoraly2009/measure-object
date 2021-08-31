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
    # DIsplay box rectangle
    box = cv2.boxPoints(rectangle)
    # Làm tròn số
    box = np.int0(box)

    # Draw point center of object with color orange and size 2 pixels
    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)
    # Vẽ Khung(contours) bao quanh object (polylines)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
#     Display width and height on the picture
    cv2.putText(img, "Width {}".format(round(w, 1)), (int(x + 10), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 0.75, (25, 144, 255), 1)
    cv2.putText(img, "Height {}".format(round(h, 1)), (int(x + 10), int(y)), cv2.FONT_HERSHEY_PLAIN, 0.75, (25, 144, 255), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
