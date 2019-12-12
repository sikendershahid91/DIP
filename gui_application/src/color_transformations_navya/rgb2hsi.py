import numpy as np
import math
import cv2
# Author: Navya Sushma Tummala
# conversion from rgb image to hsi


def rgb2hsi(image):
    image = np.float32(image)/255
    # extracting rgb channels
    red = image[:, :, 2]
    green = image[:, :, 1]
    blue = image[:, :, 0]
    hue = np.copy(red)
    temp = blue.shape[0]
    temp1 = blue.shape[1]
    # calculating hue
    for x in range(temp):
        for y in range(temp1):
            hue[x, y] = math.acos(0.5 * ((red[x, y] - green[x, y]) + (red[x, y] - blue[x, y])) / (np.sqrt((red[x, y] - green[x, y])**2 + ((red[x, y] - blue[x, y]) * (green[x, y] - blue[x, y])))))
            if green[x, y] >= blue[x, y]:
                hue[x, y] = hue[x, y]
            else:
            # 1 Degrees = pi/180 Radians
                hue[x, y] = ((360 * np.pi) / 180) - hue[x, y]
    # calculating saturation
    saturation = 1 - (3 / (red + green + blue + 0.00009) * (np.minimum(np.minimum(red, green), blue)))
    # calculating intensity
    intensity = (blue + green + red) / 3
    img = cv2.merge((hue, saturation, intensity))
    return img



