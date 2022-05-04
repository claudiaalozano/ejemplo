import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer


df = pd.DataFrame(np.random.randint(0, 5, size=(100, 1)), columns=["aleatorio"])
df.to_csv("aleatorio.csv")


class arch:
    def __init__(self, df):
        self.df = pd.read_csv(df)

        def media_desviacion(self):
            media = self.df["aleatorio"].mean()
            desviacion = self.df["aleatorio"].std()
            return media, desviacion

archivo = arch("aleatorio.csv") #instancia de la clase
print(archivo.media_desviacion())





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
