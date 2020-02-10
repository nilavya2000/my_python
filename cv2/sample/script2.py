import cv2
import glob

images=glob.glob("*.jpg")

for i in images:
    img=cv2.imread(i,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("hey",re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+i,re)
