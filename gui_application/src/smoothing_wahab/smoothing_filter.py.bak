import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image = cv2.imread('Lenna.png')

new_image = image.copy()
new_image1 = image.copy()
result1 = image.copy()
result2 = image.copy()
result3 = image.copy()
[h,w,val] = np.shape(new_image)



for i in range(h):
    for j in range(w):
        result1[i,j,0] = new_image[i,j,0]
        result1[i, j, 1] = 0
        result1[i, j, 2] = 0

        result2[i, j, 0] = 0
        result2[i, j, 1] = new_image[i, j, 1]
        result2[i, j, 2] = 0

        result3[i, j, 0] = 0
        result3[i, j, 1] = 0
        result3[i, j, 2] = new_image[i, j, 2]



#cv2.imshow('R-RGB', result1)
#cv2.imshow('G-RGB', result2)
#cv2.imshow('B-RGB', result3)


nrow=h+8
ncol=w+8
arr2 = np.zeros((nrow,ncol,3),dtype=np.uint8)




for i in range(h):
    for j in range(w):
        arr2[i+4][j+4][0] = new_image1[i][j][0]
        arr2[i+4][j+4][1] = new_image1[i][j][1]
        arr2[i+4][j+4][2] = new_image1[i][j][2]

temp1,temp2,temp3=np.shape(arr2)
#print (temp1,temp2,temp3)
"""for i in range(w):
    print (new_image[0][i])
for i in range(ncol):
    print (arr2[4][i])"""



sum1 = 0
sum2 = 0
sum3 = 0
for i in range(2, 2 + 2 + h + 2):
    for j in range(2, 2 + 2 + w + 2):
        for k in range(i - 2, i + 2 + 1):
            for l in range(j - 2, j + 1 + 2):
                sum1 = sum1 + arr2[k][l][0]
                sum2 = sum2 + arr2[k][l][1]
                sum3 = sum3 + arr2[k][l][2]
        arr2[i][j][0] = sum1 / 25
        arr2[i][j][1] = sum2 / 25
        arr2[i][j][2] = sum3 / 25

        sum1 = 0
        sum2 = 0
        sum3 = 0



cv2.imwrite('01.png',arr2)