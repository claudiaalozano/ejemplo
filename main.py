import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer


df = pd.DataFrame(np.random.randint(0, 5, size=(100, 1)), columns=["aleatorio"])
df.to_csv("aleatorio.csv")


class a:
    def __init__(self, direccion):
        self.direccion = pd.read_csv(direccion)

    def media_desviacion(self):
        media = self.direccion["aleatorio"].mean()
        desviacion = self.direccion["aleatorio"].std()
        return media, desviacion, 
    def percentiles_mediana(self):
        percentiles = self.direccion["aleatorio"].quantile([0.25, 0.5, 0.75])
        mediana = self.direccion["aleatorio"].median()
        return percentiles, mediana
    def diagrama_de_barras(self):
        fig, ax = plt.subplots
        self.direccion["aleatorio"].plot(kind="pie" , ax = ax, title="Diagrama de Barras")
        plt.savefig("diagrama_de_barras.png")
        plt.show()

    def cuanto(self):
        i = 0
        for i in self.direccion["aleatorio"]:
            if i > 60:
                i += 1
            else:
                i = 0
        return i


archivo = a("aleatorio.csv")
print(archivo.media_desviacion())
print(archivo.percentiles_mediana())








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
