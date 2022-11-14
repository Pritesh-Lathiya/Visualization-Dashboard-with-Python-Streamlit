#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go # or plotly.express as px
import io
import plotly.figure_factory as ff
import streamlit as st

from Dataframe import df
measurements = df.columns.tolist()
###########################  separte ###################################################

cat= list(df.select_dtypes('O').columns)

cat1= list(df.select_dtypes('O').columns)
cat1.insert(0, "None")

num= list(df.select_dtypes(np.number).columns)

DEFAULT = '< PICK A VALUE >'

######################################### Side Bar ###################################
st.sidebar.markdown("### Chart ")
option = st.sidebar.selectbox('Which Chart would you like ?',('Bar Chart', 'Pie Chart','Line Chart','Scatter plot','Box plot',
                                                                'Distribution plot','Histogram'))

if option == 'Bar Chart':
    option1 = st.sidebar.selectbox("On what variable ?",measurements);
    
elif option == 'Pie Chart':
    option1 = st.sidebar.selectbox("On what variable ?", cat);
    top_n = st.sidebar.text_input("How many of the top would you like to see ?",1000)
        
elif option == 'Line Chart':
    option21 = st.sidebar.selectbox("X - axis ?", num);
    option22 = st.sidebar.selectbox("Y - axis ?", num);
    option23 = st.sidebar.selectbox("Colorwise ?", cat1);

elif option == 'Box plot':
    option41 = st.sidebar.selectbox("Y - axis ?", num);
    option42 = st.sidebar.selectbox("X - axis ?", cat);
    option43 = st.sidebar.selectbox("Categorise ?", cat1);
        
elif option == 'Scatter plot':
    option31 = st.sidebar.selectbox("X - axis ?", num);
    option32 = st.sidebar.selectbox("Y - axis ?", num);
    option33 = st.sidebar.selectbox("Categorise ?", cat1);
    
    #window_ANTICOR = st.sidebar.selectbox('Window ANTICOR', values, index=default_ix)
    
elif option == 'Distribution plot':
    option51 = st.sidebar.selectbox("X - axis ?", num);
    
elif option == 'Histogram':
    option61 = st.sidebar.selectbox("X - axis ?", num);
    
else:
    option1 = st.sidebar.selectbox("On what variable ?", measurements);
    
    
#####################################  Bar chart   #############################################


with st.container():
    if option == 'Bar Chart':
        st.title("Bar Chart")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            order = st.radio("Order ??",('Ascending', 'Descending'))
        with col2:
            orientation=st.radio("Orientation ??",("Horizontal","Vertical"))
            
            
        if option1 is not None:
            if order == 'Ascending':
                if orientation == "Horizontal":
                    df_category = df.groupby(option1).size().reset_index(name = "count")
                   # df_category=df_category.head(top_n)
                    df_category.sort_values(by='count', ascending = True,inplace=True)
                    fig = px.bar(df_category, x = option1, y = "count",color_discrete_sequence = ["#ffd514"])
                    st.plotly_chart(fig, use_container_width=True);  
                if orientation == "Vertical":
                    df_category = df.groupby(option1).size().reset_index(name = "count")
                    df_category.sort_values(by='count', ascending = True,inplace=True)
                    fig = px.bar(df_category, y = option1, x = "count",color_discrete_sequence = ["#ffd514"])
                    st.plotly_chart(fig, use_container_width=True);      
                
            elif order == 'Descending':
                if orientation == "Horizontal":
                    df_category = df.groupby(option1).size().reset_index(name = "count")
                    df_category.sort_values(by='count', ascending = False,inplace=True)
                    fig = px.bar(df_category, x = option1, y = "count",color_discrete_sequence = ["#ffd514"])
                    st.plotly_chart(fig, use_container_width=True);  
                if orientation == "Vertical":   
                    df_category = df.groupby(option1).size().reset_index(name = "count")
                    df_category.sort_values(by='count', ascending = False,inplace=True)
                    fig = px.bar(df_category, y = option1, x = "count",color_discrete_sequence = ["#ffd514"])
                    st.plotly_chart(fig, use_container_width=True);  
                
            else: 
                df_category = df.groupby(option1).size().reset_index(name = "count")
                fig = px.bar(df_category, x = option1, y = "count",color_discrete_sequence = ["#ffd514"])
                st.plotly_chart(fig, use_container_width=True); 

        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )

#####################################  Line Chart   #########################################
        
    elif option == 'Line Chart': 
        st.title("Line Chart")
        st.write('Other options')
        option_1 = st.checkbox('Invisible')
        option_2 = st.checkbox('Fixedrange')
        
        if option23=="None":
            fig = px.line(df, x=option21, y=option22)
            #fig.update_xaxes(visible=False, fixedrange=False)
            #fig.update_yaxes(visible=False, fixedrange=False)
            st.plotly_chart(fig, use_container_width=True); 
        else:        
            if option_1 and option_2:
                fig = px.line(df, x=option21, y=option22,color=option23)
                fig.update_xaxes(visible=False, fixedrange=False)
                fig.update_yaxes(visible=False, fixedrange=False)
                st.plotly_chart(fig, use_container_width=True);      
            elif option_1:
                fig = px.line(df, x=option21, y=option22,color=option23)
                fig.update_xaxes(visible=False)
                fig.update_yaxes(visible=False)   
                st.plotly_chart(fig, use_container_width=True);
            elif option_2:
                fig = px.line(df, x=option21, y=option22,color=option23)
                fig.update_xaxes(fixedrange=True)
                fig.update_yaxes(fixedrange=True)
                st.plotly_chart(fig, use_container_width=True);
            else:
                fig= px.line(df, x=option21, y=option22,color=option23)
                st.plotly_chart(fig, use_container_width=True); 
        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )   
            
     
###############################  Box Plot ############################################
            
    elif option == 'Box plot':
        st.title("Box plot")  
        option_1 = st.checkbox('Transpose')      
        option_2 = st.checkbox('point outside')
        
        
        #option41 = st.sidebar.selectbox("Y - axis ?", num);    
        #option42 = st.sidebar.selectbox("X - axis ?", cat);
        if option43=="None":
            fig = go.Figure()
            fig = px.box(df,x=option41, y=option42)
            st.plotly_chart(fig ,use_container_width=True);             
        else:    
            if option_1 and option_2:
                fig = go.Figure()
                fig = px.box(df,x=option41, y=option42,color=option43, points="all")
                st.plotly_chart(fig ,use_container_width=True); 

            elif option_1:
                  fig = px.box(df,x=option41, y=option42,color=option43)
                  st.plotly_chart(fig ,use_container_width=True); 

            elif option_2:
                fig = px.box(df,x=option42, y=option41,color=option43, points="all")
                st.plotly_chart(fig ,use_container_width=True);              

            else:
                fig = px.box(df,x=option42, y=option41,color=option43)
                st.plotly_chart(fig ,use_container_width=True);  
        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )    
#################################  Scatter Plot #####################################################   


    elif option == "Scatter plot":
        st.title("Scatter plot")
        if option33=="None":
            fig = px.scatter(df, x=option31, y=option32)
            st.plotly_chart(fig, use_container_width=True); 
        else:    
            fig = px.scatter(df, x=option31, y=option32, color=option33)
            st.plotly_chart(fig, use_container_width=True); 
        
        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )
    
################################ Distribution Plot #######################################    


    elif option == 'Distribution plot':
        st.title("Distribution plot")
        hist_data = [df[option51]]
        group_labels = [option51]
        fig = ff.create_distplot(hist_data, group_labels)  #
        st.plotly_chart(fig, use_container_width=True);   #
        
        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )
######################################  HIstogram   ##################################       


    elif option == 'Histogram':
        st.title("HIstogram")
        fig = px.histogram(df[option61], x=option61)
        st.plotly_chart(fig, use_container_width=True);   #    
        
        # Create an in-memory buffer
        buffer = io.BytesIO()

        # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
        # Download the pdf from the buffer
        st.download_button(
                label="Download Image",
                data=buffer,
                file_name="figure.pdf",
                mime="application/pdf",
            )
        
###################################  Pie Chart ######################################        
    else:
        st.title("Pie Charts")     
                    
    #         col1.subheader("Top....")
    #         top_n =col1.text_input("How many of the top would you like to see ?",5)
        top_n=int(top_n)
        cnt = df.groupby(by=[option1]).count()[['ID']].rename(columns={"option1":"Count"}).reset_index()
        cnt_topn=cnt.head(top_n)
        fig = px.pie(cnt_topn, values='ID', names=option1)
        st.plotly_chart(fig, use_container_width=True);


            # Create an in-memory buffer
        buffer = io.BytesIO()

            # Save the figure as a pdf to the buffer
        fig.write_image(file=buffer, format="pdf")
           # Download the pdf from the buffer
        st.download_button(
                    label="Download Image",
                    data=buffer,
                    file_name="figure.pdf",
                    mime="application/pdf",
                )
        

                  
 
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

