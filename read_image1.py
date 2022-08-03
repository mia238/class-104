import cv2
img= cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket

text_to_show="I have the best teacher to teach me!!!!!!"
cv2.putText(img,
            text_to_show,
            (20,200),
            fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            fontScale=1,
            color=(220,208,255))
cv2.imshow("display image",img)
cv2.waitKey(0)