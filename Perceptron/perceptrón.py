# -*- coding: utf-8 -*-
"""Perceptrón.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lshdcPZ0L4gu5xctf3Psp-Mt6khAXVkE
"""

#Elaborado por : Cesar Rogelio Turner Minaya
import numpy as np

# Definimos las funciones de activación
def funcion_lineal(y):
    return y

def funcion_escalon(y):
    return 1 if y >= 0 else 0

def funcion_sigmoide(y):
    return 1 / (1 + np.exp(-y))

def funcion_relu(y):
    return max(0, y)

# Algoritmo de entrenamiento
def algoritmo_entrenamiento(X, D, alpha, funcion_activacion, max_epochs=10000):
    n, m = X.shape  # n = número de ejemplos, m = número de características
    W = np.random.uniform(-1, 1, m)  # Inicializamos los pesos aleatoriamente
    theta = np.random.uniform(-1, 1)  # Inicializamos el umbral aleatoriamente

    for epoch in range(max_epochs):
        total_error = 0
        for i in range(n):
            # Propagar: calcular Y
            Y = np.dot(X[i], W) - theta
            y_pred = funcion_activacion(Y)

            # Calcular el error
            error = D[i] - y_pred
            total_error += abs(error)

            # Retropropagación: actualizar los pesos y el umbral
            W += alpha * error * X[i]
            theta -= alpha * error

        # Verificar si el error total es aceptable
        if total_error == 0:
            break

    return W, theta

# Ejemplo de uso con diferentes funciones de activación
if __name__ == "__main__":
    # Datos de entrenamiento (X) y salidas deseadas (D)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    D = np.array([0, 1, 1, 0])  # Ejemplo para compuerta XOR
    alpha = 0.1  # Coeficiente de aprendizaje

    # Lista de funciones de activación
    funciones = {
        "Lineal": funcion_lineal,
        "Escalón": funcion_escalon,
        "Sigmoide": funcion_sigmoide,
        "ReLU": funcion_relu
    }

    # Entrenamos el modelo para cada función de activación
    for nombre, funcion in funciones.items():
        print(f"\nEntrenando con función de activación: {nombre}")
        W, theta = algoritmo_entrenamiento(X, D, alpha, funcion)
        print("Pesos entrenados:", W)
        print("Umbral entrenado:", theta)