import os
import cv2

def matchFP(folder_path,Sfile):
    sample = cv2.imread("C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\voting_app"+ folder_path + "\\" + Sfile)
    best_score = 0
    filename= None 
    image = None
    kp1, kp2, mp = None,None,None
    for file in [file for file in os.listdir("C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\voting_app"+ folder_path)][:44]:
        if file == 'secure_vote.bmp':
            continue
        fingerprint_image = cv2.imread("C:\\Users\\shikh\\OneDrive\\Desktop\\hiluuu\\" + folder_path + "\\" + file)
        sift = cv2.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(sample,None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image,None)
        matches = cv2.FlannBasedMatcher({'algorithm': 1, "trees": 10} , {}).knnMatch(descriptors_1,descriptors_2,k=2)
        match_points=[]
        for p,q in matches:
            if p.distance <  0.6 * q.distance:
                match_points.append(p)
        keypoints = 0
        if len(keypoints_1) <len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)
        print(match_points)
        if len(match_points)/ keypoints * 100 > best_score:
            best_score = len(match_points) / keypoints * 100
            filename = file 
            image = fingerprint_image
            kp1,kp2,mp = keypoints_1,keypoints_2,match_points
    print("best match :"+ str(filename))
    print("score : " + str(best_score))
    result = cv2.drawMatches(sample,kp1,image,kp2,mp,None)
    cv2.imwrite("matches_result.jpg", result)
    cv2.imshow("result",result)
    return best_score
