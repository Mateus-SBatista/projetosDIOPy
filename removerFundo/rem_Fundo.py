from rembg import remove
from PIL import Image

#Importa imagem original
img = Image.open('removerFundo\img.JPG')

#Remove fundo da Imagem
img_without_back = remove(img)

#Salva imagem sem fundo
img_without_back.save('img_without_back.png')