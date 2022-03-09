# Capture videos from camera

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

# while loop to capture the frame continuously

while True:
    ret, frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("video", gray)
        out.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()
