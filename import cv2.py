import cv2
import numpy as np

# Carrega as quatro imagens
imagem1 = cv2.imread("ras1.jpeg")
imagem2 = cv2.imread("ras2.jpeg")
imagem3 = cv2.imread("ras3.jpeg")
imagem4 = cv2.imread("ras4.jpeg")

# Redimensiona as imagens para caberem em uma única janela
dimensoes = (400, 338)
imagem1 = cv2.resize(imagem1, dimensoes)
imagem2 = cv2.resize(imagem2, dimensoes)
imagem3 = cv2.resize(imagem3, dimensoes)
imagem4 = cv2.resize(imagem4, dimensoes)

# Aplica o filtro de Canny nas três imagens
imagem1_filtrada = imagem1
imagem2_filtrada = cv2.Sobel(imagem2, cv2.CV_8U, 1, 0, ksize=3)
imagem3_filtrada = cv2.filter2D(imagem3, -1, np.ones((3,3),np.float32)/9)
imagem4_filtrada = cv2.Laplacian(imagem4, cv2.CV_8U, ksize=3)

# Cria uma janela para as quatro imagens
cv2.namedWindow("Imagens")

# Empilha as quatro imagens horizontalmente
linha1 = np.hstack((imagem1_filtrada, imagem2_filtrada))
linha2 = np.hstack((imagem3_filtrada, imagem4_filtrada))
imagem_final = np.vstack((linha1, linha2))

# Cria uma caixa cinza transparente com o texto do efeito aplicado em cada imagem
caixa = np.zeros((60, imagem_final.shape[1], 3), np.uint8)
caixa[:] = (200, 200, 200)
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(caixa, "Original", (10, 40), fonte, 1, (0, 0, 0), 2)
cv2.putText(caixa, "Sobel", (dimensoes[0] + 20, 40), fonte, 1, (0, 0, 0), 2)
cv2.putText(caixa, "Blur", (dimensoes[0] * 2 + 20, 40), fonte, 1, (0, 0, 0), 2)
cv2.putText(caixa, "Laplacian", (dimensoes[0] * 3 + 20, 40), fonte, 1, (0, 0, 0), 2)

# Empilha a caixa e a imagem final verticalmente
imagem_final = np.vstack((caixa, imagem_final))

# Mostra a imagem final na janela
cv2.imshow("Imagens", imagem_final)

# Salva a imagem final
cv2.imwrite("imagem_final.jpg", imagem_final)

# Aguarda a tecla 'q' ser pressionada para fechar
while cv2.waitKey(0) & 0xFF != ord('q'):
    pass

# Libera a janela
cv2.destroyAllWindows()
