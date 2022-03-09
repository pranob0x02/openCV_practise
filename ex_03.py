# Drawing geomatrical shapes on images

import cv2

img = cv2.imread("lena.jpg", 1)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)

# print(img)

cv2.imshow('supersaiyan0x01', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
