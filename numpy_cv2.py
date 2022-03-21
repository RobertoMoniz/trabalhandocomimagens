import numpy as np
import cv2

img = cv2.imread('C:/Users/Moniz/Desktop/images/caverna.jpg')
print(img)
print(img.dtype)
print(img.ndim)

blue, green, red = cv2.split(img)
zeros = np.zeros(blue.shape, np.uint8)
blueBGR = cv2.merge((blue, zeros, zeros))
greenBGR = cv2.merge((zeros, green, zeros))
redBGR = cv2.merge((zeros, zeros, red))

cv2.imshow('imagem', img)
cv2.imshow('blue BGR', blueBGR)
cv2.imshow('green BGR', greenBGR)
cv2.imshow('red BGR', redBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()
