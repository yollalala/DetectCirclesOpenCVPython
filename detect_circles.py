import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--image", required = True, 
	help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200, 
	param1=100, param2=50, minRadius=50, maxRadius=150)

if circles is not None:
	circles = np.round(circles[0, :]).astype("int")

	for (x, y, r) in circles:
		cv2.circle(output, (x, y), r, (255, 255, 0), 2)
		cv2.rectangle(output, (x-2, y-2), (x+2, y+2), (0, 128, 255), -1)

	cv2.imshow("output", output)
	cv2.waitKey(0)
