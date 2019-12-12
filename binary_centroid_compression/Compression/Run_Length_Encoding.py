import numpy as np

class rle:

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        run_length = [0] 
        run_length_counter = 0 
        toggle = binary_image[0,0]
        for r in range(0, binary_image.shape[0]):
            for c in range(0, binary_image.shape[1]):
                if (toggle ^ binary_image[r,c]):
                    run_length_counter += 1
                    run_length.append(0) 
                run_length[run_length_counter] +=  1 
                toggle = binary_image[r,c]
        return np.array(run_length)


    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        image = np.zeros((height, width))
        toggle = 255
        run_length_counter = 0 
        for r in range(0, image.shape[0]):
            for c in range(0, image.shape[1]):
                rle_code[run_length_counter] -= 1
                if rle_code[run_length_counter] == 0 :
                    toggle = 255 - toggle
                    run_length_counter += 1 
                image[r,c] = np.uint8(toggle)     
        return image
