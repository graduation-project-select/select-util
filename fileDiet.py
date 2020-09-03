
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import random
import pickle
import cv2
import os
# 데이터 개수 카테고리별로 200개씩 만 남기기

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset (i.e., directory of images)")
args = vars(ap.parse_args())

imagePaths = sorted(list(paths.list_images(args["dataset"])))
IMAGE_DIMS = (96, 96, 3)

catgs = []

# f = open("./fabric_labels.txt", 'r')
# while True:
#     line = f.readline().strip()
#     if not line: break
#     catgs.append(line)

# f.close()



# for imagePath in imagePaths:
# 	catg = imagePath.split(os.path.sep)[-2].split("_")[-1]
# 	catgs.append(catg)

# catgs =list(set(catgs))
count = 0
prevFname = ""

for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	# fname = imagePath.split(os.path.sep)[-2].split("_")[-1]
	catg = imagePath.split(os.path.sep)[-2]
	if prevFname != catg:
		prevFname = catg
		count = 0
	elif count < 200:
		directory_name = 'img/' + catg
		path = directory_name + '/' + str(count) + '.jpg'
		if not(os.path.isdir(directory_name)):
			os.makedirs(os.path.join(directory_name))
		cv2.imwrite(path, image)
	count += 1
	print(str(count) + ": " + imagePath)

    
