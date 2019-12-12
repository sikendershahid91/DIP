import cv2
import numpy as np

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 5 pixel cross window assigns region names
        takes a input:
        image: binary image
        return: a list of regions"""
        
        regions = dict()

        conv_mask = np.array([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]])
        
        new_region_mask = np.array([
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 0]])

        end_region_mask = np.array([
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]])
        
        padded_image = np.zeros( (image.shape[0] +2 ,image.shape[1] +2) )
        padded_image[1:image.shape[0]+1, 1:image.shape[1]+1] = image > 128
     
        region_color = 0
        temporary_storage = []
        for r in range(0, image.shape[0]+2):
             for c in range(0, image.shape[1]+2):
                 
                 if padded_image[r,c] == 1:
                     extracted_region = (padded_image[r-1:(r+1)+1,c-1:(c+1)+1] == 1) & conv_mask
                     temporary_storage.append((r,c))
                     
                     if np.all( extracted_region == new_region_mask ):
                         regions[len(regions.keys())+1] = []
                         region_color = len(regions.keys())

                     for previous_region in reversed(list(regions.keys())):
                         if ((r-1, c  ) in regions[previous_region]):
                             region_color = previous_region
                             break
                         
                     if np.all( extracted_region == end_region_mask ):
                         regions[region_color].extend(temporary_storage)
                         
                     # if padded_image[r, c+1] == 0 and padded_image[r+1, c] == 0:
                     #     regions[region_color].extend(temporary_storage)

                 else:
                     if temporary_storage:
                         regions[region_color].extend(temporary_storage)
                     temporary_storage = []
                     
        for keys in list(regions.keys()):
            if len(regions[keys]) < 15:
                del regions[keys]
        
        return regions

    
    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>

        def center(list_of_tuples):
            y, x = zip(*list_of_tuples)
            return (sum(y)//len(y), sum(x)//len(x))

        def median_center(list_of_tuples):
            y, x = zip(*list_of_tuples)
            return (sorted(y)[len(y)//2], sorted(x)[len(x)//2])

        print('region', '\t:', 'center', '\t,', 'area')
        stats = []
        for region_number in region.keys():
            regions = region[region_number]
            stats.append( (region_number, center(regions) , len(regions)) )
            print(region_number, '\t:', center(regions) ,'\t,',len(regions))
        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        # (r,c) --> (y,x) -->need to swap--> (x,y) 
        list_of_centroids = list(( (x[1][1],x[1][0]) for x in stats))
        list_of_region_numbers = list( x[0] for x in stats ) 
        list_of_area= list(( x[2] for x in stats))
        
        import matplotlib.pyplot as plt
        fig = plt.figure()
        plt.imshow(image, cmap='binary')
        plt.scatter(*zip(*list_of_centroids),color='red', marker='*')

        for i, region_number in enumerate(list_of_region_numbers):
            plt.annotate(str(region_number) + ', ' + str(list_of_area[i]) , list_of_centroids[i], color='green')
    
        fig.canvas.draw()
        ncols, nrows = fig.canvas.get_width_height()
        return np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(nrows, ncols, 3)
