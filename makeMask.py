
import numpy as np
import scipy as sp
import cv2


def makeMask(img, pickColor):

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            b = image[i,j,0]
            g = image[i,j,1]
            r = image[i,j,2]
            if pickColor == 1:
                if  r > g and r > b and r > 100:
                    r = 225
                    g = 255
                    b = 255
                else:
                    r = 0
                    g = 0
                    b = 0
            elif pickColor == 2:
                if b > g and b > r and b > 100:
                    r = 225
                    g = 255
                    b = 255
                else:
                    r = 0
                    g = 0
                    b = 0
            elif pickColor == 3:
                if g > b and g > r and g > 100:#g > 120 and b < 120 and r < 120:
                    r = 225
                    g = 255
                    b = 255
                else:
                    r = 0
                    g = 0
                    b = 0
            else:
                print ("That is not a valid input.")

            savePicture(p, "maskImage.jpg")
            show(p)








