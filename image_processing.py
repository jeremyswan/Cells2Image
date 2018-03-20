import numpy as np
from scipy import ndimage



def find_food_vacuole_centroid(frame):
    dark_thresh = np.percentile(frame,0.25)
    mask = frame < dark_thresh
    labels, numlabel = ndimage.label(mask)
    for l in range(numlabel+1):
        if np.sum(labels == l) < 300:
            labels[labels==l] = 0
    labels, numlabel = ndimage.label(labels)
    com = ndimage.measurements.center_of_mass(np.ones(labels.shape),labels,numlabel)
    return com, labels, numlabel
