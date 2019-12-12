import numpy as np

class binary_image:
    def __init__(self):
        self.hist = [0]*256
        self.threshold = 0

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
     
        for r in range(0, image.shape[0]):
            for c in range(0, image.shape[1]):
                self.hist[image[r][c]] = self.hist[image[r][c]]+1
                
        return self.hist

    def expectation(self, hist):
        """ 
        takes a histogram, 
        performs normalization
        returns the expectant
        """
        
        norm_hist = [ count_value / sum(hist) for count_value in hist ]
        expectant = sum(( norm_hist[pixel_value] * pixel_value  for pixel_value in range(0, len(norm_hist)) ))

        return int(expectant)

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value""" 
          
        self.threshold = len(hist)//2
    
        expectant1 = [0,1]
        expectant2 = [0,1]

        while (expectant1[0]-expectant1[1]) is not 0 and (expectant2[0]-expectant2[1]) is not 0:
            lower_domain = hist[:self.threshold-1]
            upper_domain = hist[self.threshold-1:]

            expectant1 = [ self.expectation(lower_domain) , expectant1[0] ]
            expectant2 = [ self.expectation(upper_domain) , expectant2[0] ]

            self.threshold = (expectant1[0] + expectant2[0]) // 2
            print('threshold', self.threshold)
            print(expectant1[0], expectant2[0])
            
        return self.threshold

    def binarize(self, image):
        """Compute the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image

        'Assume that foreground objects are darker than background objects in the input gray-level image'

        the cells are lower intensities in the original image

        above threshold : set to 0   // black background - '0'
        below threshold : set to 255 // white blobs      - '1'
        """
        
        bin_img = image.copy()

        for r in range(0, image.shape[0]):
            for c in range(0, image.shape[1]):
                bin_img[r,c] = 0 if image[r][c] > self.threshold else 255

        return bin_img


