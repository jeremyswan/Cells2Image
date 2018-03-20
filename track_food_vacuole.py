import matplotlib.pyplot as plt
import numpy as np

from scipy import ndimage
import time


import image_data

#imggen = load_images.all_images()

def find_centroid(img):
    dark_thresh = np.percentile(img,0.25)
    mask = img < dark_thresh
    labels, numlabel = ndimage.label(mask)
    for l in range(numlabel+1):
        if np.sum(labels == l) < 300:
            labels[labels==l] = 0

    labels, numlabel = ndimage.label(labels)
    com = ndimage.measurements.center_of_mass(np.ones(labels.shape),labels,numlabel)
    return com, labels, numlabel

if __name__ == '__main__':
    for i in range(10):
        current_image = image_data.fetch_random_image()
        com, labels, numlabel = find_centroid(current_image[1,:,:])

        #com = ndimage.measurements.center_of_mass(np.ones(labels.shape),labels,numlabel)
        print com


        plt.imshow(labels)
        plt.show()
    #
    # for image in imggen:
    #     img = image[0]
    #     print image[1]
    #
    #     for timepoint in range(img.shape[0]):
    #         current_image = img[timepoint,:,:,:].squeeze()
    #
    #         labels, numlabel = find_centroid(current_image[1,:,:])
    #
    #         com = ndimage.measurements.center_of_mass(np.ones(labels.shape),labels,numlabel)
    #         print timepoint, com
    #         #find com of all labels
    #         #pick closest to center
    #
    #         plt.imshow(labels)

            #plt.plot([np.sum(img[i,0,:,:]) for i in range(img.shape[0])])
    #        plt.show()
