from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import imutils

arr = np.array((1, 2, 3, 4, 5))
are = np.array((arr, arr, arr, arr, arr))

img = cv2.imread('123.jpg',0)
# cv2.imshow('image',img)
print('----',type(img))

cv2.waitKey(0)
cv2.destroyAllWindows()

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols = img.shape
crow,ccol = rows//2 , cols//2
#fshift = fshift[crow-30:crow+31, ccol-30:ccol+31] #= 0

f_ishift = np.fft.ifftshift(fshift)
img_back = np.abs(np.fft.ifft2(f_ishift))
print(are)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
