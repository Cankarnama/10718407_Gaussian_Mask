import time
import sys
import cv2
import numpy as np

print("<------------------------[ Gaussian Filter ]------------------------>")
print("\nPress enter key to increase blurring intensity\n\n")
for sigma in range(1, 5):
	print(f"Intensity {sigma}")
	img = cv2.imread('dog.jpeg')

	dst = np.empty_like(img) #create empty array the size of the image
	noise = cv2.randn(dst, (0,0,0), (20,20,20)) #add random img noise

	# Pass img through noise filter to add noise
	img_noise = cv2.addWeighted(img, 0.5, noise, 0.5, 50) 

	# Blurring function
	blur = cv2.GaussianBlur(img_noise, (15, 15), sigma)

	cv2.imshow('Img', blur)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

