import joblib
import numpy as np

model = joblib.load("../model/hydro_model.pkl")
# prédiction pour temp=30°C, humidity=75%
prediction = model.predict(np.array([[30,75]]))
print(f"Prédiction pluie : {prediction[0]} mm")
