from collections import defaultdict
import pandas as pd

disaster_df = pd.read_csv(
    "/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data_processing/disaster_data.csv")

print(disaster_df['Disaster Type'].unique())

# Start Year

year_dict = defaultdict(dict)

for index, row in disaster_df.iterrows():
    start_year = row['Start Year']
    disaster_type = row['Disaster Type']
    year_dict[start_year][disaster_type] = year_dict[start_year].get(
        disaster_type, 0) + 1

rows_list = []
total_count = 0
for year in year_dict.keys():
    total = 0
    for disaster in year_dict[year].keys():
        number = year_dict[year][disaster]
        rows_list.append({
            "Year": year,
            "Disaster": disaster,
            "Occurences": number
        })
        total += number
    rows_list.append({
        "Year": year,
        "Disaster": "Total",
        "Occurences": total
    })

df = pd.DataFrame(rows_list)
# print(df)
df.to_csv("/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data/natural_disaster.csv", index=False)
