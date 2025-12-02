import pandas as pd
import numpy as np

path = r"C:\Users\Vishakha Khokhar\Desktop\Project\cleaned_data\aqi_india_clean.csv"
df = pd.read_csv(path)

# AQI breakpoints (simple, PM2.5 only for now)
def pm25_to_aqi(x):
    if x <= 30: return 50
    elif x <= 60: return 100
    elif x <= 90: return 200
    elif x <= 120: return 300
    elif x <= 250: return 400
    else: return 500

# Filter PM2.5 rows only
pm25 = df[df['Pollutant']=='PM2.5'].copy()

pm25['AQI'] = pm25['Value'].apply(pm25_to_aqi)

pm25.to_csv(r"C:\Users\Vishakha Khokhar\Desktop\Project\cleaned_data\aqi_final.csv", index=False)

print("✔ AQI calculated and saved to aqi_final.csv")
