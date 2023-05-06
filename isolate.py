import cv2 as cv
import numpy as np

import glob

input_folder_path =  "./PrePro/output"
output_folder_path = "./PrePro/output2"

def chk_area(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) <= 0:
        return False
    
    cv.drawContours(img, contours, -1, (0, 255, 0), 2)
    area = np.max(np.array([cv.contourArea(x) for x in contours]))

    if area > 1.0:
        return img
    else :
        return np.empty_like(img)
    
def defect_valid(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) <= 0:
        return False
    area = np.max(np.array([cv.contourArea(x) for x in contours]))
    
    if area > 1.0:
        return True
    else :
        return False

for filename in glob.glob(input_folder_path + '/*.png'):
    img = cv.imread(filename, cv.IMREAD_UNCHANGED)
    
    defect_valid(img)
    img = chk_area(img)
    

    cv.imshow("image", img)
    cv.waitKey(0)

    
                              
    

