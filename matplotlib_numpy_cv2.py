import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('C:/Users/Moniz/Desktop/images/cistina.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[390, 5], [750, 5], [505, 265], [885, 265]])
pts2 = np.float32([[0, 0], [310, 0], [0, 310], [350, 310]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (350, 310))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
