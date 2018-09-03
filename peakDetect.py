import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
from scipy import ndimage


IMAGE_FOLDERPATH = './Q2/images/'

list_images = [image_file for image_file in os.listdir(IMAGE_FOLDERPATH) if not image_file.startswith('.')]
list_images.sort()

for i, image in enumerate(list_images):

    # noise reduction
    img = cv.imread(IMAGE_FOLDERPATH + image)
    img_to_display = (img / np.amax(img) * 255) .astype(np.uint8)

    denoise_img = cv.fastNlMeansDenoisingColored(img, None, 5, 5, 5, 15)
    denoise_norm_img = (denoise_img/np.amax(denoise_img)*255).astype(np.uint8)
    # plt.imshow(denoise_norm_img, cmap='gray')
    # plt.show()


    bw_img = cv.cvtColor(denoise_img, cv.COLOR_BGR2GRAY)
    max_val = np.amax(bw_img)
    norm_img = (bw_img/max_val*255).astype(np.uint8)

    # plt.imshow(denoise_img, cmap='gray')
    # plt.show()

    ret, thresh1 = cv.threshold(denoise_norm_img, 240, 250, cv.THRESH_BINARY)
    value = ndimage.measurements.center_of_mass(thresh1)
    x_center = int(round(value[1]))
    y_center = int(round(value[0]))
    # print(x_center, y_center)

    # plt.imshow(thresh1, cmap='gray')
    # plt.show()


    # Draw a diagonal blue line with thickness of 5 px
    image_with_mark = cv.line(thresh1, (x_center, y_center), (x_center, y_center), (0, 255, 0), 1)
    # plt.imshow(image_with_mark, cmap='gray')
    # plt.show()
    cv.imwrite('./Q2/images/image_' + str(i) + 'processed.jpg', image_with_mark)




