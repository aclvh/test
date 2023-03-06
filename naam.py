#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install streamlit


# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:


HairEye = pd.read_csv('HairEyeColor.csv')


# In[ ]:


st.title('Hair Eye Colour Database')


# In[ ]:


# mainbar kan ook door sidebar te selecteren komt het niet automatisch in de mainbar
InputHair = st.sidebar.selectbox('Select Hair Colour', ('Brown','Black','Blond','Red'))


# In[ ]:


HairEyeSelect = HairEye[HairEye['Hair']==InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)

