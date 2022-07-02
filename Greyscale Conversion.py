#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.__version__


# In[ ]:


# Load our input image
image = cv2.imread(r"C:\Users\anish\Downloads\dog.jpg", cv2.IMREAD_UNCHANGED)
#display image
image_greyscale=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#default view
#cv2.imshow(r"C:\Users\anish\Downloads\dog.jpg", image)     
cv2.imshow(r"C:\Users\anish\Downloads\dog.jpg", image_greyscale) 
#break
cv2.waitKey(0)
cv2.destoryAllWindows()


# In[ ]:




