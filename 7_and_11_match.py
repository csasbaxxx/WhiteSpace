import pandas as pd

df1 = pd.read_csv("7th_search_results.csv", low_memory=False)
df2 = pd.read_csv("11th_search_results.csv", low_memory=False)

for d in (df1, df2):
    d["licenseplate"] = d["licenseplate"].astype(str).str.upper().str.replace(r"[\s-]", "", regex=True)

common = set(df1["licenseplate"]) & set(df2["licenseplate"])
print(len(common), common)