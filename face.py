#import library opencv
import cv2
#variabel video capture
cap = cv2.VideoCapture(0)

#Fungsi membuat frame
while(True):
    #Membaca Video
    ret,frame = cap.read()
    #menampilkan video
    cv2.imshow('frame',frame)
    #Pengaturan frame
    if cv2.waitKey(1) == ord('b'):
        break
cap.release()
cv2.destroyAllWindows()
