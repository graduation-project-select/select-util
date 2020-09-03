
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import random
import pickle
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset (i.e., directory of images)")
args = vars(ap.parse_args())

imagePaths = sorted(list(paths.list_images(args["dataset"])))
IMAGE_DIMS = (96, 96, 3)

catgs = []

for imagePath in imagePaths:
	catg = imagePath.split(os.path.sep)[-2].split("_")[-1]
	catgs.append(catg)

catgs =list(set(catgs))
count = 0

for imagePath in imagePaths:
	count = count + 1
	image = cv2.imread(imagePath)
	print(imagePath)
	fname = imagePath.split(os.path.sep)[-2].split("_")[-1]
	for catg in catgs:
		if fname == catg:
			directory_name = 'img/' + catg
			path = directory_name + '/' + str(count) + '.jpg'
			if not(os.path.isdir(directory_name)):
				os.makedirs(os.path.join(directory_name))
			print(path)
			cv2.imwrite(path, image)


