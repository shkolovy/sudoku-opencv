import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paper_sudoku.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imwrite('paper_sudoku_gray.jpg',img)

plt.imshow(img, 'gray')
plt.show()