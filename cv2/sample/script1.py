import cv2

img=cv2.imread("kangaroo.jpg",0)


print(img.shape)
print(img)
resize=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("kangaroo",resize)
cv2.imwrite("kangroo_resize.jpg",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
