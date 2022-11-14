#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as com
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # pip install plotly-express

#'<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'

st.set_page_config(layout="wide",page_title="Data visualization Dashboard")


# ---- MAINPAGE ----
new_title = '<p style="font-family:sans-serif; color:Yellow; font-size: 42px;">Data Visualization Dashboard</p>'
st.markdown(new_title, unsafe_allow_html=True)        
st.markdown("##")



dataset = st.sidebar.file_uploader("upload file here", type = ['csv'])
if dataset is not None:
    df = pd.read_csv(dataset)     
    #st.write("Filename:",dataset.name)
    b=(dataset.name)
    a=("Filename: ")
    c=a + b
    st.header(c)
else:
    df=pd.read_csv("car_price_prediction.csv")
    df.head(2)
    st.header("Filename: Car Price Prediction")


num_rows = st.slider('Select number of rows', min_value=1, max_value=20) #geting the input.

df1 = df.head(num_rows)
st.dataframe(df1)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# In[ ]:



































# In[ ]:

















