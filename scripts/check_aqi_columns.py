import pandas as pd
import os

aqi_file = r"C:\Users\Vishakha Khokhar\Desktop\Project\raw_data\aqi_india.csv"

df = pd.read_csv(aqi_file)
print(df.columns)
print(df.head())
