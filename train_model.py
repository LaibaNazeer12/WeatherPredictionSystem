import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Training started...")

# load dataset
df = pd.read_csv("weather.csv")

# split data
X = df.drop("Weather", axis=1)
y = df["Weather"]

# train model
model = RandomForestClassifier()
model.fit(X, y)

# save model (IMPORTANT)
joblib.dump(model, "model.pkl")

print("Model saved successfully ✅")