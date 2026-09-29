import numpy as np
import pandas as pd


def haversine_measure(lat1, lon1, lat2, lon2):
    R = 6371000
    lar1, lar2 = np.radians(lat1), np.radians(lat2)
    dlar = lar2 - lar1
    lonr1, lonr2 = np.radians(lon1), np.radians(lon2)
    dlonr = (lonr2 - lonr1)
    a = np.sin(dlar/2)**2 + np.cos(lar1) * np.cos(lar2) * np.sin(dlonr/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

Time_Dilly=float(input('Welcome to Dilly-Dally! Please input the length of time for your dwell time in minutes: '))

Time_Dilly=round(Time_Dilly,-1) ## This is because time stamps change in incriments of 10min on the ankle monitor. 

Time_Dilly_td = pd.Timedelta(minutes=Time_Dilly)

Rad_Dally=float(input('Please input the radius of the circle you consider a dwelling instance in meters: '))

file_name = input('Enter the CSV file name (include the file extension): ').strip().strip('"\'') # Generlized for any file in same format. 
####df = pd.read_csv(file_name, parse_dates=["datetime"])

df = pd.read_csv(file_name, parse_dates=["datetime"])
stop_pos = "2016-11-07 00:00:30-05:00"
df2 = df[df['datetime'] <= stop_pos].copy()

mean_lat = df2["location_y"].mean()
mean_lon = df2["location_x"].mean()

print(df2.head())
print(mean_lat)
print(mean_lon)

# JaredCombs_Ankle_Monitor.csv