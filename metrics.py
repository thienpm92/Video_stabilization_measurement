import os
import sys
import numpy as np
import cv2
import math
import pdb
import matplotlib.pyplot as plt

def metrics(in_src, out_src):
	frameList = os.listdir(out_src)
	frameList.sort()

	# Create brute-force matcher object
	bf = cv2.BFMatcher()

	# Apply the homography transformation if we have enough good matches 
	MIN_MATCH_COUNT = 10 #10

	ratio = 0.7 #0.7
	thresh = 5.0 #5.0

	CR_seq = np.asarray([1])
	DV_seq = np.asarray([1])
	Pt = np.asarray([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
	P_seq = []
	count = 1
	for f in frameList:
		if f.endswith('.png'):
			# Load the images in gray scale
			img1 = cv2.imread(in_src + f, 0)
			img1o = cv2.imread(out_src + f, 0)

			prevFtp = cv2.goodFeaturesToTrack(img1, maxCorners=300, qualityLevel=0.01,
                                                     minDistance=30, blockSize=3)
			curFtp, status, err = cv2.calcOpticalFlowPyrLK(img1,img1o,prevFtp,None)
			i = np.where(status==1)[0]
			prevFtp = prevFtp[i]
			curFtp = curFtp[i]

			M,_ = cv2.findHomography(prevFtp,curFtp)


			# Obtain Scale, Translation, Rotation, Distortion value
			sx = M[0, 0]
			sy = M[1, 1]
			scaleRecovered = math.sqrt(sx*sy)

			w, _ = np.linalg.eig(M[0:2,0:2])
			w = np.sort(w)[::-1]
			DV = w[1]/w[0]
			#pdb.set_trace()

			CR_seq = np.concatenate((1.0/CR_seq, [scaleRecovered]), axis=0)
			DV_seq = np.concatenate((DV_seq, [DV]), axis=0)



			# For Stability score calculation
			if count < len(frameList):
				img2o = cv2.imread(out_src + f[:-9] + '%05d.png' % (int(f[-9:-4])+1), 0)

				prevFtp = cv2.goodFeaturesToTrack(img1o, maxCorners=300, qualityLevel=0.01,
                                                     minDistance=30, blockSize=3)
				curFtp, status, err = cv2.calcOpticalFlowPyrLK(img1o,img2o,prevFtp,None)
				i = np.where(status==1)[0]
				prevFtp = prevFtp[i]
				curFtp = curFtp[i]

				M,_ = cv2.findHomography(prevFtp,curFtp)


				P_seq.append(np.matmul(Pt, M))
				Pt = np.matmul(Pt, M)
			sys.stdout.write('\rFrame: ' + str(count) + '/' + str(len(frameList)))
			sys.stdout.flush()
			print(count)
			count += 1
		#end
	#end

	# Make 1D temporal signals
	P_seq_t = np.asarray([1])
	P_seq_r = np.asarray([1])

	#pdb.set_trace()
	for Mp in P_seq:
		sx = Mp[0, 0]
		sy = Mp[1, 1]
		c = Mp[0, 2]
		f = Mp[1, 2]
		#w, _ = np.linalg.eig(Mp[0:2,0:2])
		#w = np.sort(w)[::-1]
		#DV = w[1]/w[0]
		transRecovered = math.sqrt(c*c + f*f)
		thetaRecovered = math.atan2(sx, sy) * 180 / math.pi
		#thetaRecovered = DV
		P_seq_t = np.concatenate((P_seq_t, [transRecovered]), axis=0)
		P_seq_r = np.concatenate((P_seq_r, [thetaRecovered]), axis=0)

	P_seq_t = np.delete(P_seq_t, 0)
	P_seq_r = np.delete(P_seq_r, 0)

	# FFT
	fft_t = np.fft.fft(P_seq_t)
	fft_r = np.fft.fft(P_seq_r)
	fft_t = abs(fft_t)**2
	fft_r = abs(fft_r)**2
	#freq = np.fft.fftfreq(len(P_seq_t))
	#plt.plot(freq, abs(fft_r)**2)
	#plt.show()
	#print(abs(fft_r)**2)
	#print(freq)
	fft_t = np.delete(fft_t, 0)
	fft_r = np.delete(fft_r, 0)
	fft_t = fft_t[:int(len(fft_t)/2)]
	fft_r = fft_r[:int(len(fft_r)/2)]

	SS_t = np.sum(fft_t[:5])/np.sum(fft_t)
	SS_r = np.sum(fft_r[:5])/np.sum(fft_r)

	# Delete initialized entry
	CR_seq = np.delete(CR_seq, 0)
	DV_seq = np.delete(DV_seq, 0)

	# Print results
	print('\n***Last H:')
	print(M)
	print('***Cropping ratio (Avg, Min):')
	print( str.format('{0:.4f}', np.min([np.mean(CR_seq), 1])) +' | '+ str.format('{0:.4f}', np.min([CR_seq.min(), 1])) )
	print('***Distortion value:')
	print(str.format('{0:.4f}', np.absolute(DV_seq.min())) )
	print('***Stability Score (Avg, Trans, Rot):')
	print(str.format('{0:.4f}',  (SS_t+SS_r)/2) +' | '+ str.format('{0:.4f}', SS_t) +' | '+ str.format('{0:.4f}', SS_r) )

if __name__ == '__main__':
	metrics(in_src='./src/', out_src='./dst/')



