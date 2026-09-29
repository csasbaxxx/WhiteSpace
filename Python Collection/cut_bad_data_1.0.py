import pandas as pd
#import math used when rounding but not needed. 


Time_Dilly=int(input('This will cut dates you don\'t want and keep the ones you do want. What date do you want to keep? (7, 8, 9, 10, or 11) '))

Time_Dilly_ts = pd.Timestamp(year=2016, month=11, day=Time_Dilly)
Time_Dilly_ts_next = Time_Dilly_ts + pd.Timedelta(days=1)

Time_Dilly_td = Time_Dilly_ts.strftime('%Y-%m-%d')
Time_Dilly_td_next = Time_Dilly_ts_next.strftime('%Y-%m-%d')

file_name = input('Enter the CSV file name (include the file extension): ').strip().strip('"\'') # Generlized for any file in same format. 

df = pd.read_csv(file_name, parse_dates=["report_date"])

df2 = df[(df['report_date'] >= Time_Dilly_td) & (df['report_date'] < Time_Dilly_td_next)].copy()

df2.to_csv(f"Crime_Report_{Time_Dilly}th.csv", index=False)

#Below is so I can copy and past in terminal while using VSC
# output_crime_reports_with_datetime.csv