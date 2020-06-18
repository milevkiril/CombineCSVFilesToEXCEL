import pandas as pd
import numpy as np
import os, collections, csv
from datetime import datetime
from os.path import basename

start_counter = datetime.now()
pathName = 'D:\\Kircata\\Python Projects\\CombineCSVFiles\\CSV files'
filesToRead = ['recurring_turning_on_and_off_2018.04.csv', 'recurring_turning_on_and_off_2018.05.csv', 'recurring_turning_on_and_off_2018.06.csv'];

df = []
numberOfFiles = 2
i = 1

for file in filesToRead:
    if i == 1:
        data = pd.read_csv(os.path.join(pathName, file), encoding='cp1251', delimiter = ',', header = None)#.fillna("0")
    else:
        data = pd.read_csv(os.path.join(pathName, file), skiprows = 1, encoding='cp1251', delimiter = ',', header = None)#.fillna("0")  

    df.append(data)
    i = i + 1

final = "D:\\Kircata\\Python Projects\\CombineCSVFiles\\CSV files\\Combined.xlsx"
df = pd.concat(df)
df.to_excel(final)

print("done")

load_duration = datetime.now() - start_counter
print(load_duration)