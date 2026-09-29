import numpy as np
import pandas as pd

# need Haversine formula 
def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000
    lar1, lar2 = np.radians(lat1), np.radians(lat2)
    dlar = lar2 - lar1
    lonr1, lonr2 = np.radians(lon1), np.radians(lon2)
    dlonr = (lonr2 - lonr1)
    a = np.sin(dlar/2)**2 + np.cos(lar1) * np.cos(lar2) * np.sin(dlonr/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

print('I\'m trying to find a MAC address that appears close to two very specific locations.')

file_name1 = 'WIFI_2016-11-07.csv'
df1 = pd.read_csv(file_name1, parse_dates=["datetime"])
file_name2 = 'WIFI_2016-11-11.csv'
df2 = pd.read_csv(file_name2, parse_dates=["datetime"])

compare_lat1 = 39.29699
compare_long1 = -76.66485

compare_lat2 = 39.298172
compare_long2 = -76.665271

dist = df1.apply(
    lambda r: haversine_m(compare_lat1, compare_long1, r["sensor_latitude"], r["sensor_longitude"]),
    axis=1
)
df1_near = df1[dist <= 100].copy()

dist = df2.apply(
    lambda r: haversine_m(compare_lat2, compare_long2, r["sensor_latitude"], r["sensor_longitude"]),
    axis=1
)
df2_near = df2[dist <= 100].copy()

merged_df = df1_near.merge(df2_near, on="mac", how="inner", suffixes=("_1", "_2"))

if merged_df.empty:
    print("No matches found")
else:
    merged_df.to_csv("merged_data.csv", index=False)

