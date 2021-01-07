import cv2
cap = cv2.VideoCapture("rtsp://192.168.1.1:7070/webcam")
# cap = cv2.VideoCapture(0)
ret, frame = cap.read()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 保存视频的编码
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))
framesize = (1280, 720)
out = cv2.VideoWriter('./output.avi', fourcc, 20, framesize)
while ret:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow("frame", frame)
    print(framesize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()



