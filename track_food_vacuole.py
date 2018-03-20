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

        print com

        plt.imshow(labels)
        plt.show()
