# Author : Navya Sushma Tummala
# rgb to cmyk
import numpy as np
import cv2
# reading an image
image = cv2.imread("sky.png")
[rows, cols, dim] = np.shape(image)
image1 = np.float32(image)/255
cmyk = np.zeros((rows, cols, 4), dtype="uint8")
for i in range(rows):
    for j in range(cols):
        # dividing by 255
        blue = image1[i, j, 0]
        green = image1[i, j, 1]
        red = image1[i, j, 2]
        # getting cmy components
        c = 1 - red
        m = 1 - green
        y = 1 - blue
        # extracting min of cmy to find k - black channel
        cmy_min = np.minimum(np.minimum(c, m), y)
        if cmy_min != 1:
            temp = 1 - cmy_min
            range_cmyk = 100
            # c, m, y, k channels
            cmyk[i][j][0] = range_cmyk * (c - cmy_min) / temp
            cmyk[i][j][1] = range_cmyk * (m - cmy_min) / temp
            cmyk[i][j][2] = range_cmyk * (y - cmy_min) / temp
            cmyk[i][j][3] = range_cmyk * cmy_min
        else:
            cmyk[i][j][0] = 0
            cmyk[i][j][1] = 0
            cmyk[i][j][2] = 0
            cmyk[i][j][3] = 1
cv2.imshow('result', cmyk)
cv2.waitKey(0)



