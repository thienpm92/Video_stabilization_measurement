#import cython_ITF
import numpy as np 
import cv2
import math
from measurement import *

save_path = './dst/'
#input_path = '/media/vipl/DATA/Dataset/video_stab/DeepStab-dataset/unstable/56.avi'
input_path = '/home/vipl/Eric/video_stabilization/PWStableNet/56_pwstabnet.avi'
vid = cv2.VideoCapture(input_path)
Nframe = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
imgSize=(640,480)


for idx in range(Nframe-1):
    checkFrame,curFrame = vid.read()
    if not checkFrame:
        break
    curFrame = cv2.resize(curFrame,imgSize)
    storage = save_path + str(idx) + '.png'
    cv2.imwrite(storage, curFrame) 



