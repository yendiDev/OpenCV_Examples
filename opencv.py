import cv2

image = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
print(image)

cv2.imshow('Lena Image', image)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('lena_copy2.png', image)
    cv2.destroyAllWindows()
