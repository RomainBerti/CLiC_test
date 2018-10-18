import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


IMAGE_INPUT_DIRECTORY = './Q1/images/'
NB_ROW = 9
NB_COL = 9

# list all the files in IMAGE_INPUT_DIRECTORY without hidden files
list_images = [image_file for image_file in os.listdir(IMAGE_INPUT_DIRECTORY) if not image_file.startswith('.')]
list_images.sort()

# initialization
amplitude_max = 0
# find the maximum over the batch of images
for filename in list_images:
    image = Image.open(IMAGE_INPUT_DIRECTORY + filename)
    image_array = np.array(image)
    amplitude = np.amax(image_array)
    if amplitude > amplitude_max:
        amplitude_max = amplitude

result = Image.new("RGB", (900, 900))

# I choose a final image size of 900x900 composed of 100x100 images
reconstructed_image = np.zeros((900, 900))
overlap = 24
small_image_size = 100
image_increment = round(small_image_size * overlap / 1024)

for it_image, filename in enumerate(list_images):
    path = os.path.expanduser(IMAGE_INPUT_DIRECTORY + filename)
    image = Image.open(path)
    # normalize image on 8bits (0-255)
    image = np.array(image)/amplitude_max * 255
    # resize image
    small_image = cv.resize(image, dsize=(small_image_size, small_image_size), interpolation=cv.INTER_LANCZOS4)
    x = (it_image // NB_COL) * (small_image_size - image_increment)  # floor division to go through the col
    y = (it_image % NB_ROW) * (small_image_size - image_increment)  # y is modulo of the width of the full image
    reconstructed_image[x:x+small_image_size, y:y+small_image_size] = small_image

plt.imshow(reconstructed_image, cmap='seismic')
plt.show()
cv.imwrite('./Q1_reconstructed_image.png', reconstructed_image)


