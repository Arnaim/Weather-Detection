import warnings
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from class_preproccising import data_pre
warnings.filterwarnings('ignore')

# Load and preprocess the data
df = pd.read_csv(r"weather_classification_data.csv")
df = data_pre(df)

# Separate features and target
target_column = "Weather Type"
X = df.drop(columns=[target_column])
y = df[target_column]

# Define column types
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Create pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, max_depth=50, random_state=77))
])

# Fit model
pipeline.fit(X, y)

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(pipeline, file)
