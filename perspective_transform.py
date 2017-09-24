import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('paper_sudoku.jpg')


pts1 = np.float32([[163,206],[806,182],[875,781], [110,810]])
(tl, tr, br, bl) = pts1

widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
maxWidth = max(int(widthA), int(widthB))

heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
maxHeight = max(int(heightA), int(heightB))

pts2 = np.float32([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]])

M = cv2.getPerspectiveTransform(pts1,pts2)

img_transormed = cv2.warpPerspective(img,M,(maxWidth, maxHeight))

green_color = (116, 244, 66)
line_thickness = 20

cv2.rectangle(img, tuple(tl), tuple(tl), green_color, line_thickness)
cv2.rectangle(img, tuple(tr), tuple(tr), green_color, line_thickness)
cv2.rectangle(img, tuple(br), tuple(br), green_color, line_thickness)
cv2.rectangle(img, tuple(bl), tuple(bl), green_color, line_thickness)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(img_transormed),plt.title('Transormed')
plt.show()
