import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)

def data_pre(df):
    df = df.drop(columns=["LandAverageTemperatureUncertainty", "LandMaxTemperatureUncertainty",
                          "LandMinTemperatureUncertainty", "LandAndOceanAverageTemperatureUncertainty"], axis=1)
    
    df.rename(columns={"dt": "Date", "LandAverageTemperature": "land_avg_temperature",
                   "LandMaxTemperature": "land_max_temperature", "LandMinTemperature": "land_min_temperature" ,
                   "LandAndOceanAverageTemperature" : "land_and_ocean_AVG"}, inplace=True)
    
    df["Date"] = pd.to_datetime(df["Date"])
    df["year"] = df["Date"].dt.year
    df["month"] = df["Date"].dt.month
    df.set_index("year", inplace=True)
    df.dropna(inplace=True)
    return df
