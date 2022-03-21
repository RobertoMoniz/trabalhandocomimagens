from PIL import Image

# Carregando a imagem
imagem = Image.open('C:/Users/Moniz/Desktop/images/cistina.jpg')

# Sumarizando detalhes sobre a imagem
# Modo da imagem
print(imagem.mode)
# Formato da imagem
print(imagem.format)
# Tamanho da imagem (largura, altura)
print(imagem.size)

# Apresentando a imagem
imagem.show()
