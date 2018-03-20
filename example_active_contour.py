import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import active_contour
from skimage.filters import gaussian

import load_images
prefix = '../Curated Images/'
images = load_images.images

movie = skimage.io.imread(''.join([prefix,images[0]['filename']]))
img=movie[1,1,:,:]

# initial snake
centr=np.array([250,250])
rad=100
theta=np.linspace(0,2*np.pi,50)
si=np.array([centr[0]+rad*np.sin(theta), centr[1]+rad*np.cos(theta)]).T

s=active_contour(img,si,alpha=0.01,beta=0.01,w_line=1,max_iterations=5000,convergence=0.1)
plt.imshow(img,cmap='gray')
plt.plot(si[:,0],si[:,1])
plt.plot(s[:,0],s[:,1])

plt.show()