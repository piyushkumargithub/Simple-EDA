from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd 
import numpy as np 
import sklearn
import seaborn as sbn
import matplotlib.pyplot as plt

@st.cache(persist=True)

#target is still needed to work on
def load_data(selectbox):
    
    path="Datasets/"+selectbox+".csv"
    data=pd.read_csv(path)
    target=data
    return data,target

def load_own_data(file):
    data=pd.read_csv(file)
    target=data
    return data,target

options=["Hyper Cars",
    #"netflix titles",
    "Spotify songs",
    #"Game Awards",
    "Pokemon",
    #"googleplaystore",
    #"Fifa players"
        ]


def main():
    st.title("SIMPLE EDA")
    st.sidebar.title("It all begins here")
    st.markdown("<h3> WELCOME </h3>",unsafe_allow_html=True)

    selectbox=st.sidebar.selectbox(label="choose file to play around with",options=options)
    st.sidebar.markdown("OR")
    file=st.sidebar.file_uploader(label="upload your file here")
    
    
    if file==None:    
        data,target=load_data(selectbox)
        st.subheader((selectbox+" dataset").upper())
    elif file!= None:
        data,target=load_own_data(file)


    
    rows=st.sidebar.slider(label="rows",min_value=1,max_value=min(100,len(data)))
    
    st.dataframe(data.head(rows))
    
    
    st.sidebar.title("Plot Scatterplot between 2 features ")
    X_axis=st.sidebar.selectbox("For x axis",options=data.columns.tolist())
    Y_axis=st.sidebar.selectbox("For y axis",options=data.columns.tolist())
    if st.sidebar.button("Show Plot"): 
        if  X_axis!=Y_axis:
            
            fig,ax=plt.subplots()
            ax=sbn.scatterplot(data=data,x=X_axis,y=Y_axis)
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        
        elif X_axis==Y_axis:
            st.markdown("## You have choosen same feature for both axis")
        
      
        

    

if __name__=='__main__':
    main()
