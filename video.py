import cv2


# creating an instance of the video class
cap = cv2.VideoCapture(0)

# get fourcc variable for saving with video
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# create an instance of video writer
out = cv2.VideoWriter('output.avi', fourcc, 24, (640, 480))

# create while loop to capture frames
while cap.isOpened():
    return_val, frames = cap.read()

    if return_val:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frames)

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Main Webcam', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()