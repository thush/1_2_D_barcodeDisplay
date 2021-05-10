import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread
import EinkDisplay

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Read-In the image

img = imread('296-128-qr_.bmp')
# img = imread('296_128_Redone.gif')
# img = imread('100_100_DATAMATRIX_barcode.png')
# img = imread('296_128_USPostal.bmp')
# img = imread('296_128_UKPostal.bmp')


gray = rgb2gray(img)

img1 = np.asarray(gray, dtype=np.uint8)
h = gray.shape[0]
w = gray.shape[1]
ww = 0
if (w % 8):
	ww = w // 8 + 1
else:
	ww = w // 8
# print('ww -> ', ww)
# print('size', h, w)
# print('New Re-sized ', img1.size)


data = np.zeros((4736,), dtype=np.uint8)
i = 0
j = 0
A = np.zeros((128, 296))  # [gray.shape[0]][gray.shape[0]]
t = 7
k = 0
temp = 0
for row in gray:
    for x in row:
        if x == 0:
            A[i][j] = 0
        else:
            A[i][j] = 255
            # print('<',hex(temp), end='--')
            temp = temp | (1 << t)
            # print(hex(temp),'>')
        if (t > 0):
            t = t - 1
        else:
            data[k] = temp
            t = 7
            temp = 0
            k = k + 1

        # print("cell" ,i, j, end=' ')
        j = j + 1
    i = i + 1
    j = 0

B = A.transpose()
EinkDisplay.Eink_show(B)