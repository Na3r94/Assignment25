import cv2
import numpy as np

img = cv2.imread('input_img/flower_input.jpg', 0)

img_result = cv2.GaussianBlur(img, (51, 51), 0)

rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        if img[i, j] > 130:
            img_result[i, j] = img[i, j]
for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_img = img_result[i-1:i+2, j-1:j+2]
        small_img_1d = small_img.reshape(9)
        small_img_sorted = np.sort(small_img_1d)
        img_result[i, j] = small_img_sorted[4]

cv2.imwrite('output_img/P1J25.jpg', img_result)
cv2.imshow('output', img_result)
cv2.waitKey()