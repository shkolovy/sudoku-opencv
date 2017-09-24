import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paper_sudoku.jpg')


pts1 = np.float32([[163,206],[806,182],[875,781], [110,810]])
(tl, tr, br, bl) = pts1

green_color = (116, 244, 66)
line_thickness = 20

cv2.rectangle(img, tuple(tl), tuple(tl), green_color, line_thickness)
cv2.rectangle(img, tuple(tr), tuple(tr), green_color, line_thickness)
cv2.rectangle(img, tuple(br), tuple(br), green_color, line_thickness)
cv2.rectangle(img, tuple(bl), tuple(bl), green_color, line_thickness)

plt.imshow(img)
plt.show()
