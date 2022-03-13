# Drawing geomatrical shapes on images

import cv2
# import numpy as np


img = cv2.imread("lena.jpg", 1)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 255), 10)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), -1)
# print(img)

img = cv2.circle(img, (447, 63), 60, (0, 0, 255), -1)


# putting text in the image
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "OpenCV", (10, 500), font,
                  4, (0, 0, 255), 10, cv2.LINE_AA)

cv2.imshow('supersaiyan0x01', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
