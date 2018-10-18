import numpy as np
import cv2 as cv
import os
from scipy import ndimage


IMAGE_FOLDERPATH = './Q2/images/'
list_images = [image_file for image_file in os.listdir(IMAGE_FOLDERPATH) if not image_file.startswith('.')]
list_images.sort()

RESULT_DIRECTORY = './Q2/results/'
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

GREEN_RGB = (0, 255, 0)
h = 5  # Parameter regulating filter strength
h_for_color_components = 5  # The same as h but for color components.
template_window_size = 5  # Size in pixels of the template patch that is used to compute weights.
search_window_size = 15  # Size in pixels of the window that is used to compute weighted average for given pixel

threshold = 240  # threshold value.
max_value = 255  # maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.

for it_image, filename in enumerate(list_images):

    # noise reduction
    image = cv.imread(IMAGE_FOLDERPATH + filename)
    denoised_image = cv.fastNlMeansDenoisingColored(image, None, h, h_for_color_components,
                                                   template_window_size, search_window_size)
    denoised_norm_image = (denoised_image / np.amax(denoised_image) * 255).astype(np.uint8)
    bw_image = cv.cvtColor(denoised_image, cv.COLOR_BGR2GRAY)

    ret, threshold_image = cv.threshold(denoised_norm_image, threshold, max_value, cv.THRESH_BINARY)
    value = ndimage.measurements.center_of_mass(threshold_image)
    x_center = int(round(value[1]))
    y_center = int(round(value[0]))

    # Draw a green point with thickness of 1 px
    marked_image = cv.line(threshold_image, (x_center, y_center), (x_center, y_center), GREEN_RGB, 1)
    # Write result
    cv.imwrite(RESULT_DIRECTORY + 'image_' + str(it_image) + '_processed.jpg', marked_image)
