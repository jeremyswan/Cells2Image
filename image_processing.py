import numpy as np
from scipy import ndimage
from skimage.morphology import binary_dilation
from skimage import measure
from skimage import filters


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

def get_cell_mask(img,centroid,ptile=50,blur_sigma=11):
    M=np.abs(img-np.percentile(img.flatten(),ptile))
    M=ndimage.gaussian_filter(M,blur_sigma)
    thr = filters.threshold_otsu(M)
    M=M>thr
    L=measure.label(M)
    RP=measure.regionprops(L,intensity_image=img)
    return M,RP

def get_donut(center_mask):
    # takes a mask and returns the donut mask around it
    
    #generate circular mask for dilation
    r = 50
    y,x = np.ogrid[-r:r, -r:r]
    circle = x*x + y*y <= r*r
    
    # dilate and subtract
    total_mask = binary_dilation(center_mask,circle)
    donut_mask = total_mask - center_mask
    
    return donut_mask
