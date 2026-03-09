from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI(title="Predicción de Consumo Energético")

# 1. Simulación de datos (En un entorno profesional, esto vendría de una DB)
# Datos: [Temperatura Exterior, Horas de Uso] -> Consumo (kWh)
X_train = np.array([[15, 8], [20, 10], [25, 12], [30, 14], [10, 6]])
y_train = np.array([150, 210, 280, 350, 95])

# 2. Entrenamos el modelo al iniciar la API
modelo = LinearRegression()
modelo.fit(X_train, y_train)


@app.get("/")
def home():
    return {"mensaje": "Modelo de ML cargado y listo para predecir"}


@app.get("/predecir")
def predecir_consumo(temp: float, horas: float):
    # El modelo espera una lista de listas [[temp, horas]]
    entrada = np.array([[temp, horas]])
    prediccion = modelo.predict(entrada)[0]

    return {
        "input": {"temperatura": temp, "horas_operacion": horas},
        "prediccion_consumo_kwh": round(float(prediccion), 2),
    }
