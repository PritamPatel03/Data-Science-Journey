import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nNumber of Movies and TV Shows:")
print(df["type"].value_counts())
