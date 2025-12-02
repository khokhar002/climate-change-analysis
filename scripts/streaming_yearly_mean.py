# streaming_yearly_mean.py
import pandas as pd
from collections import defaultdict
import os, gc

infile = r"C:\Users\Vishakha Khokhar\Desktop\Project\cleaned_data\temperature_global_clean.csv"
out_yearly = r"C:\Users\Vishakha Khokhar\Desktop\Project\cleaned_data\temperature_yearly_mean.csv"

chunksize = 2_000_000  # reduce if still large
sum_by_year = defaultdict(float)
count_by_year = defaultdict(int)

usecols = ['Year','Temperature']  # only read what we need

for chunk in pd.read_csv(infile, usecols=usecols, chunksize=chunksize):
    # ensure numeric and drop NaNs only in chunk (cheap)
    chunk['Temperature'] = pd.to_numeric(chunk['Temperature'], errors='coerce')
    chunk = chunk.dropna(subset=['Temperature','Year'])
    chunk['Year'] = pd.to_numeric(chunk['Year'], errors='coerce').astype(int)

    grp = chunk.groupby('Year')['Temperature'].agg(['sum','count']).reset_index()
    for _, row in grp.iterrows():
        y = int(row['Year'])
        sum_by_year[y] += float(row['sum'])
        count_by_year[y] += int(row['count'])

    del chunk, grp
    gc.collect()

# finalize mean
years = sorted(sum_by_year.keys())
out_rows = []
for y in years:
    out_rows.append({'Year': y, 'MeanTemperature': sum_by_year[y] / count_by_year[y]})

pd.DataFrame(out_rows).to_csv(out_yearly, index=False)
print("Saved yearly mean to", out_yearly)
