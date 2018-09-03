from __future__ import print_function
import os
from PIL import Image
# import PIL
import os
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
import matplotlib
from matplotlib import pyplot
import scipy


IMAGE_FOLDERPATH = './Q1/images/'
NB_ROW = 3
NB_COL = 3

list_images = [f for f in os.listdir(IMAGE_FOLDERPATH) if not f.startswith('.')]
list_images.sort()

image_finale = []
it_image = 1
amp_max = 0
amp_min = 0

# find the maximum over the batch of images
for file in list_images:
    im = Image.open(IMAGE_FOLDERPATH + file)
    X = np.array(im)
    if np.amax(X) > amp_max:
        amp_max = np.amax(X)

# print(amp_max) = 1560

# img = cv2.imread(IMAGE_FOLDERPATH + list_images[1])
# # Display Image
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#overlap is 307
for row in range(1,9):
    for col in range(1, 9):
        # im = mpimg.imread(IMAGE_FOLDERPATH + list_images[it_image])
        # plt.imshow(im)
        #
        # image_finale[1+1024*(col-1):1024*col][ 1024+1014*(row-1) : 1024*row] = numpy.array(im)
        # it_image +=1
        continue



# # # # X = np.random.random((100, 100)) # sample 2D array
# im = Image.open(IMAGE_FOLDERPATH + list_images[1])
# im = (im).astype('uint8')
#
# plt.imshow(im, cmap='jet')
# plt.show()
# print(im.size)
# print(im.mode)
# im = im.convert('RGB')
#
# print(im.mode)
# # X = np.fliplr(np.flipud(np.array(im)))
# im = im.resize((128, 128), Image.ANTIALIAS)
# print(im.size)
# # X = np.array(im)
#
# plt.imshow(im, cmap='jet')
# plt.show()

# im = Image.open(IMAGE_FOLDERPATH + list_images[1])
# img = np.array(im)
# res = cv2.resize(img, dsize=(128, 128), interpolation=cv2.INTER_LANCZOS4)
# plt.imshow(res, cmap='gray')
# plt.show()

files = list_images

result = Image.new("RGB", (900, 900))
X_data = []
final = []
tableau = np.zeros((900,900))


#for index, file in enumerate(files):
for i in range(0,81):
    path = os.path.expanduser(IMAGE_FOLDERPATH + list_images[i])
    img = Image.open(path)
    img = np.array(img)/amp_max*255
    X_data = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_LANCZOS4)
    # I suppose that the camera goes from left to right and up to down (not in a Z way)
    x = i // 9 * 98
    y = i % 9 * 98
    # print(x,y)
    # print(tableau[x:x+100,y:y+100].shape)
    # print(X_data.shape)
    tableau[x:x+100,y:y+100] = X_data
    # plt.imshow(X_data, cmap='gray')
    # plt.show()
    # final = np.vstack((tableau, X_data))
  # res.thumbnail((400, 400), Image.ANTIALIAS)
  # x = index // 2 * 400
  # y = index % 2 * 400
  # w, h = 128, 128
  # print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  # result.paste(img, (x, y, x + w, y + h))

# result.save(os.path.expanduser('./image.jpg'))
# print(X_data)
# print(tableau.shape)
plt.imshow(tableau, cmap='seismic')
plt.show()
cv2.imwrite('./test.png', tableau)


