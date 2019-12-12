# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

from numpy import sqrt, zeros
import matplotlib.pyplot as plt

class Filtering:
    image = None
    filter = None
    cutoff = None
    order = None

    def __init__(self, image, filter_name, cutoff, order = 0):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        filter_name: the name of the mask to use
        cutoff: the cutoff frequency of the filter
        order: the order of the filter (only for butterworth
        returns"""
        self.filter_name = filter_name
        self.image = image
        if filter_name == 'ideal_l':
            self.filter = self.get_ideal_low_pass_filter
        elif filter_name == 'ideal_h':
            self.filter = self.get_ideal_high_pass_filter
        elif filter_name == 'butterworth_l':
            self.filter = self.get_butterworth_low_pass_filter
        elif filter_name == 'butterworth_h':
            self.filter = self.get_butterworth_high_pass_filter
        elif filter_name == 'gaussian_l':
            self.filter = self.get_gaussian_low_pass_filter
        elif filter_name == 'gaussian_h':
            self.filter = self.get_gaussian_high_pass_filter

        self.cutoff = cutoff
        self.order = order


    def get_ideal_low_pass_filter(self, shape, cutoff):
        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""

        mask = zeros(shape)
        row_size, col_size = shape[0], shape[1]
        center_row, center_col = row_size/2 , col_size/2
        for r in range(0, row_size):
            for c in range(0, col_size):
                freq_dist = sqrt( (r-center_row)**2 + (c-center_col)**2 )
                mask[r,c] = 0.0 if freq_dist > cutoff else 1.0

        return mask


    def get_ideal_high_pass_filter(self, shape, cutoff):
        """Computes a Ideal high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask
        return 1 - self.get_ideal_low_pass_filter(shape, cutoff)
        
    def get_butterworth_low_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth low pass mask"""
        
        mask = zeros(shape)
        row_size, col_size = shape[0], shape[1]
        center_row, center_col = row_size/2 , col_size/2
        for r in range(0, row_size):
            for c in range(0, col_size):
                freq_dist = sqrt( (r-center_row)**2 + (c-center_col)**2 )
                mask[r,c] = (1/(1+(freq_dist/cutoff)*order)) if freq_dist > cutoff else 1.0

        return mask

    def get_butterworth_high_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask
        mask = zeros(shape)
        row_size, col_size = shape[0], shape[1]
        center_row, center_col = row_size/2 , col_size/2
        for r in range(0, row_size):
            for c in range(0, col_size):
                freq_dist = sqrt( (r-center_row)**2 + (c-center_col)**2 )
                mask[r,c] = (1/(1+(freq_dist/cutoff)*order*2)) if freq_dist < cutoff else 1.0

        return mask
        # return 1 - self.get_butterworth_low_pass_filter(shape, cutoff, order*2) # wrong ?
    
    
    
    def get_gaussian_low_pass_filter(self, shape, cutoff):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""
        from numpy import exp
        
        mask = zeros(shape)
        row_size, col_size = shape[0], shape[1]
        center_row, center_col = row_size/2 , col_size/2
        for r in range(0, row_size):
            for c in range(0, col_size):
                freq_dist = sqrt( (r-center_row)**2 + (c-center_col)**2 )
                mask[r,c] = (exp(-(freq_dist**2)/(cutoff*2)**2)) if freq_dist > cutoff else 1.0

        return mask

    def get_gaussian_high_pass_filter(self, shape, cutoff):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask
        from numpy import exp
        mask = zeros(shape)
        row_size, col_size = shape[0], shape[1]
        center_row, center_col = row_size/2 , col_size/2
        for r in range(0, row_size):
            for c in range(0, col_size):
                freq_dist = sqrt( (r-center_row)**2 + (c-center_col)**2 )
                mask[r,c] = 1 - (exp(-(freq_dist**2)/(cutoff*2)**2)) if r < cutoff else 1.0

        return mask

    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage)
        """
        
        from numpy import max, min
        
        max_value, min_value = max(image), min(image)
        # print(min_value, max_value)
        # print(image)
        min_value = 0 if min_value < 0 else min_value  
        _image = 255 * ( ( image - min_value )/ (max_value - min_value) )
        # print('next')
        # print(min(_image), max(_image))
        # print(_image)
        return 255 - _image.astype('uint8') 


    def filtering(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT        
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape, cutoff, order)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        take negative of the image to be able to view it (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8 
        """
        from numpy import fft
        import numpy as np

        _image_dft = fft.fft2(self.image)
        _image_dft = fft.fftshift(_image_dft)
        # dft = DFT.DFT()
        # plt.figure(1) 
        # plt.imshow(self.image)
        # plt.figure(2)
        # plt.imshow(20*np.log10(abs(_image_dft))) 
        # print(_image_dft)
        # print(abs(_image_dft))
        # plt.show()
        filter = self.filter(self.image.shape, self.cutoff, self.order) \
                 if self.filter_name.startswith('butterworth') \
                    else self.filter(self.image.shape, self.cutoff)
        
        _image_dft_filtered = _image_dft * filter
        _image_filtered = abs(fft.ifft2(_image_dft_filtered))
        
        return [ self.post_process_image(_image_filtered), \
                 self.post_process_image(20*np.log10(abs(_image_dft)+.00001)),   \
                 self.post_process_image(20*np.log10(abs(_image_dft_filtered)+.00001)) ]
    
# filtered image, magnitude of DFT, magnitude of filtered DFT        
