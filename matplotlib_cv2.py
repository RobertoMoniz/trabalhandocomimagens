from matplotlib import pyplot as plt
import cv2

plt.style.use('classic')

img = cv2.imread('C:/Users/Moniz/Desktop/images/budismo.jpg')
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col, lw=2)
    plt.xlim([0, 256])
plt.grid()
plt.show()
