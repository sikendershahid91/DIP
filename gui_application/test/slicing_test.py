#!/usr/bin/env python3

import sys
sys.path.append('../src/')

from filters import Slice

import numpy as np
import cv2

if __name__ == '__main__':
## TESTS

    #Linear Slicing Test
    test_image = np.array([
        [1, 2, 3],
        [3, 2, 1],
        [3, 4, 2]])

    linear_sliced_image = np.array([
        [1, 6, 9],
        [9, 6, 1],
        [9, 4, 6]])

    output_image = Slice().linear_slice(test_image.copy(), [2, 3], 3)

    if np.array_equal(output_image, linear_sliced_image):
        print("Passed")
    else:
        print("Failed")
        print(output_image)
        print(linear_sliced_image)

    #Inverted Linear Slicing Test
    inverted_linear_sliced_image = np.array([
        [0, 1, 1],
        [1, 1, 0],
        [1, 2, 1]])


    output_image = Slice().inverted_linear_slice(test_image.copy(), [3, 5], 0.5)

    if np.array_equal(output_image, inverted_linear_sliced_image):
        print("Passed")
    else:
        print("Failed")
        print(output_image)
        print(inverted_linear_sliced_image)

    #Constant Slicing Test
    constant_sliced_image = np.array([
        [1, 7, 7],
        [7, 7, 1],
        [7, 4, 7]])
    output_image = Slice().constant_slice(test_image.copy(), [2, 3], 3)

    if np.array_equal(output_image, constant_sliced_image):
        print("Passed")
    else:
        print("Failed")
        print(output_image)
        print(constant_sliced_image)

    #Inverted Constant Slicing
    inverted_constant_sliced_image = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 2, 1]])
    output_image = Slice().inverted_constant_slice(test_image.copy(), [3, 5], 0.5)

    if np.array_equal(output_image, inverted_constant_sliced_image):
        print("Passed")
    else:
        print("Failed")
        print(output_image)
        print(inverted_constant_sliced_image)

    import matplotlib.pyplot as plt
    input_image = cv2.imread("../images/Lenna.png", 0)

    # testing gray level to color transformation
    plt.imshow(input_image)
    plt.show()
    output_image = Slice().gray_to_color_transformation(input_image, (0.3, 0.5, 0.2))
    plt.imshow(output_image)
    plt.show()
    output_image = Slice().gray_to_color_transformation(input_image, (0.5, 0.1, 0.4))
    plt.imshow(output_image)
    plt.show()

    print(input_image.shape)
    print(np.min(input_image), np.max(input_image))
    while True:
        print(np.min(input_image), np.max(input_image))
        plt.imshow(input_image)
        plt.show()
        gain = input('what gain: ')
        a, b = input('what bounds ').split()
        Slice().constant_slice( input_image, [float(a), float(b)], float(gain))
        plt.imshow(input_image)
        plt.xticks([]), plt.yticks([])
        plt.show()
        cv2.waitKey(0)

