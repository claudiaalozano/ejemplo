import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from csv import writer

with open("ejemplo.csv", "a" , newline= " ") as a f_object:
    writer_obect = writer(f_object)
    columna_random = np.random.rand(0,5, size=len(df1))
    writer_obect.writerow(columna_random)
    f_object.close()
    
