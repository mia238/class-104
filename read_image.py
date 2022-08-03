from cgitb import grey
import cv2
img= cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
#print(img)
grey_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray image",grey_img)
print(grey_img)
cv2.waitKey(0)