import pandas as pd
import numpy as np
import os, collections, csv
from datetime import datetime
from os.path import basename

start_counter = datetime.now()
pathName = 'D:\\Kircata\\Python Projects\\CombineCSVFiles\\CSV files'
filesToRead = ['recurring_turning_on_and_off_2018.04.csv', 'recurring_turning_on_and_off_2018.05.csv', 'recurring_turning_on_and_off_2018.06.csv',
               'recurring_turning_on_and_off_2018.07.csv', 'recurring_turning_on_and_off_2018.08.csv', 'recurring_turning_on_and_off_2018.09.csv',
               'recurring_turning_on_and_off_2018.10.csv', 'recurring_turning_on_and_off_2018.11.csv', 'recurring_turning_on_and_off_2018.12.csv',
               'recurring_turning_on_and_off_2019.01.csv', 'recurring_turning_on_and_off_2019.02.csv', 'recurring_turning_on_and_off_2019.03.csv',
               'recurring_turning_on_and_off_2019.04.csv', 'recurring_turning_on_and_off_2019.05.csv', 'recurring_turning_on_and_off_2019.06.csv',
               'recurring_turning_on_and_off_2019.07.csv', 'recurring_turning_on_and_off_2019.08.csv', 'recurring_turning_on_and_off_2019.09.csv',
               'recurring_turning_on_and_off_2019.10.csv', 'recurring_turning_on_and_off_2019.11.csv', 'recurring_turning_on_and_off_2019.12.csv',
               'recurring_turning_on_and_off_2020.01.csv', 'recurring_turning_on_and_off_2020.02.csv', 'recurring_turning_on_and_off_2020.03.csv',
               'recurring_turning_on_and_off_2020.04.csv', 'recurring_turning_on_and_off_2020.05.csv'];

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