
import pandas as pd
import numpy as np


data = {
    "Nombre": [
        "Ana", "Luis", "Carla", "Pedro", "Laura", "Jorge", "Sofía", "Miguel",
        "Camila", "David", "Susana", "Fernando", "Irene", "Pablo", "Marta",
        "Diego", "Cristina", "Antonio", "Raquel", "Mario"
    ],
    "Edad": [
        18, 20, 19, 21, 19, 18, 20, 22, 19, 21, 18, 23, 19, 20, 18, 21, 22, 20, 19, 22
    ],
    "Genero": [
        "F", "M", "F", "M", "F", "M", "F", "M","F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"
    ],
    "Matematicas": [
        80, 85, 90, 70, 75, 88, 92, 78, 65, 89, 66, 74, 81, 92, 77, 83, 79, 84, 68, 91
    ],
    "Fisica": [
        85, 90, 75, 88, 82, 70, 89, 76, 73, 85, 78, 70, 68, 95, 82, 80, 87, 89, 91, 73
    ],
    "Quimica": [
        90, 87, 80, 94, 76, 88, 84, 79, 82, 77, 75, 69, 78, 90, 81, 85, 88, 80, 92, 78
    ],
    "Aprobado": [
        True, True, True, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True
    ]
}

df = pd.DataFrame(data)
print(df.head(5))

def multiplicacion(a,b):
    return a*b