import numpy as np
import cv2

image = cv2.imread('lena.jpg', 1)
image = cv2.line(image, (10, 10), (255, 255), (0, 0, 255), 10)
image = cv2.arrowedLine(image, (110, 110), (355, 355), (222, 134, 179), 10)
image = cv2.rectangle(image, (384, 0), (510, 128), (222, 134, 179), 10)
image = cv2.circle(image, (447, 63), 63, (0, 255, 0), 1)

font = cv2.FONT_HERSHEY_COMPLEX
image = cv2.putText(image, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imshow('image', image)

k = cv2.waitKey(0)

if k == 27 or k == ord('q'):
    cv2.destroyAllWindows()