import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./images/nuclei.png')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#load image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #reads the image as a grayscale image
plt.imshow(gray, cmap='gray')
plt.axis('off')
# plt.show()

# print(gray[5:25, :15]) #pixels have integer values from 0 to 255.

#use histogram to inspect and decide which threshold to use for converting the gray image to a binary one
# hist, bins = np.histogram(gray.flatten(), bins = 256, range=(0,256))
# plt.plot(hist)
# # plt.show()
# bin_centers = (bins[:-1] + bins[1:]) / 2
# plt.figure(figsize=(8, 4))
# plt.plot(bin_centers, hist, color='blue')
# # plt.show()
#
# #convert the image
# B = np.zeros_like(gray, dtype=np.uint8)
# print(f'The shape of matrix B is {B.shape}')
# print(f'matrix B is type {type(B)}')
# print(f'matrix B has element type {type(B[0,0])}')
# # print(B)
# B[gray > 100] = 255 #binarization
# # print(B[:25, :15])
#
# otsu_threshold, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# print(otsu_threshold)
# print(binary_image[5:25, :15])
#
# np.set_printoptions(linewidth=200)
# B = binary_image[0:60:2, 0:40:2]
# print(B)
# n_comp, labeled_img = cv2.connectedComponents(binary_image)
# print(n_comp)


coins = cv2.imread('images/coins.png', cv2.IMREAD_GRAYSCALE)
print(coins)
print(coins.shape)
plt.imshow(coins, cmap='gray')
plt.show()
coins = cv2.GaussianBlur(coins, (3,3), 0) #blurring creates more homogeneity
plt.imshow(coins, cmap='gray')
plt.show()

th = 110
coins2 = np.copy(coins)
coins2[coins2 > th] = 255
coins2[coins <= th] = 0
plt.imshow(coins2, cmap='gray')
plt.show()

#erosion to separate attached/distorted parts
kernel = np.ones((2,2), np.uint8)
eroded = cv2.erode(coins2, kernel, iterations=5)
plt.imshow(eroded, cmap='gray')
plt.show()

n_comp, labeled_img = cv2.connectedComponents(eroded)
print(n_comp)

dist = cv2.distanceTransform(coins2, cv2.DIST_L2, 3)
plt.imshow(dist, cmap='gray')
plt.show()

otsu_th, coins5 = cv2.threshold(coins, 90, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(coins5, cmap='gray')
plt.show()
dist5 = cv2.distanceTransform(coins5, cv2.DIST_L2, 3)
plt.imshow(dist5, cmap='gray')
plt.show()
