import pandas as pd

df = pd.read_csv('./data_processing/co-emissions-per-capita.csv')

df.dropna(inplace=True)
print(df)

for i, row in df.iterrows():
    year = row['Year']
    if not year == 2019:
        df.at[i, 'Year'] = None

df.dropna(inplace=True)
print(df)

df.to_csv("/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data/co2_emission_per_capita.csv", index=False)
