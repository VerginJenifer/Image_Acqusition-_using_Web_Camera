
## Aim:
 
To write a python program using OpenCV to capture the image from the web camera and do the following image manipulations.
i) Write the frame as JPG 
ii) Display the video 
iii) Display the video by resizing the window
iv) Rotate and display the video

## Software Used
Anaconda - Python 3.7
## Algorithm
### Step 1:
Import the OpenCV library (cv2).

### Step 2:
Initialize the webcam using cv2.VideoCapture(0).

### Step 3:
Capture frames in a loop, and:

Save a frame as JPG file using cv2.imwrite().

Display the live video stream using cv2.imshow().

### Step 4:
Resize the video frame using cv2.resize() and display it.

### Step 5:
Rotate the frame using cv2.rotate() and display the rotated video.

### Step 6:
Break the loop when the user presses the ‘q’ key and release the camera.

## Program:
``` Python
### Developed By: D VERGIN JENIFER
### Register No: 212223240174

## i) Write the frame as JPG file

import cv2
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
# DEVELOPED BY D VERGIN JENIFER 212223240174
capture=cv2.VideoCapture(0)
ret,frame=capture.read()
if ret:
    cv2.imwrite("image.jpg",frame)
capture.release()
captured=cv2.imread('image.jpg')

plt.imshow(captured[:,:,::-1])
plt.title('Captured Image')
plt.axis('off')
plt.show()


## ii) Display the video

Capture=cv2.VideoCapture(0)
for i in range(50):
    ret,frame=Capture.read()
    if not ret:
        break
    org_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(org_frame)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)
Capture.release()
#DEVELOPED BY D VERGIN JENIFER 212223240174


## iii) Display the video by resizing the window

capture=cv2.VideoCapture(0)
for i in range(50):
    ret,frame=capture.read()
    if not ret:
        break
    resized=cv2.resize(frame,(100,150))
    org_frame=cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(org_frame)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)
capture.release()
#DEVELOPED BY D VERGIN JENIFER 212223240174


## iv) Rotate and display the video


capture=cv2.VideoCapture(0)
for i in range(50):
    ret,frame=capture.read()
    if not ret:
        break
    rotated=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    org_frame=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
    clear_output(wait=True)
    plt.imshow(org_frame)
    plt.axis('off')
    plt.show()
    time.sleep(0.05)
capture.release()
#DEVELOPED BY D VERGIN JENIFER 212223240174






```
## Output

### i) Write the frame as JPG image

<img width="735" height="521" alt="image" src="https://github.com/user-attachments/assets/efd7216b-8197-48d3-9a8d-fd3fe0d3d4e5" />


### ii) Display the video

<img width="651" height="499" alt="image" src="https://github.com/user-attachments/assets/a0a2b7a2-0c2e-4000-b848-94e24a09f4a7" />



### iii) Display the video by resizing the window

<img width="341" height="490" alt="image" src="https://github.com/user-attachments/assets/e2154cf7-2f6b-46b7-b508-c9c954c067b4" />



### iv) Rotate and display the video


<img width="377" height="490" alt="image" src="https://github.com/user-attachments/assets/fd0b6eb6-8f32-4b48-8aa7-1adb9c612fe0" />




## Result:
Thus the image is accessed from webcamera and displayed using openCV.
