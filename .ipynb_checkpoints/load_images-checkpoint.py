import skimage.io
import numpy as np

prefix = '/media/brad/Seagate Backup Plus Drive/Malaria Images/Curated Images/'

images = { 'filename':'recording1.czi - recording1.czi #03.tif', 'rounded':69, 'egress':76  }

img = skimage.io.imread(''.join([prefix,'recording1.czi - recording1.czi #03.tif']))

print img.shape
