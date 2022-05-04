import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer


df = pd.DataFrame(np.random.randint(0, 5, size=(100, 1)), columns=["aleatorio"])
df.to_csv("aleatorio.csv")

#función que calcule la media con el DataFrame creado antes y lo añada a la misma del

def __init__(self, df):
    media = df.mean()
    desviacion = df.std()
    print("Media: ", media)
    print("Desviacion: ", desviacion)
    
#función que te calcule la desviación estándar con el DataFrame creado antes y lo añada al mismo 




#segunda prueba para añadir columna

#ejemplo = pd.read_csv("ejemplo.csv", header= 0)
#df=pd.DataFrame(ejemplo)
#df.columna_random = np.random.rand(0,5)
#df.to_csv("ejemplo.csv", index=False)

#añadir columna a ejemplo.csv 
#ejemplo = pd.read_csv("ejemplo.csv", header= 0)
#df=pd.DataFrame(ejemplo)
#df.columna_random = np.random.rand(0,5)
#df.to_csv("ejemplo.csv", index=False)
