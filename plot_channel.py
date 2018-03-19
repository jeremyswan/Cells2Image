import matplotlib.pyplot as plt
import numpy as np

import load_images

allimg = load_images.allimages()


for image in allimg:
    img = image[0]
    print image[1]

    plt.plot([np.sum(img[i,0,:,:]) for i in range(img.shape[0])])
    plt.show()
