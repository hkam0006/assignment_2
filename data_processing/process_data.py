import pandas as pd

df = pd.read_csv('./data_processing/number-of-deaths-by-risk-factor.csv')

for i, row in df.iterrows():
    year = row['Year']
    if year != 2019:
        df.at[i, 'Year'] = None

df.dropna(inplace=True)

print(df)

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
    column_names[18]: "Air pollution",
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

df['Total Air Pollution Deaths'] = df["Ambient particulate matter pollution"] + \
    df["Household air pollution from solid fuels"] + df['Air pollution']

df.drop(["Ambient particulate matter pollution",
        "Household air pollution from solid fuels", 'Air pollution'], axis=1, inplace=True)

df.rename(
    columns={'Total Air Pollution Deaths': "Air Pollution"}, inplace=True)

df.to_csv("/Users/sonnykam/Documents/Monash_Uni/FIT3179/assignment_2/assignment_2/data/deaths.csv", index=False)
