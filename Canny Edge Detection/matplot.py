import cv2
import numpy as np
from matplotlib import pyplot as plt

#threshold
img2 = cv2.imread('C:\\Users\\Rishika\\Documents\\Computer_Vision\\Canny_Edge_Detection\\images\\foggy.png')
saliencySR = cv2.saliency.StaticSaliencySpectralResidual_create()
_, saliencySRMap = saliencySR.computeSaliency(img2)

img1 = cv2.imread('C:\\Users\\Rishika\\Documents\\Computer_Vision\\Canny_Edge_Detection\\images\\foggy.png')
saliencyFG = cv2.saliency.StaticSaliencyFineGrained_create()
_, saliencyFGMap = saliencyFG.computeSaliency(img1)

img = cv2.imread('C:\\Users\\Rishika\\Documents\\Computer_Vision\\Canny_Edge_Detection\\images\\foggy.png', cv2.IMREAD_GRAYSCALE)
blurImg = cv2.blur(img,(10,10)) 
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.Canny(img,100,200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

saliencyFG = cv2.saliency.StaticSaliencyFineGrained_create()
_, saliencyFGMap = saliencyFG.computeSaliency(sobelY)

titles = ['Image', 'Blurred image', 'Gradient', 'Non-Max Suppression', 'Threshold', 'Hysteresis']
images = [img2, blurImg, sobelCombined, edges, saliencySRMap, sobelY]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()