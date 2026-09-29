import pandas as pd

file_name = input('Enter the CSV file name (include the file extension): ').strip().strip('"\'') # Generlized for any file in same format. 

df = pd.read_csv(file_name)

df["report_date"] = pd.to_datetime(df["report_date"], format="%d-%m-%Y").dt.strftime("%Y-%m-%d")


# pull the "11/<day>" pattern out of the text column — swap 'pre-text' for your real column name
#extracted = df["pre-text"].str.extract(r'(11/\d{1,2})')[0]

#Maybe save below for later

# build a real datetime column, assuming year 2016
#df["datetime"] = pd.to_datetime(extracted + "/2016", format="%m/%d/%Y", errors="coerce")

df.to_csv("output_crime_reports_with_datetime.csv", index=False)

#Below is so I can copy and past in terminal while using VSC
# crime_reports.csv