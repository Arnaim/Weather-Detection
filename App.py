import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from reg_preprocessing import data_pre
from sklearn.pipeline import Pipeline
import pickle

st.title("Weather Detection Project!🌧️")

model = pickle.load(open("model_r.pkl", "rb"))

#make a sidebar tto select if the user needs  classification or regression or forcasting
st.sidebar.title("Choose the Model Type:")
task = st.sidebar.selectbox("Choose a task", ["Regression", "Classification"])


if task == "Regression":
    st.write("Regression")
    st.write("Please enter the following details to predict the temperature:")
    land_avg_temperature = st.number_input("Enter the land_avg_temperature")
    land_max_temperature = st.number_input("Enter the land_max_temperature")
    land_min_temperature = st.number_input("Enter the land_min_temperature")
    
    input_data = np.array([[land_avg_temperature, land_max_temperature, land_min_temperature]])
    prediction = model.predict(input_data)
    
    if st.button("Predict"):
        st.write(f"The predicted temperature is: {prediction[0]}")

elif task == "Classification":
    st.write("Classification")
    st.write("Please enter the following details to predict the weather type:")
    temperature = st.number_input("Enter the temperature")
    humidity = st.number_input("Enter the humidity")
    wind_speed = st.number_input("Enter the wind speed")
    percipitation = st.number_input("Enter the percipitation")
    pressure = st.number_input("Enter the atmospheric pressure")
    uv_index = st.number_input("Enter the uv index")
    visibility = st.number_input("Enter the visibility")
    
    #get the cloud cover and season as a dropdown
    cloud_cover = st.selectbox("Select the cloud cover", ["clear", "cloudy", "partly cloudy", "overcast"])
    season = st.selectbox("Select the season", ["Winter", "Spring", "Summer", "Autumn"])
    location = st.selectbox("Select the location", ["coastal", "mountain", "inland"])
    
    input_data = np.array([[temperature, humidity, wind_speed, percipitation, cloud_cover, pressure, uv_index, season, visibility, location]])
    scaler = pickle.load(open("scaler.pkl", "rb"))
    input_data = scaler.transform(input_data)
    
    prediction = model.predict(input_data)
    
    if st.button("Predict"):
        st.write(f"The predicted weather type is: {prediction[0]}")
        

    
