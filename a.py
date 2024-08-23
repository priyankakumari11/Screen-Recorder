# Screen reonding using opencv
import cv2
import pyautogui as p
import numpy as np
import os
home_directory = os.path.expanduser("~")
print(f"Home directory: {home_directory}")
# create resolution
rs = p.size()
print(rs)

# filename in which we store recording
# fn = input("Please Enter file name and path: ")

# fix the frame rate
fps = 25

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("ricordedvideo1.mp4",fourcc,fps,rs)


cv2.namedWindow("Live Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording",(rs.width,rs.height))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live Recording",f)
    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()
