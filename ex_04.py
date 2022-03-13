# Show text/date and time on videos using OpenCV

import cv2
import datetime
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = f"width: {cap.get(3)} height: {cap.get(4)}"
        date_time = str(datetime.datetime.now())

        frame = cv2.putText(frame, date_time, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("video", frame)
        # out.write(frame)

        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()
