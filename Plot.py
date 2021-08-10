import streamlit as st
import matplotlib.pyplot as plt  
import seaborn as sbn  


def createScatter(data,X_axis,Y_axis):  
     
        
        if  X_axis!=Y_axis:
            
            fig,ax=plt.subplots()
            ax=sbn.scatterplot(data=data,x=X_axis,y=Y_axis)
            plt.xticks(rotation="vertical",fontsize=5)
            st.pyplot(fig)

        
        elif X_axis==Y_axis:
            st.markdown("## You have choosen same feature for both axis")




def createSwarm():
    pass


def createLine():
    pass

def createHeat():
    pass

def createBar():
    pass