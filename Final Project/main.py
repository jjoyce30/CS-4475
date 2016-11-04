# Sydni Perterson and Jackie Joyce
# CS 4475 Final Project - Selective Color Transfer
# python example.py --source images/ocean_sunset.jpg --target images/ocean_day.jpg

# import the necessary packages
from color_transfer import color_transfer
import imageBlend
#import makeMask
import numpy as np
import argparse
import cv2
import math

# load the images
source = cv2.imread("images/source.jpg")
target = cv2.imread("images/flower.jpg")

# transfer the color distribution from the source image
# to the target image
transfer = color_transfer(source, target)
cv2.imwrite("output/imageSet2/transfer.jpg", transfer)

#pickColor = 1 #input("Type 1 for red. \n Type 2 for blue. \n Type 3 for green.")
#makeMask.makeMask(pickColor)
mask = cv2.imread("images/maskImage.jpg")

def run_blend(black_image, white_image, mask):
  """ This function administrates the blending of the two images according to 
  mask.

  Assume all images are float dtype, and return a float dtype.
  """

  # Automatically figure out the size
  min_size = min(black_image.shape)
  depth = int(math.floor(math.log(min_size, 2))) - 4 # at least 16x16 at the highest level.

  gauss_pyr_mask = imageBlend.gaussPyramid(mask, depth)
  gauss_pyr_black = imageBlend.gaussPyramid(black_image, depth)
  gauss_pyr_white = imageBlend.gaussPyramid(white_image, depth)


  lapl_pyr_black  = imageBlend.laplPyramid(gauss_pyr_black)
  lapl_pyr_white = imageBlend.laplPyramid(gauss_pyr_white)

  outpyr = imageBlend.blend(lapl_pyr_white, lapl_pyr_black, gauss_pyr_mask)
  outimg = imageBlend.collapse(outpyr)

  outimg[outimg < 0] = 0 # blending sometimes results in slightly out of bound numbers.
  outimg[outimg > 255] = 255
  outimg = outimg.astype(np.uint8)

  return lapl_pyr_black, lapl_pyr_white, gauss_pyr_black, gauss_pyr_white, \
      gauss_pyr_mask, outpyr, outimg

def viz_gauss_pyramid(pyramid):
  """ This function creates a single image out of the given pyramid.
  """
  height = pyramid[0].shape[0]
  width = pyramid[0].shape[1]

  out = np.zeros((height*len(pyramid), width), dtype = float)

  for idx, layer in enumerate(pyramid):
    if layer.max() <= 1:
      layer = layer.copy() * 255

    out[(idx*height):((idx+1)*height),:] = cv2.resize(layer, (width, height), 
        interpolation = 3)

  return out.astype(np.uint8)

def viz_lapl_pyramid(pyramid):
  """ This function creates a single image out of the given pyramid.
  """
  height = pyramid[0].shape[0]
  width = pyramid[0].shape[1]

  out = np.zeros((height*len(pyramid), width), dtype = np.uint8)

  for idx, layer in enumerate(pyramid[:-1]):
     # We use 3 for interpolation which is cv2.INTER_AREA. Using a value is
     # safer for compatibility issues in different versions of OpenCV.
     patch = cv2.resize(layer, (width, height),
         interpolation = 3).astype(float)
     # scale patch to 0:256 range.
     patch = 128 + 127*patch/(np.abs(patch).max())

     out[(idx*height):((idx+1)*height),:] = patch.astype(np.uint8)

  #special case for the last layer, which is simply the remaining image.
  patch = cv2.resize(pyramid[-1], (width, height), 
      interpolation = 3)
  out[((len(pyramid)-1)*height):(len(pyramid)*height),:] = patch

  return out


black_img = cv2.imread("images/source.jpg")
white_img = cv2.imread("output/imageSet2/transfer.jpg")
mask_img = cv2.imread("output/imageSet2/mask.jpg")

black_img = black_img.astype(float)
white_img = white_img.astype(float)
mask_img = mask_img.astype(float) / 255

print "Applying blending."
lapl_pyr_black_layers = []
lapl_pyr_white_layers = []
gauss_pyr_black_layers = []
gauss_pyr_white_layers = []
gauss_pyr_mask_layers = []
out_pyr_layers = []
out_layers = []

for channel in range(3):
  lapl_pyr_black, lapl_pyr_white, gauss_pyr_black, gauss_pyr_white, gauss_pyr_mask,\
      outpyr, outimg = run_blend(black_img[:,:,channel], white_img[:,:,channel], \
                       mask_img[:,:,channel])
  
  lapl_pyr_black_layers.append(viz_lapl_pyramid(lapl_pyr_black))
  lapl_pyr_white_layers.append(viz_lapl_pyramid(lapl_pyr_white))
  gauss_pyr_black_layers.append(viz_gauss_pyramid(gauss_pyr_black))
  gauss_pyr_white_layers.append(viz_gauss_pyramid(gauss_pyr_white))
  gauss_pyr_mask_layers.append(viz_gauss_pyramid(gauss_pyr_mask))
  out_pyr_layers.append(viz_lapl_pyramid(outpyr))
  out_layers.append(outimg)

lapl_pyr_black_img = cv2.merge(lapl_pyr_black_layers)
lapl_pyr_white_img = cv2.merge(lapl_pyr_white_layers)
gauss_pyr_black_img = cv2.merge(gauss_pyr_black_layers)
gauss_pyr_white_img = cv2.merge(gauss_pyr_white_layers)
gauss_pyr_mask_img = cv2.merge(gauss_pyr_mask_layers)
outpyr = cv2.merge(out_pyr_layers)
outimg = cv2.merge(out_layers)

cv2.imwrite("output/imageSet2/lapl_pyr_black_img.jpg", lapl_pyr_black_img)
cv2.imwrite("output/imageSet2/lapl_pyr_white_img.jpg", lapl_pyr_white_img)
cv2.imwrite("output/imageSet2/gauss_pyr_black_img.jpg", gauss_pyr_black_img)
cv2.imwrite("output/imageSet2/gauss_pyr_white_img.jpg", gauss_pyr_white_img)
cv2.imwrite("output/imageSet2/gauss_pyr_mask_img.jpg", gauss_pyr_mask_img)
cv2.imwrite("output/imageSet2/outpyr.jpg", outpyr)
cv2.imwrite("output/imageSet2/outimg.jpg", outimg)


