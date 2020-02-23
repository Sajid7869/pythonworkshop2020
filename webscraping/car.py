import cv2
'''list=['person4.jpg','photo3.jpg']
for i in list:'''
face_cascade=cv2.CascadeClassifier(r'cars.xml')
video=cv2.VideoCapture(r'Cars - 1900.mp4')
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    'print(type(video))'
    '''img=cv2.imread('srk.jpg',1)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)'''
    faces=face_cascade.detectMultiScale(gray,
    scaleFactor=1.03,
    minNeighbors=5
    )
    for x,y,w,h in faces:
        rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)   
# print(faces)
    cv2.imshow('Gray image',frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
video.release()