import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFO ==========")
print(df.info())

print("\n========== MOVIES vs TV SHOWS ==========")
print(df["type"].value_counts())

print("\n========== TOP 10 COUNTRIES ==========")
print(df["country"].value_counts().head(10))

print("\n========== MOST COMMON GENRES ==========")
print(df["listed_in"].value_counts().head(10))
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Fill missing country values
df["country"].fillna("Unknown", inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
