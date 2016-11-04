# ASSIGNMENT 5
# Jackie Joyce

import cv2
import numpy as np
import scipy as sp

""" Assignment 5 - Detecting Gradients / Edges

This file has a number of functions that you need to fill out in order to
complete the assignment. Please write the appropriate code, following the
instructions on which functions you may or may not use.

GENERAL RULES:
    1. DO NOT INCLUDE code that saves, shows, displays, writes the image that
    you are being passed in. Do that on your own if you need to save the images
    but the functions should NOT save the image to file. (This is a problem
    for us when grading because running 200 files results a lot of images being
    saved to file and opened in dialogs, which is not ideal). Thanks.

    2. DO NOT import any other libraries aside from the three libraries that we
    provide. You may not import anything else, you should be able to complete
    the assignment with the given libraries (and in most cases without them).

    3. DO NOT change the format of this file. Do not put functions into classes,
    or your own infrastructure. This makes grading very difficult for us. Please
    only write code in the allotted region.
"""

def imageGradientX(image):
    """ This function differentiates an image in the X direction.

    Note: See lectures 02-06 (Differentiating an image in X and Y) for a good
    explanation of how to perform this operation.

    The X direction means that you are subtracting columns:
    der. F(x, y) = F(x+1, y) - F(x, y)

    You should compute the absolute value of the differences in order to avoid
    setting a pixel to a negative value which would not make sense.

    We want you to iterate the image to complete this function. You may NOT use
    any functions that automatically do this for you.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The image gradient in the X direction.
    """
    # WRITE YOUR CODE HERE.
    w, h = image.shape
    for y in range (h - 1):
        for x in range (w):
            image[x, y] = abs(image[x, y + 1] - image[x, y])
            
        
    #cv2.imwrite('check.jpg', image)
    return (image)



    # END OF FUNCTION.

def imageGradientY(image):
    """ This function differentiates an image in the Y direction.

    Note: See lectures 02-06 (Differentiating an image in X and Y) for a good
    explanation of how to perform this operation.

    The X direction means that you are subtracting columns:
    der. F(x, y) = F(x, y+1) - F(x, y)

    You should compute the absolute value of the differences in order to avoid
    setting a pixel to a negative value which would not make sense.

    We want you to iterate the image to complete this function. You may NOT use
    any functions that automatically do this for you.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The image gradient in the Y direction.
    """
    # WRITE YOUR CODE HERE.

    w, h = image.shape
    for y in range (h):
        for x in range (w - 1):
            image[x, y] = abs(image[x + 1, y] - image[x, y])
    
    
    #cv2.imwrite('check_y.jpg', image)
    return (image)


    # END OF FUNCTION.

def computeGradient(image, kernel):
    """ This function applies an input 3x3 kernel to the image, and outputs the
    result. This is the first step in edge detection which we discussed in
    lecture.

    You may assume the kernel is a 3 x 3 matrix.
    View lectures 2-05, 2-06 and 2-07 to review this concept.

    The process is this: At each pixel, perform cross-correlation using the
    given kernel. Do this for every pixel, and return the output image.

    The most common question we get for this assignment is what do you do at
    image[i, j] when the kernel goes outside the bounds of the image. You are
    allowed to start iterating the image at image[1, 1] (instead of 0, 0) and
    end iterating at the width - 1, and column - 1.

    Args:
        image (numpy.ndarray): A grayscale image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The computed gradient for the input image.
    """
    # WRITE YOUR CODE HERE.
    w, h = image.shape

    for y in range(h - 1):
        for x in range(w - 1):
            a = image[x-1, y +1] * kernel[0,2]
            b = image[x, y +1] * kernel[1,2]
            c = image[x+1, y +1] * kernel[2,2]
            d = image[x-1, y] * kernel[0,1]
            e = image[x, y] * kernel[1,1]
            f = image[x+1, y] * kernel[2,1]
            g = image[x-1, y -1] * kernel[0,0]
            h = image[x, y -1] * kernel[1,0]
            i = image[x+1, y -1] * kernel[2,0]
            image [x,y] = (a+b+c+d+e+f+g+h+i)
            
    #cv2.imwrite('flower_blur.jpg', image)
    return (image)


    # END OF FUNCTION.