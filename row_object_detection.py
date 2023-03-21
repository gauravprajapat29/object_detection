#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bing_image_downloader import downloader


# In[26]:


# downloader.download("apple fruit ", limit=30,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)


# In[23]:


import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# In[24]:


path = r"C:\Users\WSCUBETECH\OneDrive\Desktop\pr\dataset"


# In[25]:


file_name = os.listdir(path)
file_name.sort()
file_name


# In[6]:


from sklearn.preprocessing  import LabelEncoder


# In[7]:


le = LabelEncoder()
le.fit(file_name)
file_no = le.transform(file_name)


# In[8]:


output = []
image = []
image_flatten = []


# In[9]:


for i,j in zip(file_name,file_no):
    path1 = path+"\\"+i
    for filename in os.listdir(path1):
        path2 = path1+"\\"+filename 
        img = cv2.imread(path2)
        img = cv2.resize(img,(150,200))
        image_flatten.append(img.flatten())
        output.append(j)
        image.append(img)


# In[11]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# In[12]:


x_trian , x_test ,y_train ,y_test = train_test_split(image_flatten,output,test_size=0.2,random_state=42)


# In[13]:


from sklearn.svm import SVC


# In[14]:


s = SVC(C=10,
    kernel='linear',
    degree=1,
    gamma='scale')


# In[15]:


s.fit(x_trian,y_train)


# In[16]:


pr = s.predict(x_test)


# In[17]:


j = cv2.imread(r"C:\Users\WSCUBETECH\OneDrive\Desktop\pr\dataset\smart watch\Image_1.jpg")
j = cv2.resize(j,(150,200))
j1 = j.flatten()


# In[19]:


ar = s.predict([j1])


# In[85]:


s.score(x_test,y_test),s.score(x_trian,y_train)


# In[86]:


import pickle
p = open("obj.txt","wb")
pickle.dump(s,p)
p.close()


# In[ ]:




