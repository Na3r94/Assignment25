import cv2
import numpy as np

img = cv2.imread('input_img/lion.png', 0)

img_result = np.zeros(img.shape)

mask = np.array([[0, -1, 0],
                 [-1, 4, -1],
                 [0, -1, 0]])

rows, cols = img.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_img = img[i-1:i+2, j-1:j+2]
        img_result[i,j] = np.sum(mask * small_img)

cv2.imwrite('output_img/P2J25.jpg', img_result )
cv2.imshow('Output', img_result)
cv2.waitKey()