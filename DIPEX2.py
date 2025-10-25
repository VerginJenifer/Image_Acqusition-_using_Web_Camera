#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

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


# In[9]:


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


# In[10]:


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


# In[11]:


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

