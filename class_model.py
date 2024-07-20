import warnings
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import pickle
import streamlit as st
from class_preproccising import data_pre
warnings.filterwarnings('ignore')

target_column = "Weather Type"
def train_model(df, target_column, n_estimators=100, max_depth=50, random_state=77):
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])
    
    y_train = df[target_column]
    X_train = df.drop(columns=[target_column])
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )

    model.fit(X_train, y_train)
    return model, scaler



if __name__ == "__main__":
    df = pd.read_csv(r"E:\Full Data Science Projects\Weather type classification\weather_classification_data.csv") 
    df =  data_pre(df)
    
    model, scaler = train_model(df, target_column='Weather Type')
    
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)
    with open("scaler.pkl", "wb") as file:
        pickle.dump(scaler, file)

