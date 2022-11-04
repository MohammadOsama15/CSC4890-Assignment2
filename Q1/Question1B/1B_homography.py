import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[324,530],[179,717],[782,776],[761,525],[223,461] ])
dest_points = np.array([[517,643],[185,632],[786,763],[452,601],[111,628]])


h, status = cv2.findHomography(src_points, dest_points)
print(h)
im_src = cv2.imread('img1greyscale.png')
im_dst = cv2.imread('img2grayscale.png')

im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()

#Coordinates for image1
#[[324,530],[179,717],[782,776],[761,525],[223,461]
#Coordinates for image2
# [[517,643],[185,632],[786,763],[452,601],[111,628]]


