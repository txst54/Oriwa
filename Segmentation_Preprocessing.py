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
img = cv2.resize(img, (512, 512))
plt.imshow(img)
plt.show()
print(img.shape)
img = img.transpose((2, 0, 1))
#COLOR DETECTION
red = np.where(((img[0]==255) & (img[1]<255) & (img[2]<255))==True)
blue = np.where(((img[2]==255) & (img[0]<255) & (img[1]<255))==True)
V = np.zeros((512, 512))
for i in range(len(blue[0])):
  V[blue[0][i]][blue[1][i]] = 255
plt.imshow(V)
plt.show()
M = np.zeros((512, 512))
for i in range(len(red[0])):
  M[red[0][i]][red[1][i]] = 255
plt.imshow(M)
plt.show()
division = int(input("Divisons: "))
def grid(div, li):
  out = []
  #print(li.shape)
  a = int(512/div)
  #print(a)
  for y in range(div):
    #print(y)
    for x in range(div):
      #print(y*a, ((y+1)*a), x*a, (x+1)*a)
      #print(li[y*a:((y+1)*a), x*a:(x+1)*a].shape)
      out.append(li[y*a:((y+1)*a), x*a:(x+1)*a])
  return out
Mr = np.array(grid(division, V))
Vb = np.array(grid(division, M))
print(np.where([Mr==255]))
plt.imshow(Mr[3])
plt.show() 
