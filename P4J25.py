import cv2
import numpy as np

img = cv2.imread('input_img/batman.jpg', 0)

img_result = np.zeros(img.shape)

len = int(input('Enter convolution size: '))
mask = np.ones((len,len)) / (len**2)

rows, cols = img.shape

border = int(len/2)

for i in range(border, rows - border -1):
    for j in range(border, cols - border - 1):
        small_img = img[i-border:i+border+1, j-border:j+border+1]
        img_result[i, j] = np.sum(small_img * mask)


cv2.imwrite(f'output_img/P4-{len}J25.jpg', img_result)
cv2.imshow('output', img_result)
cv2.waitKey()