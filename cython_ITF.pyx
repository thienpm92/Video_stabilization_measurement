import cython
import math



cpdef float PSNR_cython(unsigned char [:, :] img1, unsigned char [:, :] img2):

    cdef int i,j,h,w
    h = img1.shape[0]
    w = img1.shape[1]

    cdef int N_pixel = w*h
    cdef int tmp = w*h
    cdef float total = 0

    for i in range (h):
        for j in range (w):
            if (img1[i,j] ==0) or (img2[i,j] ==0):
                N_pixel -= 1
                continue
            total += float(abs(img1[i,j]-img2[i,j]))**2
    cdef float error = total/N_pixel
    cdef float psnr = (10*math.log10((255**2)/error))
    return psnr
