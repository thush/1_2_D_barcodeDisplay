import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread
import EinkDisplay

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
# load the image
# img = imread('80_80_QRCode.gif')
# img = imread('100_100_DATAMATRIX_barcode.png')
# img = imread('xx1.gif')
img = imread('barcode.gif')
# img = imread('100_100_DATAMATRIX_barcode.png')
# img = imread('BZebra.gif')

gray = rgb2gray(img)
data = np.zeros((4736,), dtype=np.uint8)
i = 0
j = 0
A = np.zeros((100, 100))  # [gray.shape[0]][gray.shape[0]]
t = 7
k = 0
temp = 0
for row in gray:
    for x in row:
        if x == 0:
            A[i][j] = 0
        else:
            A[i][j] = 255
            print('<',hex(temp), end='--')
            temp = temp | (1 << t)
            # print(hex(temp),'>')
        # print(A[i][j],t, end=' ')
        if (t > 0):
            t = t - 1
        else:
            data[k] = temp
            # print('<',format(temp, '02x'),' ',format(data[k], '02x'),'--')
            t = 7
            temp = 0
            k = k + 1

        # print("cell" ,i, j, end=' ')
        j = j + 1
    # print('')
    # print('<-------------------->')
    i = i + 1
    j = 0
B = A.transpose()
EinkDisplay.Eink_show(A)