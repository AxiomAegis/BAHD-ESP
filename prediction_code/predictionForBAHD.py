#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ["CUDA_VISIBLE_DEVICES"]="1"


# In[2]:


import sys
sys.path.insert(0, 'code')
from prediction import ESP_predicton


# In[14]:


import pandas as pd
data = pd.read_csv("file path.csv").drop_duplicates()
data


# In[13]:


def calculate_ESP_predicton(row):
    pred_df = ESP_predicton(
        metabolite_list = [row["final_SMILE"]],
        enzyme_list = [row["Protein"]]
             )
    
    if pred_df is not None:
        return pred_df.loc[0, "valid input"], pred_df.loc[0, "Prediction score"]
    else:
        return "No result", "No result"

data[['valid input', "Prediction score"]] = data.apply(calculate_ESP_predicton, axis=1, result_type="expand")
data


# In[6]:


data.to_excel('BAHD_save file path.xlsx', index=False)


# In[ ]:




