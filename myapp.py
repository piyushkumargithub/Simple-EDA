from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#custom made modules
import Plot
import regression as ra


@st.cache_data(persist=True)


# target is still needed to work on
def load_data(selectbox):

    path = "Datasets/"+selectbox+".csv"
    data = pd.read_csv(path)
    target = data
    return data, target


def load_own_data(file):
    data = pd.read_csv(file)
    target = data
    return data, target


options = ["Hyper Cars",
           #"netflix titles",
           "Spotify songs",
           #"Game Awards",
           "Pokemon",
           # "googleplaystore",
           #"Fifa players"
           ]


def main():

    st.title("SIMPLE EDA")
    st.sidebar.title("Data exploration made simple")
    st.markdown("<h3> WELCOME </h3>",unsafe_allow_html=True)

    # select to choose from available csv files
    selectbox = st.sidebar.selectbox(
        label="choose file to play around with", options=options)
    st.sidebar.markdown("OR")

    # if user wants to upload their file
    file = st.sidebar.file_uploader(label="upload your file here")

    # to load dataset
    if file == None:
        data, target = load_data(selectbox)
        st.subheader((selectbox+" dataset").upper())
    elif file != None:
        data, target = load_own_data(file)

    # choose no of rows or entries to show from uploaded dataset
    rows = st.sidebar.slider(label="rows", min_value=1,
                             max_value=min(100, len(data)))
    st.dataframe(data.head(rows))

    # list of plot available to choose from
    plotoptions = ["Scatterplot", "Swarmplot",
                   "Lineplot", "Heatmap", "Barplot"]
    plotoption = st.sidebar.selectbox(
        label="choose type of plot", options=plotoptions)

    if plotoption == "Scatterplot":
        st.sidebar.title("Plot Scatterplot between 2 features ")
        X_axis = st.sidebar.selectbox(
            "For x axis", options=data.columns.tolist())
        Y_axis = st.sidebar.selectbox(
            "For y axis", options=data.columns.tolist())
        if st.sidebar.button("Show Plot"):
            Plot.createScatter(data, X_axis, Y_axis)

    elif plotoption == "Swarmplot":
        st.sidebar.title("Plot Swarmplot between 2 features ")
        X_axis = st.sidebar.selectbox(
            "For x axis", options=data.columns.tolist())
        Y_axis = st.sidebar.selectbox(
            "For y axis", options=data.columns.tolist())
        if st.sidebar.button("Show Plot"):
            Plot.createSwarm(data, X_axis, Y_axis)

        # part still under construction

    elif plotoption == "Lineplot":
        st.sidebar.title("Plot Lineplot between 2 features ")
        X_axis = st.sidebar.selectbox(
            "For x axis", options=data.columns.tolist())
        Y_axis = st.sidebar.selectbox(
            "For y axis", options=data.columns.tolist())
        if st.sidebar.button("Show Plot"):
            Plot.createLine(data, X_axis, Y_axis)

    elif plotoption == "Heatmap":
        st.sidebar.title("Plot Heatmap between 2 features ")

        # Axis not required
        # X_axis = st.sidebar.selectbox("For x axis", options=data.columns.tolist())
        # Y_axis = st.sidebar.selectbox("For y axis", options=data.columns.tolist())
        if st.sidebar.button("Show Plot"):
            Plot.createHeat(data)

    elif plotoption == "Barplot":
        st.sidebar.title("Plot Barplot between 2 features ")
        X_axis = st.sidebar.selectbox(
            "For x axis", options=data.columns.tolist())
        Y_axis = st.sidebar.selectbox(
            "For y axis", options=data.columns.tolist())
        if st.sidebar.button("Show Plot"):
            Plot.createBar(data, X_axis, Y_axis)

    regression = st.sidebar.checkbox("Check to apply regression algorithm")
    if regression:
        regModels(data)


def regModels(data):
    mlAlgorithms = ["Simple Linear Regression", "Multiple Linear Regression",
                    "Polynomial Regression", "Support Vector Regression"]
    mlAlgorithm = st.sidebar.selectbox(
        "which algorithm you want to apply", mlAlgorithms)

    if mlAlgorithm == "Simple Linear Regression":
        # to get only columns with numerical values select_dtypes is used here
        X = st.sidebar.selectbox("Feature ", options=data.select_dtypes(
            include=np.number).columns.tolist())
        Y = st.sidebar.selectbox("Target ", data.select_dtypes(
            include=np.number).columns.tolist())

        # this part is still in development and will break
        Xdata = data[X].values.reshape(-1, 1)
        Ydata = data[Y].values.reshape(-1, 1)
        # test set size

        test_size = st.sidebar.slider(
            label="test set size", min_value=0.1, max_value=0.9, step=0.1)

        


        st.pyplot(ra.linearRegression(X,Y,Xdata,Ydata,test_size))

        


if __name__ == '__main__':
    main()
