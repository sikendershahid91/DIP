import cip_ui
import filters
import cv2
import os
import sys
import numpy as np
cip_ui.app.window.protocol("WM_DELETE_WINDOW", cip_ui.app.window.quit)
cip_ui.app.window.mainloop()

"""baseDir = os.path.dirname(__file__) #lets us open files from current directory
test = cv2.imread(os.path.join(baseDir,"monkey.jpg"),0)
#print(test.shape)


def gray_to_color_transformation(image, intensity, weight):
        sliced_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if (image[i,j,0] == image[i,j,1]) and (image[i,j,0] == image[i,j,2]) and (image[i,j,0] in range(intensity[0], intensity[1])):
                    sliced_image[i, j, 0] = weight[0] * image[i, j ,0]
                    sliced_image[i, j, 1] = weight[1] * image[i, j, 0]
                    sliced_image[i, j, 2] = weight[2] * image[i, j, 0]
                else:
                    sliced_image[i, j, 0] = image[i, j,0]
                    sliced_image[i, j, 1] = image[i, j,1]
                    sliced_image[i, j, 2] = image[i, j,2]
        return sliced_image
newtest = np.zeros((test.shape[0], test.shape[1], 3), dtype=np.uint8)
def interval_slice(image,inter):
    newImage
    scale = np.amax(image)/inter
    for intensity in range(0,np.amax(image)/inter):
        scale = np.amax(image)/inter
        gray_to_color_transformation(image, scale, [255-scale,0+scale,255-scale])
    

for i in range(test.shape[0]):
    for j in range(test.shape[1]):
        newtest[i, j, 0] = test[i, j]
        newtest[i, j, 1] = test[i, j]
        newtest[i, j, 2] = test[i, j]
test = interval_slice(newtest,10)



cv2.imshow("sdf", test)
cv2.waitKey()
"""