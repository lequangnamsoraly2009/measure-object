# import cv2
from object_detector import *

img = cv2.imread("phone.jpeg")
# Load Object Detector

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

# Draw objects boundaries

for cnt in contours:
    # Vẽ Khung(contours) bao quanh object (polylines)
    cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

    # Get rectangle when draw polylines
    (x, y), (w, h), angle = cv2.minAreaRect(cnt)
    # Draw point center of object with color orange and size 2 pixels
    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)

    print(x, y)  # 297.5 and 171.5 ? x and y ? => (x,y) là center point of the object -> Tọa độ trung tâm của object
    print(w, h)   # 311.0 and 145.0
    print(angle)   # 90(độ)

cv2.imshow("Image", img)
cv2.waitKey(0)
