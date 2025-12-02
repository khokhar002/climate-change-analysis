import os
import pandas as pd

folder = r"C:\Users\Vishakha Khokhar\Desktop\Project\raw_data\Global_temp"
out_csv = r"C:\Users\Vishakha Khokhar\Desktop\Project\raw_data\temperature_global.csv"

if os.path.exists(out_csv):
    os.remove(out_csv)

files = sorted([f for f in os.listdir(folder) if f.startswith("air_temp")])
first_write = True

for file in files:
    year = int(file.split(".")[1])
    path = os.path.join(folder, file)

    df = pd.read_csv(path, header=None, delim_whitespace=True)

    latitudes = df.iloc[0, 1:].astype(float).values
    longitudes = df.iloc[1:, 0].astype(float).values
    temps = df.iloc[1:, 1:]

    rows = []
    for i, lon in enumerate(longitudes):
        for j, lat in enumerate(latitudes):
            rows.append((year, lon, lat, temps.iloc[i, j]))

    year_df = pd.DataFrame(rows, columns=["Year", "Longitude", "Latitude", "Temperature"])
    year_df.to_csv(out_csv, mode="a", header=first_write, index=False)
    first_write = False

    print(f"Processed year: {year}")

print("Done! temperature_global.csv created.")
