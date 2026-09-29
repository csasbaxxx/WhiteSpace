import pandas as pd

print('I\'m trying to find the white car.')

df1 = pd.read_csv("LPR_2016-11-11.csv", parse_dates=["datetime"], low_memory=False)
#df1 = pd.read_csv("LPR_2016-11-07.csv", parse_dates=["datetime"])
df2 = pd.read_csv("VehicleRegistration_copy.csv", low_memory=False)

lp_list = ["LPR00130", "LPR00129", "LPR00191", "LPR00193", "LPR00192", "LPR00194", "LPR00034", "LPR00032", "LPR00035", "LPR00033", "LPR00233", "LPR00232", "LPR00234", "LPR00231"]

w1 = df1["datetime"].between(
    pd.Timestamp("2016-11-11T10:00:00-05:00"),
    pd.Timestamp("2016-11-11T10:11:30-05:00"),
)

#w2 = df["datetime"].between(
#    pd.Timestamp("2016-11-11T10:00:00-05:00"),
#    pd.Timestamp("2016-11-11T10:11:30-05:00"),
#)

df_match_lpr = df1[w1 & df1["lpr_id"].isin(lp_list)].copy()

white = df2[df2["Vehicle Color"].str.strip().str.upper() == "WHITE"]

df_result = df_match_lpr.merge(
    white,
    left_on="licenseplate",
    right_on="License Plate",
    how="inner",
    suffixes=("_lpr", "_reg"),
)

df_result.to_csv("11th_search_results.csv", index=False)

