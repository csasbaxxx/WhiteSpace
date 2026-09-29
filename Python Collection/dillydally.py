import numpy as np
import pandas as pd
#import math used when rounding but not needed. 

# need Haversine formula 
def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000
    lar1, lar2 = np.radians(lat1), np.radians(lat2)
    dlar = lar2 - lar1
    lonr1, lonr2 = np.radians(lon1), np.radians(lon2)
    dlonr = (lonr2 - lonr1)
    a = np.sin(dlar/2)**2 + np.cos(lar1) * np.cos(lar2) * np.sin(dlonr/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

Time_Dilly=float(input('Welcome to Dilly-Dally! Please input the length of time for your dwell time in minutes: '))

#####Below is when I thought the ankle monitor was in 10 minute increments. But it is in 10 second increments. 

#if Time_Dilly <= 4:  #This is used so that we don't round down to zero minutes. 
#    Time_Dilly = math.ceil(Time_Dilly / 10) * 10

#Time_Dilly=round(Time_Dilly,-1) ## This used because time stamps change in incriments of 10min on the ankle monitor. 

#####Above is when I thought the ankle monitor was in 10 minute increments. But it is in 10 second increments. 

Time_Dilly_td = pd.Timedelta(minutes=Time_Dilly) #converts minutes to whatever this is "0 days 00:45:20"

Rad_Dally=float(input('Please input the radius of the circle you consider a dwelling instance in meters: '))

file_name = input('Enter the CSV file name (include the file extension): ').strip().strip('"\'') # Generlized for any file in same format. 

df = pd.read_csv(file_name, parse_dates=["datetime"])

anchor_pos = 0
segments = []

while anchor_pos < len(df) - 1: #Start of while loop
    anchor = df.iloc[anchor_pos]
    rest = df.iloc[anchor_pos + 1:]

    # 1. Distance from the anchor to rest
    dist = haversine_m(anchor["location_y"], anchor["location_x"], rest["location_y"], rest["location_x"])
    over = dist >= Rad_Dally

    # 2. Where does this group end?
    if over.any():
        stop_pos = df.index.get_loc(over.idxmax())
    else:
        stop_pos = len(df)            # never crossed, so the current group runs to the end of the file

    # 3. Define the group: anchor row up to, but NOT including, the stopping row
    group = df.iloc[anchor_pos:stop_pos]

    # 4. Is this larger than "Time_Dilly_td"?
    duration = group["datetime"].iloc[-1] - group["datetime"].iloc[0]    # last timestamp in group minus first

    if duration >= Time_Dilly_td: #If yes, record this data. 
        mean_lat = group["location_y"].mean()
        mean_long = group["location_x"].mean()
        segments.append({"start": anchor["datetime"], "stop": group["datetime"].iloc[-1], "duration": duration, "mean_lat": mean_lat, "mean_long": mean_long})

    # 5. New anchor
    anchor_pos = stop_pos

# After the loop create dwell_points.csv
pd.DataFrame(segments, columns=["start", "stop", "duration", "mean_lat", "mean_long"]).to_csv("dwell_points.csv", index=False) # This is so an empty result will at least pass something

# pd.DataFrame(segments).to_csv("dwell_points.csv", index=False) This was the old output
#Below is so I can copy and past in terminal while using VSC
# JaredCombs_Ankle_Monitor.csv