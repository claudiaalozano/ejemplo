import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer

with open("ejemplo.csv", "a" , newline= " ") as f_object:
    writer_object = writer(f_object)
    columna_random = np.random.rand(0,5)
    writer_object.writerow(columna_random)
    f_object.close()

#segunda prueba para añadir columna

ejemplo = pd.read_csv("ejemplo.csv", header= 0)
df=pd.DataFrame(ejemplo)
df.columna_random = np.random.rand(0,5)
df.to_csv("ejemplo.csv", index=False)