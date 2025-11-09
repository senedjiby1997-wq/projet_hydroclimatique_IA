import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("../data/sample_weather.csv")
X = df[['temp','humidity']]
y = df['rainfall']

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "../model/hydro_model.pkl")
print("Modèle entraîné et sauvegardé !")
