import pandas as pd

# Load dataset
df = pd.read_csv("../data/netflix_titles.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nNumber of Movies and TV Shows:")
print(df["type"].value_counts())
import matplotlib.pyplot as plt

counts = df['type'].value_counts()

counts.plot(kind='bar')
plt.title("Number of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("../imgs/movies_vs_tv.png")
plt.show()
# Top 10 Countries with Most Content
print("\nTop 10 Countries with Most Content:")

# Remove missing values
country_data = df['country'].dropna()

# Split multiple countries and count separately
all_countries = country_data.str.split(', ').explode()

top_countries = all_countries.value_counts().head(10)

print(top_countries)

# Plot
top_countries.plot(kind='bar')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("../imgs/top_countries.png")
plt.show()
# Year-wise Release Trend
print("\nContent Release Trend by Year:")

year_counts = df['release_year'].value_counts().sort_index()

print(year_counts.tail(10))  # last 10 years

# Plot
year_counts.plot(kind='line')
plt.title("Netflix Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.savefig("../imgs/release_trend.png")
plt.show()
