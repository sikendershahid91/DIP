import numpy as np
import cv2

def smoothing(image):
    new_image1 = image.copy()
    [h,w,val] = np.shape(new_image1)
    arr3 = image.copy()
    nrow=h+8
    ncol=w+8
    arr2 = np.zeros((nrow,ncol,3),dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            arr2[i+4][j+4][0] = new_image1[i][j][0]
            arr2[i+4][j+4][1] = new_image1[i][j][1]
            arr2[i+4][j+4][2] = new_image1[i][j][2]

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

    for i in range(h):
        for j in range(w):
            arr3[i][j][0] = arr2[i+4][j+4][0]
            arr3[i][j][1] = arr2[i+4][j+4][1]
            arr3[i][j][2] = arr2[i+4][j+4][2]
    return arr3