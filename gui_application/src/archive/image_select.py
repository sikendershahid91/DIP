#!/usr/bin/env python3

import os
import glob
acceptable_file_type = ['png', 'jpg']


print("current working : ", os.getcwd())

os.chdir( input('path to image dir : ' ) )
print("current working :  " , os.getcwd())

images=[] 
for file_type in acceptable_file_type:
    images.extend(glob.glob("*."+file_type))

for image_number in range(0, len(images)):
    print(image_number, images[image_number])

image_number = int(input('select_images'))

print("IMAGE LOCATION: ", os.getcwd() + '/' + images[image_number] )  
