### 🌍 **Data-Driven Climate Change Impact Analysis**



A complete end-to-end data analysis project that examines global temperature rise, Indian monsoon rainfall patterns, and air pollution (AQI) using Python, Pandas, Matplotlib, and Jupyter Notebooks.



This project uses real climate datasets from open sources like Kaggle, NOAA, IMD, and CPCB to identify clear evidence of climate change.





##### 📁 Project Structure:





climate-change-analysis/

│

├── notebooks/

│   ├── EDA\_temperature.ipynb

│   ├── EDA\_rainfall.ipynb

│   ├── AQI\_analysis.ipynb

│

├── scripts/

│   ├── combine\_temperature.py

│   ├── clean\_all\_data.py

│   ├── stream\_yearly\_mean.py

│   ├── plot\_all.py

│

├── visuals/

│   ├── temp\_yearly\_mean.png

│   ├── rainfall\_yearly.png

│   ├── aqi\_city\_top10.png

│

├── README.md

└── requirements.txt





##### 📦 Dataset Sources





1\. Global Temperature Data



* Kaggle (Multiple yearly CSVs)



* NOAA Global Surface Temperature Data

&nbsp;  https://www.ncei.noaa.gov/



2\. Indian Rainfall Dataset



* IMD (Indian Meteorological Department)



* Kaggle: “Indian Rainfall Dataset”



3\. Air Quality / AQI Dataset



* Kaggle: Indian Air Quality Data



* CPCB India Air Quality Portal





##### ⚙️ Technologies Used



* Python



* Pandas / NumPy



* Matplotlib / Seaborn



* Jupyter Notebook



* GitHub



* Data Cleaning \& EDA



* Climate Analytics





##### 📊 Project Tasks \& Workflow







1\. Temperature Analysis



* Combined multiple year-wise files



* Extracted latitude, longitude, temperature



* Computed yearly mean global temperature



Identified warming trends



###### Key Insight:



📈 Global temperatures show a steady rise, with the fastest warming occurring after 1980.





✔ 2. Rainfall Analysis (India)



* Used subdivision-wise IMD monsoon data



* Focused on JUN–SEP rainfall



* Analyzed year-to-year rainfall variation



Key Insight:



🌧️ Rainfall shows high variability and more extreme events (floods/droughts) in recent decades.







3\. Air Quality / AQI Analysis



* Used dataset containing pollutants: PM2.5, PM10, NO₂, SO₂, OZONE



* Calculated AQI categories



* Identified most polluted cities



Key Insight:



😷 Northern India has extremely high PM2.5 levels; many cities fall in “Poor” to “Severe” AQI.





##### 📉 Generated Visuals



🟥 1. Global Yearly Mean Temperature



visuals/temp\_yearly\_mean.png

Shows increasing global temperature trend over the decades.



🟦 2. India Monsoon Rainfall Trend



visuals/rainfall\_yearly.png

Shows yearly rainfall variability and extreme climate events.



🟩 3. Top 10 Polluted Cities (PM2.5)



visuals/aqi\_city\_top10.png

Identifies highly polluted Indian cities using AQI.





##### 🧠 Key Findings



* 🌡 Global warming is clearly visible in temperature trends.



* 🌧 Rainfall patterns are unstable, with increased extreme events.



* 😷 Air pollution is dangerously high in many Indian cities.



* 🌍 Climate change shows multi-dimensional impact across temperature, rainfall, and pollution.































