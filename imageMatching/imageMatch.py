import cv2
import random
import os

inputImage = cv2.imread("input.jpg")
compare = []
match = []

root_path = "example/"
imagePaths = os.listdir(root_path)
for imagePath in imagePaths:
    compare.append(root_path + imagePath)

print(compare)

for c in compare:
    compareImage = cv2.imread(c)
    sift = cv2.xfeatures2d.SIFT_create()
    kp, kd = sift.detectAndCompute(inputImage, None)
    c_kp, c_kd = sift.detectAndCompute(compareImage, None)
    bfMatcher = cv2.BFMatcher()
    matchList = bfMatcher.knnMatch(kd, c_kd, k=2)
    goodList = []
    for m, n in matchList:
        if m.distance < 0.6 * n.distance:
            goodList.append([m])
    match.append(len(goodList))
    print(len(goodList))

outputImage = cv2.imread(compare[match.index(max(match))])
cv2.imshow("outputImage", outputImage)
cv2.waitKey(0)

# grayscaleImageNDArray = cv2.cvtColor(imageNDArray, cv2.COLOR_BGR2GRAY)
# rotateGrayscaleImagenDArray = cv2.cvtColor(rotateImageNDArray, cv2.COLOR_BGR2GRAY)

# sift = cv2.SIFT()

# random.shuffle(goodList)  # 비교한 특징점들 중에서 일부만 골고루 표시하기 위해 섞는다.
# matchImageNDArray = cv2.drawMatchesKnn(inputImage, kp, compareImage, c_kp, goodList, flags=2, outImg=None)