import warnings
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pickle
import streamlit as st
from reg_preprocessing import data_pre

warnings.filterwarnings('ignore')

def create_pipeline(x_train, y_train, k="all", n_estimators=100, max_depth=50, random_state=77, n_jobs=-1):
    pipeline = Pipeline([
        ("feature_selection", SelectKBest(k=k)),  # Feature selection
        ("scaler", StandardScaler()),  # Scaling
        ("regressor", RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state,
            n_jobs=n_jobs
        ))  # Regression model
    ])
    
    pipeline.fit(x_train, y_train)
    return pipeline


def main():
    try:
        df = pd.read_csv(r"E:\Full Data Science Projects\Weather Prediction Project\GlobalTemperatures.csv")
        df = data_pre(df)
        
        target = "land_and_ocean_AVG"
        if target not in df.columns:
            raise ValueError(f"Target column '{target}' not found in the DataFrame.")
        
        y_train = df[target]
        x_train = df[["land_avg_temperature", "land_max_temperature", "land_min_temperature"]]
        
        # Check if x_train and y_train have data
        if x_train.empty or y_train.empty:
            raise ValueError("x_train or y_train is empty.")
        
        pipeline = create_pipeline(x_train, y_train)
        
        # Train and save model
        with open("model_r.pkl", "wb") as file:
            pickle.dump(pipeline, file)
        
        st.write("Model trained and saved successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")  # Print error to the console
        st.write(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
