from myro import *
def makeMask(pickColor):
    p = makePicture(pickAFile())
    for i in getPixels(p):
		r = getRed(i)
		g = getGreen(i)
		b = getBlue(i)
		if pickColor == 1:
			if  r > g and r > b and r > 100:
				setRed(i, 255)
				setGreen(i, 255)
				setBlue(i, 255)
			else:
				setRed(i, 0)
                setGreen(i, 0)
                setBlue(i, 0)
		if pickColor == 2:
			if b > g and b > r and b > 100:
				setRed(i, 255)
				setGreen(i, 255)
				setBlue(i, 255)
			else:
				setRed(i, 0)
				setGreen(i, 0)
				setBlue(i, 0)
		if pickColor == 3:
			if g > b and g > r and g > 100:#g > 120 and b < 120 and r < 120:
				setRed(i, 255)
				setGreen(i, 255)
				setBlue(i, 255)
			else:
				setRed(i, 0)
				setGreen(i, 0)
				setBlue(i, 0)
		else:
			print ("That is not a valid input.")

    savePicture(p, "output/imageSet2/mask.jpg")
    show(p)








