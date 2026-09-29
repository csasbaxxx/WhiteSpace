import pandas as pd
import glob

search_value = input('What MAC Addy are we looking for? ')
search_column = "mac"

files = glob.glob("WIFI_2016-11-**.csv")   # adjust the pattern to match your filenames

results = []
for f in files:
    df = pd.read_csv(f)
    if search_column in df.columns:
        matches = df[df[search_column] == search_value].copy()
        if not matches.empty:
            matches["source_file"] = f
            results.append(matches)

if results:
    combined = pd.concat(results, ignore_index=True)
    print(combined)
    combined.to_csv("search_results.csv", index=False)
else:
    print("No matches found.")