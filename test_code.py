#import cython_ITF
import numpy as np 
import cv2
import math
from measurement import *

# def ITF_WMR_score(input_path):
#     vid = cv2.VideoCapture(input_path)
#     Nframe = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
#     ITF = 0
#     _,prevFrame = vid.read()
#     prevFrame = cv2.resize(prevFrame,(640,360))
#     for idx in range(Nframe-1):
#         checkFrame,curFrame = vid.read()
#         curFrame = cv2.resize(curFrame,(640,360))
#         if not checkFrame:
#             break
#         img1 = cv2.cvtColor(prevFrame,cv2.COLOR_BGR2GRAY)
#         img2 = cv2.cvtColor(curFrame,cv2.COLOR_BGR2GRAY)
#         psnr = cython_ITF.PSNR_cython(img1,img2)
#         ITF += psnr
#         prevFrame = curFrame.copy()
#     ITF = ITF/(Nframe-1)
#     return ITF


# src_path = '/media/vipl/DATA/Dataset/video/DeepStab/unstable/56.avi'
# dst_path = '/home/vipl/Eric/video_stabilization/PWStableNet/56_pwstabnet.avi'
# itf_wmr_score = ITF_WMR_score(dst_path)
# print(itf_wmr_score)


# src_path = '/media/vipl/DATA/Dataset/video_stab/DeepStab-dataset/unstable/56.avi'
# dst_path = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_pwstabnet.avi'
# stab_score_1 = stability_score_1(dst_path)
# stab_score_2 = stability_score_2(dst_path)
# itf_score = ITF_score(dst_path)
# itf_wmr_score = ITF_WMR_score(dst_path)
#crop_ratio,distortion_ratio = distortion_cropping(src_path,dst_path)
# print('stab_score_1',stab_score_1)
# print('stab_score_2',stab_score_2)
#print('stab_score',round(stab_score,2),'  ','itf_score',round(itf_score,2),'  ','itf_wmr_score',round(itf_wmr_score,2))
# print('crop',round(crop_ratio,2),'  ','distortion_ratio',round(distortion_ratio,2))
# res = [itf_score,itf_wmr_score,stab_score,crop_ratio[2],distortion_ratio[0]]
# print(itf_score,' ',itf_wmr_score,' ',stab_score,' ',crop_ratio[2],' ',distortion_ratio[0])
# file1 = open("MyFile.txt","a")
# file1.write(res)

src_path = '/media/vipl/DATA/Dataset/video_stab/data_test/pax_5_origin.avi'

dst_path1 = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_adobe.avi'
dst_path2 = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_realtime.avi'
dst_path3 = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_youtube.avi'
dst_path4 = '/media/vipl/DATA/Dataset/video_stab/result/bundle_pax_5.avi'
dst_path5 = '/media/vipl/DATA/Dataset/video_stab/result/meshflow_pax_5.avi'
dst_path6 = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_pwstabnet.avi'
dst_path7 = '/media/vipl/DATA/Dataset/video_stab/result/pax_5_thesis.avi'


stab_score_0 = stability_score_1(src_path)
stab_score_1 = stability_score_1(dst_path1)
stab_score_2 = stability_score_1(dst_path2)
stab_score_3 = stability_score_1(dst_path3)
stab_score_4 = stability_score_1(dst_path4)
stab_score_5 = stability_score_1(dst_path5)
stab_score_6 = stability_score_1(dst_path6)
stab_score_7 = stability_score_1(dst_path7)
print('stab_score_1',round(stab_score_0,2))
print('stab_score_1',round(stab_score_1,2))
print('stab_score_1',round(stab_score_2,2))
print('stab_score_1',round(stab_score_3,2))
print('stab_score_1',round(stab_score_4,2))
print('stab_score_1',round(stab_score_5,2))
print('stab_score_1',round(stab_score_6,2))
print('stab_score_1',round(stab_score_7,2))
print('')

mean_crop1, min_distor1 = distortion_cropping(src_path,dst_path1)
mean_crop2, min_distor2 = distortion_cropping(src_path,dst_path2)
mean_crop3, min_distor3 = distortion_cropping(src_path,dst_path3)
mean_crop4, min_distor4 = distortion_cropping(src_path,dst_path4)
mean_crop5, min_distor5 = distortion_cropping(src_path,dst_path5)
mean_crop6, min_distor6 = distortion_cropping(src_path,dst_path6)
mean_crop7, min_distor7 = distortion_cropping(src_path,dst_path7)

print('mean_crop',round(mean_crop1,2))
print('mean_crop',round(mean_crop2,2))
print('mean_crop',round(mean_crop3,2))
print('mean_crop',round(mean_crop4,2))
print('mean_crop',round(mean_crop5,2))
print('mean_crop',round(mean_crop6,2))
print('mean_crop',round(mean_crop7,2))
print('')
print('min_distor',round(min_distor1,2))
print('min_distor',round(min_distor2,2))
print('min_distor',round(min_distor3,2))
print('min_distor',round(min_distor4,2))
print('min_distor',round(min_distor5,2))
print('min_distor',round(min_distor6,2))
print('min_distor',round(min_distor7,2))
print('')
itf_score0 = ITF_score(src_path)
itf_score1 = ITF_score(dst_path1)
itf_score2 = ITF_score(dst_path2)
itf_score3 = ITF_score(dst_path3)
itf_score4 = ITF_score(dst_path4)
itf_score5 = ITF_score(dst_path5)
itf_score6 = ITF_score(dst_path6)
itf_score7 = ITF_score(dst_path7)
print('itf',round(itf_score0,2))
print('itf',round(itf_score1,2))
print('itf',round(itf_score2,2))
print('itf',round(itf_score3,2))
print('itf',round(itf_score4,2))
print('itf',round(itf_score5,2))
print('itf',round(itf_score6,2))
print('itf',round(itf_score7,2))
itf_score0 = ITF_WMR_score(src_path)
itf_score1 = ITF_WMR_score(dst_path1)
itf_score2 = ITF_WMR_score(dst_path2)
itf_score3 = ITF_WMR_score(dst_path3)
itf_score4 = ITF_WMR_score(dst_path4)
itf_score5 = ITF_WMR_score(dst_path5)
itf_score6 = ITF_WMR_score(dst_path6)
itf_score7 = ITF_WMR_score(dst_path7)
print('ITF_WMR_score',round(itf_score0,2))
print('ITF_WMR_score',round(itf_score1,2))
print('ITF_WMR_score',round(itf_score2,2))
print('ITF_WMR_score',round(itf_score3,2))
print('ITF_WMR_score',round(itf_score4,2))
print('ITF_WMR_score',round(itf_score5,2))
print('ITF_WMR_score',round(itf_score6,2))
print('ITF_WMR_score',round(itf_score7,2))