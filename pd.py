import pandas as pd

df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
print(df.head())
print(df.info())
print(df.describe())

df = pd.read_csv('dz.csv')
print(df)

df.fillna(value=0, inplace=True)

print(df)

group = df.groupby('City')['Salary'].mean()

print(group)
