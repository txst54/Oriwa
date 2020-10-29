import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("waterbomb.PNG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.array(img)
plt.imshow(img)
plt.show()
itemindex = np.where(img==0)
img = img[itemindex[1][0]:itemindex[1][-1], itemindex[0][0]:itemindex[0][-1]]
