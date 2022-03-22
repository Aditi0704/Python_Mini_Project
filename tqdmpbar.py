#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tqdm import tqdm
import time
    
for i in tqdm(range(20),desc="tqdm() Progress Bar"):
    time.sleep(0.5)


# In[ ]:




