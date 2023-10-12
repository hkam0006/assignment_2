import pandas as pd

df = pd.read_csv('./data_processing/number-of-deaths-by-risk-factor.csv')
df.dropna(inplace=True)

column_names = list(df.columns)

new_col_names = {
    column_names[3]: "High Systolic Blood Pressure",
    column_names[4]: "High sodium diet",
    column_names[5]: "Low whole grains diet",
    column_names[6]: "Alcohol use",
    column_names[7]: "Low fruits diet",
    column_names[8]: "Unsafe water source",
    column_names[9]: "Secondhand smoke",
    column_names[10]: "Low birth weight",
    column_names[11]: "Child wasting",
    column_names[12]: "Unsafe sex",
    column_names[13]: "Diet low in nuts and seeds",
    column_names[14]: "Household air pollution from solid fuels",
    column_names[15]: "Diet low in vegetables",
    column_names[16]: "Smoking",
    column_names[17]: "High fasting plasma glucose",
    column_names[18]: "Air pollution (indoor and outdoor)",
    column_names[19]: "High body-mass index",
    column_names[20]: "Unsafe sanitation",
    column_names[21]: "Drug use",
    column_names[22]: "Low bone mineral density",
    column_names[23]: "Vitamin a deficiency",
    column_names[24]: "Child stunting",
    column_names[25]: "Non-exclusive breastfeeding",
    column_names[26]: "Iron deficiency",
    column_names[27]: "Ambient particulate matter pollution",
    column_names[28]: "Low physical activity",
    column_names[29]: "No access to handwashing facility",
    column_names[30]: "High ldl cholesterol"
}
df.rename(columns=new_col_names, inplace=True)

df.drop(["Entity", "Code"], axis=1, inplace=True)

results = df.groupby('Year', as_index=False).sum()

print(results)

df_columns_names = list(df.columns)
df_columns_names = df_columns_names[1:]

rows_list = []

cardio_set = set(["High Systolic Blood Pressure", "High sodium diet", "Smoking",
                  "High fasting plasma glucose", "High body-mass index", "High ldl cholesterol"])

nutri_set = set(["Low whole grains diet", "Low fruits diet", "Diet low in nuts and seeds",
                 "Diet low in vegetables", "Low bone mineral density", "Vitamin a deficiency", "Low physical activity"])

environ_set = set(["Second Hand Smoke", "Unsafe water source",
                  "Unsafe sanitation", "No access to handwashing facility"])

maternal_set = set(["Low birth weight", "Child wasting", "Unsafe sex",
                   "Child stunting", "Non-exclusive breastfeeding", "Iron deficiency"])

substance_set = set(["Alcohol use", "Drug use"])

air_pollution_set = set(["Air pollution (indoor and outdoor)"])

for index, row in results.iterrows():
    year = row["Year"]
    cardio = {
        "Year": year,
        "Risk of Death": "Cardiovascular",
        "Number of Deaths": 0
    }
    nutri = {
        "Year": year,
        "Risk of Death": "Nutrition",
        "Number of Deaths": 0
    }
    environmental = {
        "Year": year,
        "Risk of Death": "Environmental",
        "Number of Deaths": 0
    }
    maternal = {
        "Year": year,
        "Risk of Death": "Maternal and Child Health",
        "Number of Deaths": 0
    }
    substance = {
        "Year": year,
        "Risk of Death": "Substance Use",
        "Number of Deaths": 0
    }
    air_pollution = {
        "Year": year,
        "Risk of Death": "Air Pollution",
        "Number of Deaths": 0
    }

    for col_name in df_columns_names:
        num_deaths = row[col_name]
        if col_name in cardio_set:
            cardio["Number of Deaths"] += num_deaths
        elif col_name in nutri_set:
            nutri["Number of Deaths"] += num_deaths
        elif col_name in environ_set:
            environmental['Number of Deaths'] += num_deaths
        elif col_name in maternal_set:
            maternal['Number of Deaths'] += num_deaths
        elif col_name in substance_set:
            substance["Number of Deaths"] += num_deaths
        elif col_name in air_pollution_set:
            air_pollution['Number of Deaths'] += num_deaths
    rows_list.append(cardio)
    rows_list.append(nutri)
    rows_list.append(environmental)
    rows_list.append(maternal)
    rows_list.append(substance)
    rows_list.append(air_pollution)


transformed_df = pd.DataFrame(rows_list)

print(transformed_df)

# transformed_df.to_csv(
# "/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data/deaths.csv", index=False)
