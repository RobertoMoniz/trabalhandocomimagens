import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagem = np.array(Image.open('C:/Users/Moniz/Desktop/images/hal9000.jpg').convert("L"))
imagem[100:120] = 188
imagem[500:520] = 188

lx, ly = imagem.shape
print(lx, ly)

X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
imagem[mask] = 188

imagem[range(lx), range(ly)] = 255

plt.imshow(imagem, cmap='gray')
plt.show()
