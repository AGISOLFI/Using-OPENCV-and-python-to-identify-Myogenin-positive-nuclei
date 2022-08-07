########################
# Myogenin Positive Nuclei
# Versison: xxxx
#########################

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Db 5 Revised.tiff")
(Blue_img, Green_img, Red_img) = cv2.split(img)
#use the following to show the different channels:
# cv2.imshow("Red", Red_img)
# cv2.imshow("Green", Green_img)
# cv2.imshow("Blue", Blue_img)

#Counting the DAPI stained nuclei
#################################

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 30
params.maxThreshold = 255
params.thresholdStep=.1

# Filter by Area.
params.filterByArea = True
params.minArea = 2

#filter by color
params.filterByColor=1
params.blobColor=255

#filter by circulatrity
filterByCircularity = 1
params.minCircularity=0
params.maxCircularity=1

#filter by convexity
filterByConvexity=1
params.minConvexity=0
params.maxConvexity=1

#filter by Inerta Ratio
params.filterByInertia = True
params.minInertiaRatio = 0
params.maxInertiaRatio = 1

# Create a detector with the parameters

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(Blue_img)

# Create an Image with keypoints circled
nuc_with_keypoints = cv2.drawKeypoints(Blue_img, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
nuclei=len(keypoints)-1 #minus one because of scale bar

	# Show keypoints
plt.title('Nuclei Detection')
plt.imshow(nuc_with_keypoints)


#Overlay Analysis
######################################
height, width = Blue_img.shape
overlay_channel = np.zeros((height,width,3), np.uint8)


for i in range (height): #traverses through height of the image
    for j in range (width): #traverses through width of the image
        if Blue_img[i,j]>10 and Red_img[i,j]>10: #If the pixel contains both read and blue:
          overlay_channel[i,j]= (255,255,255) #make a white pixel on the new img in the same spot

#use the following line to display the new overlay image:
cv2.imshow('Binary',overlay_channel)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255
params.thresholdStep=.1

# Filter by Area.
params.filterByArea = True
params.minArea = 1

#filter by color
params.filterByColor=1
params.blobColor=255

#filter by circulatrity
filterByCircularity = 1
params.minCircularity=0
params.maxCircularity=1

#filter by convexity
filterByConvexity=1
params.minConvexity=0
params.maxConvexity=1

#filter by Inerta Ratio
params.filterByInertia = True
params.minInertiaRatio = 0
params.maxInertiaRatio = 1

# Create a detector with the parameters

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(overlay_channel)
# Create an Image with keypoints circled
myo_with_keypoints = cv2.drawKeypoints(overlay_channel, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
myogenic_nuclei=len(keypoints)-1 #minus one because of scale bar

plt.show() #shows the nuclei detection graph

	# Show keypoints
plt.title('Myogenic Nuclei')
plt.imshow(myo_with_keypoints)


print('# of Nuclei: ',nuclei) 
print('# of Myogenic Nuclei: ', myogenic_nuclei) 
print('Percent of overlap: ', (myogenic_nuclei/nuclei)*100)

plt.show()# Shows the myogenic nuclei graph