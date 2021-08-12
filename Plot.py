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




def createSwarm(data,X_axis,Y_axis):

    if X_axis!=Y_axis:
        fig,ax=plt.subplots()
        ax=sbn.swarmplot(data=data,x=X_axis,y=Y_axis)
        plt.xticks(rotation="vertical",fontsize=5)
        st.pyplot(fig)

    elif X_axis == Y_axis:
        st.markdown("## You have choosen same feature for both axis")




def createLine(data,X_axis,Y_axis):
    if X_axis!=Y_axis:
        fig,ax=plt.subplots()
        ax=sbn.lineplot(data=data,x=X_axis,y=Y_axis)
        plt.xticks(rotation="vertical",fontsize=5)
        st.pyplot(fig)

    elif X_axis == Y_axis:
        st.markdown("## You have choosen same feature for both axis")



def createHeat(data):

    #heatmap doesn't require x,y axis it is created with the numeral fetures in the given datset
        mj = data.select_dtypes(exclude='object')

        fig,ax=plt.subplots()
        ax=sbn.heatmap(data=mj)
        plt.xticks(rotation="vertical",fontsize=5)
        st.pyplot(fig)

    # elif X_axis == Y_axis:
    #     st.markdown("## You have choosen same feature for both axis")


def createBar(data,X_axis,Y_axis):


    #only working on numeral features need to be updated

    if X_axis!=Y_axis:
        fig,ax=plt.subplots()
        ax=sbn.barplot(data=data,x=X_axis,y=Y_axis)
        plt.xticks(rotation="vertical",fontsize=5)
        st.pyplot(fig)

    elif X_axis == Y_axis:
        st.markdown("## You have choosen same feature for both axis")