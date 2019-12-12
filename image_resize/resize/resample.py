import numpy as np
from .interpolation import interpolation

class resample:
    def __init__(self):
        self.class_name = '[resample]: '
        
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fc: scale along x direction (eg. 0.5, 1.5, 2.5)
        fr: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """
        print(self.class_name, "running nearest neighbor algorithm")
        (fc, fr) = (fx, fy)
        
        # Write your code for nearest neighbor interpolation here
        (r_size_orig, c_size_orig) = image.shape
        (r_size_new, c_size_new) = (np.uint16(r_size_orig * fr), np.uint16(c_size_orig * fc))
        new_image = np.zeros((r_size_new, c_size_new))

        print('r, y: ', r_size_orig, ' c, x: ', c_size_orig)
        print('r_new: ', r_size_new, ' c_new: ', c_size_new)
        
        for r in range(0, r_size_new):
            for c in range(0, c_size_new):
                if not r/fr%1 and not c/fc%1:
                    new_image[r][c] = image[np.uint16(r/fr)][np.uint16(c/fc)]
                else:
                    pt1=round(r/fr) if round(r/fr) < r_size_orig-1 else r_size_orig-1
                    pt2=round(c/fc) if round(c/fc) < c_size_orig-1 else c_size_orig-1
                    new_image[r][c] = image[np.uint16(pt1)][np.uint16(pt2)] 
        return new_image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        print(self.class_name, "running bilinear interpolation algorithm")
        (fc, fr) = (fx, fy)
        
        # Write your code for bilinear interpolation here
        (r_size_orig, c_size_orig) = image.shape
        (r_size_new, c_size_new) = (np.uint16(r_size_orig * fr), np.uint16(c_size_orig * fc))
        new_image = np.zeros((r_size_new, c_size_new))

        print('r, y: ', r_size_orig, ' c, x: ', c_size_orig)
        print('r_new: ', r_size_new, ' c_new: ', c_size_new)
        
        interpolate = interpolation()
        for r in range(0, r_size_new):
            for c in range(0, c_size_new):
                if not r/fr%1 and not c/fc%1:
                    new_image[r][c] = image[np.uint16(r/fr)][np.uint16(c/fc)]
                else:
                    (r_pt1, c_pt1) = (np.ceil(r/fr), np.ceil(c/fc))
                    (r_pt2, c_pt2) = (np.floor(r/fr), np.floor(c/fc))
                    r_pt1 = r_pt1 if r_pt1 < r_size_orig-1 else r_pt1-1
                    c_pt1 = c_pt1 if c_pt1 < c_size_orig-1 else c_pt1-1
          
                    I1 = image[np.uint16(r_pt1)][np.uint16(c_pt1)]
                    I2 = image[np.uint16(r_pt1)][np.uint16(c_pt2)]
                    I3 = image[np.uint16(r_pt2)][np.uint16(c_pt1)]
                    I4 = image[np.uint16(r_pt2)][np.uint16(c_pt2)]

                    pt1 = (r_pt1 * fr, c_pt1 * fc, I1)
                    pt2 = (r_pt1 * fr, c_pt2 * fc, I2)
                    pt3 = (r_pt2 * fr, c_pt1 * fc, I3)
                    pt4 = (r_pt2 * fr, c_pt2 * fc, I4)
                    unknown = (r, c)
                    
                    new_image[r][c] = np.uint16(interpolate.bilinear_interpolation(pt1,pt2,pt3,pt4, unknown))
        return new_image
