# plot_all.py
import os
import pandas as pd
import matplotlib.pyplot as plt

# --------- PATHS (change if needed) ----------
base = r"C:\Users\Vishakha Khokhar\Desktop\Project"
clean_path = os.path.join(base, "cleaned_data")
visuals = os.path.join(base, "visuals")
os.makedirs(visuals, exist_ok=True)

# --------- 1) Global yearly mean temperature ----------
temp_file = os.path.join(clean_path, "temperature_global_clean.csv")
print("Loading temp:", temp_file)
temp = pd.read_csv(temp_file)

# ensure numeric
temp['Temperature'] = pd.to_numeric(temp['Temperature'], errors='coerce')
temp = temp.dropna(subset=['Temperature','Year'])

# yearly global mean
yearly_temp = temp.groupby('Year')['Temperature'].mean().reset_index()

plt.figure(figsize=(10,5))
plt.plot(yearly_temp['Year'], yearly_temp['Temperature'], marker='o')
plt.title("Global Yearly Mean Temperature")
plt.xlabel("Year")
plt.ylabel("Mean Temperature")
plt.grid(alpha=0.3)
fn = os.path.join(visuals, "temp_yearly_mean.png")
plt.savefig(fn, bbox_inches='tight')
plt.close()
print("Saved:", fn)

# --------- 2) Rainfall trend (yearly) ----------
rain_file = os.path.join(clean_path, "rainfall_india_clean.csv")
print("Loading rainfall:", rain_file)
rain = pd.read_csv(rain_file)

# Try detect columns: common formats Year / Year, Rainfall or Date / Rainfall
if 'Year' in rain.columns:
    rain['Year'] = pd.to_numeric(rain['Year'], errors='coerce')
else:
    # try extracting year from 'Date' if present
    if 'Date' in rain.columns:
        rain['Year'] = pd.to_datetime(rain['Date'], errors='coerce').dt.year
    else:
        raise SystemExit("Rainfall file has no Year or Date column. Check rainfall_india_clean.csv")

# assume rainfall amount column is named like 'Rainfall' or 'rainfall' or 'Precipitation'
possible_cols = ['Rainfall','rainfall','Precipitation','precipitation','Amount','amount']
rain_col = next((c for c in possible_cols if c in rain.columns), None)
if rain_col is None:
    # fallback: use the numeric column other than Year
    num_cols = [c for c in rain.columns if pd.api.types.is_numeric_dtype(rain[c]) and c != 'Year']
    if len(num_cols) >= 1:
        rain_col = num_cols[0]
    else:
        raise SystemExit("Couldn't find rainfall numeric column. Inspect rainfall_india_clean.csv")

yearly_rain = rain.groupby('Year')[rain_col].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(yearly_rain['Year'], yearly_rain[rain_col], marker='o')
plt.title("India Yearly Total Rainfall")
plt.xlabel("Year")
plt.ylabel(f"Total {rain_col}")
plt.grid(alpha=0.3)
fn = os.path.join(visuals, "rainfall_yearly.png")
plt.savefig(fn, bbox_inches='tight')
plt.close()
print("Saved:", fn)

# --------- 3) Pollution -> simple PM2.5-derived AQI & top cities ----------
aqi_clean = os.path.join(clean_path, "aqi_india_clean.csv")
print("Loading pollution:", aqi_clean)
poll = pd.read_csv(aqi_clean)

# Keep numeric Value column and pollutant name
poll['Value'] = pd.to_numeric(poll['Value'], errors='coerce')
poll = poll.dropna(subset=['Value'])

# Simple PM2.5->AQI mapping (example breakpoints)
def pm25_to_aqi(x):
    # use simple mapping; you can replace with official breakpoints later
    if x <= 30: return 50
    elif x <= 60: return 100
    elif x <= 90: return 200
    elif x <= 120: return 300
    elif x <= 250: return 400
    else: return 500

pm25 = poll[poll['Pollutant'].str.upper() == 'PM2.5'.upper()].copy()
if pm25.empty:
    print("Warning: no PM2.5 records found. Top-pollutants plot will use pollutant averages instead.")
else:
    pm25['AQI'] = pm25['Value'].apply(pm25_to_aqi)
    # if you have a date column, extract year; else group by station or city
    if 'Date' in pm25.columns:
        pm25['Year'] = pd.to_datetime(pm25['Date'], errors='coerce').dt.year
    # yearly average AQI (nationwide)
    if 'Year' in pm25.columns:
        yearly_aqi = pm25.groupby('Year')['AQI'].mean().reset_index()
        plt.figure(figsize=(10,5))
        plt.plot(yearly_aqi['Year'], yearly_aqi['AQI'], marker='o')
        plt.title("India Average AQI (from PM2.5)")
        plt.xlabel("Year"); plt.ylabel("AQI")
        plt.grid(alpha=0.3)
        fn = os.path.join(visuals, "aqi_trend_pm25.png")
        plt.savefig(fn, bbox_inches='tight'); plt.close()
        print("Saved:", fn)
    # top 10 cities by PM2.5 average
    top_cities = (pm25.groupby('city')['Value'].mean()
                       .sort_values(ascending=False).head(10).reset_index())
    plt.figure(figsize=(10,6))
    plt.barh(top_cities['city'][::-1], top_cities['Value'][::-1])
    plt.xlabel("PM2.5 (avg)"); plt.title("Top 10 Cities by PM2.5")
    fn = os.path.join(visuals, "aqi_city_top10.png")
    plt.savefig(fn, bbox_inches='tight'); plt.close()
    print("Saved:", fn)

# --------- 4) Quick temperature scatter for one sample year (heatmap-like) ----------
# pick a year that exists (e.g., median year)
available_years = sorted(temp['Year'].unique())
if available_years:
    sample_year = available_years[len(available_years)//2]
    s = temp[temp['Year'] == sample_year].copy()
    # convert lat/lon to numeric
    s['Latitude'] = pd.to_numeric(s['Latitude'], errors='coerce')
    s['Longitude'] = pd.to_numeric(s['Longitude'], errors='coerce')
    s = s.dropna(subset=['Latitude','Longitude','Temperature'])
    plt.figure(figsize=(12,6))
    plt.scatter(s['Longitude'], s['Latitude'], c=s['Temperature'], s=6)
    plt.colorbar(label='Temperature')
    plt.title(f"Temperature grid scatter ({sample_year})")
    plt.xlabel("Longitude"); plt.ylabel("Latitude")
    fn = os.path.join(visuals, f"temp_world_scatter_{sample_year}.png")
    plt.savefig(fn, bbox_inches='tight'); plt.close()
    print("Saved:", fn)
else:
    print("No years found in temperature data; skip world scatter.")

print("\nAll plots done. Check folder:", visuals)
