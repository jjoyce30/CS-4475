# ASSIGNMENT 5
# JAckie Joyce

import cv2
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

img = cv2.imread('flower_gray.jpg',0)
edges = cv2.Canny(img,100,200)

cv2.imwrite('edges 2.jpg', edges)

