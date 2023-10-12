import pandas as pd

df = pd.read_csv("./data_processing/global_temperature.csv")

df['Category'] = None

for index, row in df.iterrows():
    if row['Anomaly'] < 0:
        df.at[index, 'Category'] = "Below"
    else:
        df.at[index, 'Category'] = "Above"

print(df)

df.to_csv("/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data/global_temp.csv", index=False)
