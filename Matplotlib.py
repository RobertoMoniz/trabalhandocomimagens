from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# Carrega a imagem como um array de pixels
data = mpimg.imread('C:/Users/Moniz/Desktop/images/japanese.png')
# Imprime os arrays de dados
print(data)
# Imprime o tipo
print(type(data))

# Dados sobre o array de pixels
# Tipo de dados
print(data.dtype)
# Dimensão de dados
print(data.shape)

# Apresenta o array de pixels como uma imagem
lum_img = data[:, :, 0]
imgplot = plt.imshow(lum_img, cmap='twilight')
plt.axis('off')
plt.show()