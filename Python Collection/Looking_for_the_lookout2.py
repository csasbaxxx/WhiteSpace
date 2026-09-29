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

print('I\'m trying to find any MAC address near locations.')

df = pd.read_csv("search_results.csv", parse_dates=["datetime"], low_memory=False)

compare_lat1 = 39.29699
compare_long1 = -76.66485

compare_lat2 = 39.298172
compare_long2 = -76.665271

w1 = df["datetime"].between(
    pd.Timestamp("2016-11-07T10:10:00-05:00"),
    pd.Timestamp("2016-11-07T10:10:30-05:00"),
)
w2 = df["datetime"].between(
    pd.Timestamp("2016-11-11T10:00:00-05:00"),
    pd.Timestamp("2016-11-11T10:25:30-05:00"),
)

d1 = df[w1]
d2 = df[w2]

near1 = d1[haversine_m(compare_lat1, compare_long1,
                       d1["sensor_latitude"], d1["sensor_longitude"]) <= 100]
near2 = d2[haversine_m(compare_lat2, compare_long2,
                       d2["sensor_latitude"], d2["sensor_longitude"]) <= 100]

df_near = pd.concat([near1, near2])
df_near.to_csv("output_search_results.csv", index=False)

