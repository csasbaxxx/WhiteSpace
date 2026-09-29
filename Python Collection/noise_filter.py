import pandas as pd
import numpy as np

# need Haversine formula 
def haversine_np(lat1, lon1, lat2, lon2):
    R = 6371000
    lar1, lar2 = np.radians(lat1), np.radians(lat2)
    dlar = lar2 - lar1
    lonr1, lonr2 = np.radians(lon1), np.radians(lon2)
    dlonr = (lonr2 - lonr1)
    a = np.sin(dlar/2)**2 + np.cos(lar1) * np.cos(lar2) * np.sin(dlonr/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

ankle = pd.read_csv("JaredCombs_Ankle_Monitor.csv")
dwells = pd.read_csv("29min_dwell_points.csv")

# distance from every ankle point to every dwell point, in meters
lat1 = ankle["location_y"].values[:, None]
lon1 = ankle["location_x"].values[:, None]
lat2 = dwells["mean_lat"].values[None, :]
lon2 = dwells["mean_long"].values[None, :]

min_dist = haversine_np(lat1, lon1, lat2, lon2).min(axis=1)

ankle_noise_filtered = ankle[min_dist > 50].copy()
ankle_noise_filtered.to_csv("ankle_monitor_noise_filtered.csv", index=False)

#Start of seperate file by days

initial=7

while initial < 12 :
    Time_Dilly = initial
    Time_Dilly_ts = pd.Timestamp(year=2016, month=11, day=Time_Dilly, tz='America/New_York')
    Time_Dilly_ts_next = Time_Dilly_ts + pd.Timedelta(days=1)

    Time_Dilly_td = Time_Dilly_ts.isoformat(timespec='milliseconds')
    Time_Dilly_td_next = Time_Dilly_ts_next.isoformat(timespec='milliseconds')

    file_name = 'ankle_monitor_noise_filtered.csv'

    df = pd.read_csv(file_name, parse_dates=["datetime"])

    df2 = df[(df['datetime'] >= Time_Dilly_td) & (df['datetime'] < Time_Dilly_td_next)].copy()

    df2.to_csv(f"Jared_Combs_{Time_Dilly}th.csv", index=False)
    initial = initial +1