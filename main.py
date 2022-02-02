#importando bibliotecas
import cv2
import numpy as np
#lendo as imagens
imagem = cv2. imread("foto1.png")
gray = cv2.cvtColor( imagem, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,
     cv2. ADAPTIVE_THRESH_MEAN_C,
     cv2. THRESH_BINARY, 9, 9)
cor = cv2.bilateralFilter(imagem, 9, 250, 250)
cartoon = cv2.bitwise_and(cor, cor, mask=edges)
cv2. imshow("Image", imagem)
cv2. imshow("edges", edges)
cv2. imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()