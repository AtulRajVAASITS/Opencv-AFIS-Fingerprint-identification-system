import cv2 as cv
import numpy as np
import os

test_original = cv.imread("s.png",cv.IMREAD_GRAYSCALE)
cv.imshow("Original", cv.resize(test_original, None, fx=1, fy=1))
cv.waitKey(0)
cv.destroyAllWindows()

for file in [file for file in os.listdir("/home/jake/Downloads/d1")]:
    
    fingerprint_database_image = cv.imread("/home/jake/Downloads/d1/" + file)
    cv.imshow("Origi", fingerprint_database_image)
    sift = cv.SIFT_create()
    
    keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)
    
    matches = cv.FlannBasedMatcher(dict(algorithm=1, trees=10), 
          dict()).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []
   
    for p, q in matches:
        if p.distance < 0.1*q.distance:
            match_points.append(p)
         
    keypoints = 0
    if len(keypoints_1) <= len(keypoints_2):
        keypoints = len(keypoints_1)            
    else:
        keypoints = len(keypoints_2)

    if (len(match_points) / keypoints)>0.25:
        print("% match: ", len(match_points) / keypoints * 100)
        print("Figerprint ID: " + str(file)) 
        result = cv.drawMatches(test_original, keypoints_1, fingerprint_database_image,keypoints_2, match_points, None) 
        result = cv.resize(result, None, fx=1.5, fy=1.5)
        print(result)
        cv.imshow('result', result)
        cv.waitKey(0)
        break;
    
