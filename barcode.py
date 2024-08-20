import cv2
import cvzone 
from pyzbar import pyzbar as bar

cap = cv2.VideoCapture(0)
output = None
temp = None
x = []
i = 0
while 1:
    ret,frame = cap.read()
    res = bar.decode(frame)
    for data in res:
        output = data.data
        output = str(output,'utf-8')
        output = output.strip('\r\n')
        if(i != 0):
            if(x[i] == x[i-1]):
                continue
        x.append(output)
        print(output)


    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
    cvzone.putTextRect(frame,'Barcode Scanner',[190,30],thickness=2,scale=2,border=2)
    cvzone.putTextRect(frame,f'{output}',[40,300],thickness=2,scale=2,border=2)
    output = None
    cv2.imshow('frame',frame)
    temp = output
    cv2.waitKey(1)

