import pandas as pd
import glob

search_addresses = pd.read_csv("HomeLocationRegistry_Copy.csv")[["mac", "firstname", "lastname", "middlename", "ssn"]]
search_column = "mac"

files = glob.glob("WIFI_2016-11-*.csv")

results = []
for f in files:
    df = pd.read_csv(f)
    if search_column in df.columns:
        matches = df.merge(search_addresses, on="mac", how="inner")
        if not matches.empty:
            matches["source_file"] = f
            results.append(matches)

if results:
    combined = pd.concat(results, ignore_index=True)
    print(combined)
    combined.to_csv("search_results.csv", index=False)
else:
    print("No matches found.")