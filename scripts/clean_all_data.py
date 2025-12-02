import pandas as pd
import os

raw_path = r"C:\Users\Vishakha Khokhar\Desktop\Project\raw_data"
clean_path = r"C:\Users\Vishakha Khokhar\Desktop\Project\cleaned_data"

# Make sure cleaned_data folder exists
if not os.path.exists(clean_path):
    os.makedirs(clean_path)

# ------------------ 1. CLEAN TEMPERATURE -------------------
temp_file = os.path.join(raw_path, "temperature_global.csv")
print("Loading:", temp_file)

temp = pd.read_csv(temp_file)

temp['Temperature'] = pd.to_numeric(temp['Temperature'], errors='coerce')
temp = temp[(temp['Temperature'] > -200) & (temp['Temperature'] < 60)]
temp.dropna(inplace=True)

temp.to_csv(os.path.join(clean_path, "temperature_global_clean.csv"), index=False)
print("✔ Cleaned: Temperature")

# ------------------ 2. CLEAN RAINFALL -------------------
rain_file = os.path.join(raw_path, "rainfall_india.csv")
print("Loading:", rain_file)

rain = pd.read_csv(rain_file)
rain.dropna(inplace=True)

rain.to_csv(os.path.join(clean_path, "rainfall_india_clean.csv"), index=False)
print("✔ Cleaned: Rainfall")

# ------------------ 3. CLEAN AQI -------------------
aqi_file = os.path.join(raw_path, "aqi_india.csv")
print("Loading:", aqi_file)

aqi = pd.read_csv(aqi_file)

# Keep only required columns
aqi = aqi[['country','state','city','station','pollutant_id','pollutant_avg']]

# Rename for clarity
aqi.rename(columns={'pollutant_id':'Pollutant', 'pollutant_avg':'Value'}, inplace=True)

# Drop missing values
aqi.dropna(subset=['Value'], inplace=True)
aqi['Value'] = pd.to_numeric(aqi['Value'], errors='coerce')

aqi.dropna(subset=['Value'], inplace=True)

aqi.to_csv(os.path.join(clean_path, "aqi_india_clean.csv"), index=False)

print("✔ Cleaned: AQI Pollution Data")

print("\n🎉 All files cleaned successfully!")

