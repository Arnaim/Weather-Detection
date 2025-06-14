import pandas as pd
import streamlit as st
import numpy as np
import pickle

st.title("Weather Detection Project! 🌧️")

# Sidebar to choose task
st.sidebar.title("Choose the Model Type:")
task = st.sidebar.selectbox("Choose a task", ["Regression", "Classification"])

# REGRESSION MODEL
if task == "Regression":
    st.subheader("🌡️ Regression Task")
    model = pickle.load(open("model_r.pkl", "rb"))  # Load regression model

    st.write("Please enter the following details to predict the temperature:")
    land_avg_temperature = st.number_input("Enter the land_avg_temperature")
    land_max_temperature = st.number_input("Enter the land_max_temperature")
    land_min_temperature = st.number_input("Enter the land_min_temperature")

    input_data = np.array([[land_avg_temperature, land_max_temperature, land_min_temperature]])

    if st.button("Predict (Regression)"):
        prediction = model.predict(input_data)
        st.success(f"🌡️ The predicted temperature is: {prediction[0]:.2f}°C")

# CLASSIFICATION MODEL
elif task == "Classification":
    st.subheader("🌥️ Classification Task")
    model = pickle.load(open("model.pkl", "rb"))  # Load classification pipeline

    st.write("Please enter the following details to predict the weather type:")

    # Numeric inputs
    temperature = st.number_input("Enter the temperature")
    humidity = st.number_input("Enter the humidity")
    wind_speed = st.number_input("Enter the wind speed")
    percipitation = st.number_input("Enter the percipitation")
    pressure = st.number_input("Enter the atmospheric pressure")
    uv_index = st.number_input("Enter the UV index")
    visibility = st.number_input("Enter the visibility")

    # Categorical inputs
    cloud_cover = st.selectbox("Select the cloud cover", ["clear", "cloudy", "partly cloudy", "overcast"])
    season = st.selectbox("Select the season", ["Winter", "Spring", "Summer", "Autumn"])
    location = st.selectbox("Select the location", ["coastal", "mountain", "inland"])

    # Create input DataFrame
    input_dict = {
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Wind Speed": [wind_speed],
    "Precipitation (%)": [percipitation],
    "Cloud Cover": [cloud_cover],
    "Atmospheric Pressure": [pressure],
    "UV Index": [uv_index],
    "Season": [season],
    "Visibility (km)": [visibility],
    "Location": [location]
}

    input_df = pd.DataFrame(input_dict)

    if st.button("Predict (Classification)"):
        prediction = model.predict(input_df)
        st.success(f"☁️ The predicted weather type is: {prediction[0]}")
