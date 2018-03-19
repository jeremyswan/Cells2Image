import matplotlib.pyplot as plt
import numpy as np

import load_images

imggen = load_images.all_images()


for image in imggen:
    img = image[0]
    print image[1]

    plt.plot([np.sum(img[i,0,:,:]) for i in range(img.shape[0])])
    plt.show()
