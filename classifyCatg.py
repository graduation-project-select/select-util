
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

f = open("./fabric_labels.txt", 'r')
while True:
    line = f.readline().strip()
    if not line: break
    catgs.append(line)

f.close()


# for imagePath in imagePaths:
# 	catg = imagePath.split(os.path.sep)[-2].split("_")[-1]
# 	catgs.append(catg)

# catgs =list(set(catgs))
count = 0

for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	# fname = imagePath.split(os.path.sep)[-2].split("_")[-1]
	fname = imagePath.split(os.path.sep)[-2]
	if "abstract" in fname.lower(): continue
	attrs = fname.split("_") # 옷의 속성 태그들
	for attr in attrs:
		if attr.lower() in catgs:
			catg = attr.lower()
			print(catg)
			directory_name = 'img/' + catg
			path = directory_name + '/' + str(count) + '.jpg'
			count += 1
			if not(os.path.isdir(directory_name)):
				os.makedirs(os.path.join(directory_name))
			print(path)
			cv2.imwrite(path, image)
			break
