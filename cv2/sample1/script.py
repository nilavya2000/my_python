import cv2

img=cv2.imread("img3.jpg",1)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resize=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("galaxy",resize)
cv2.imwrite("img3_resized.jpg",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
