import cv2
import numpy as np

img = cv2.imread('input_img/building.tif')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img_result = np.zeros(img.shape)

mask = np.array([[-1, -1, -1],
                 [0, 0, 0],
                 [1, 1, 1]])
rows, cols = img.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        sample_img = img[i-1:i+2, j-1:j+2]

        img_result[i, j] = np.sum(mask * sample_img)
cv2.imwrite('output_img/P3-1J25.jpg', img_result)
cv2.imshow('output', img_result)
cv2.waitKey()