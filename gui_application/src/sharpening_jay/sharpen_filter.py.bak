import cv2
import numpy as np

image = cv2.imread('O_Image.png')
[h, w, val] = np.shape(image)

filtered_image = np.zeros((h+2, w+2, 3), dtype=np.int)
final_image = np.zeros((h, w, 3), dtype=np.int)
pad_image = np.zeros((h+2, w+2, 3), dtype=np.int)
nw = w + 2
nh = h + 2

for i in range(h):
    for j in range(w):
        pad_image[i + 1][j + 1][0] = image[i][j][0]
        pad_image[i + 1][j + 1][1] = image[i][j][1]
        pad_image[i + 1][j + 1][2] = image[i][j][2]

laplace_filter = [[0, 1, 0],
          [1, -4, 1],
          [0, 1, 0]]

red_arr = [[0 for x in range(3)] for y in range(3)]
green_arr = [[0 for x in range(3)] for y in range(3)]
blue_arr = [[0 for x in range(3)] for y in range(3)]
red_comp = [[0 for x in range(3)] for y in range(3)]
green_comp = [[0 for x in range(3)] for y in range(3)]
blue_comp = [[0 for x in range(3)] for y in range(3)]
red_sum = 0
green_sum = 0
blue_sum = 0
r1 = 0
c1 = 0
for i in range(1,  h+1):
    for j in range(1,  w+1):
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                red_arr[r1][c1] = pad_image[k][l][0]
                green_arr[r1][c1] = pad_image[k][l][1]
                blue_arr[r1][c1] = pad_image[k][l][2]
                c1 = c1 + 1
            r1 = r1 + 1
            c1 = 0
        r1 = 0

        red_comp = np.multiply(red_arr, laplace_filter)
        red_sum = red_comp.sum()
        red_sum = red_sum * (-1)

        green_comp = np.multiply(green_arr, laplace_filter)
        green_sum = green_comp.sum()
        green_sum = green_sum * (-1)

        blue_comp = np.multiply(blue_arr, laplace_filter)
        blue_sum = blue_comp.sum()
        blue_sum = blue_sum * (-1)

        filtered_image[i][j][0] = red_sum
        filtered_image[i][j][1] = green_sum
        filtered_image[i][j][2] = blue_sum
        red_arr = [[0 for x in range(3)] for y in range(3)]
        green_arr = [[0 for x in range(3)] for y in range(3)]
        blue_arr = [[0 for x in range(3)] for y in range(3)]

        red_comp = [[0 for x in range(3)] for y in range(3)]
        green_comp = [[0 for x in range(3)] for y in range(3)]
        blue_comp = [[0 for x in range(3)] for y in range(3)]

        red_sum = 0
        green_sum = 0
        blue_sum = 0

for i in range(h):
    for j in range(w):
        final_image[i][j][0] = filtered_image[i+1][j+1][0] + image[i][j][0]
        final_image[i][j][1] = filtered_image[i+1][j+1][1] + image[i][j][1]
        final_image[i][j][2] = filtered_image[i+1][j+1][2] + image[i][j][2]

cv2.imwrite('Final_Image.png', final_image)
