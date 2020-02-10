import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img1=cv2.imread("img1.jpg")
img2=cv2.imread("img2.jpg")
img3=cv2.imread("img3.jpg")

g_image1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
g_image2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
g_image3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

faces1=face_cascade.detectMultiScale(g_image1,scaleFactor=1.05, minNeighbors=5)
faces2=face_cascade.detectMultiScale(g_image2,scaleFactor=1.05, minNeighbors=5)
faces3=face_cascade.detectMultiScale(g_image3,scaleFactor=1.05, minNeighbors=5)

a=0

for x, y, w, h in faces:
    a=a+1
    img1=cv2.rectangle(img1, (x,y),(x+w,y+h),(0,255,0),3)
    img2=cv2.rectangle(img2, (x,y),(x+w,y+h),(0,255,0),3)
    img3=cv2.rectangle(img3, (x,y),(x+w,y+h),(0,255,0),3)



#print(type(faces))
#print(faces)

resized1=cv2.resize(img1,(int(img.shape[1]/3),int(img.shape[0]/3)))
resized2=cv2.resize(img2,(int(img.shape[1]/3),int(img.shape[0]/3)))
resized3=cv2.resize(img3,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("gray",resized)
print("no of faces : ",a)
cv2.waitKey(0)
cv2.destroyAllWindows()
