import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/Superstore.csv", encoding="latin1")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Monthly Sales Trend
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# -----------------------------
# 1) Monthly Sales Trend (SAVE)
# -----------------------------
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/monthly_sales_trend.png")
plt.show()

# -----------------------------
# 2) Top 10 Products by Sales
# -----------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Sales:")
print(top_products)

top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../images/top_10_products_sales.png")
plt.show()

# -----------------------------
# 3) Profit by Region
# -----------------------------
profit_by_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

print("\nProfit by Region:")
print(profit_by_region)

profit_by_region.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../images/profit_by_region.png")
plt.show()

# -----------------------------
# 4) Top 10 Loss-Making Products
# -----------------------------
loss_products = df.groupby("Product Name")["Profit"].sum().sort_values().head(10)

print("\nTop 10 Loss-Making Products:")
print(loss_products)

loss_products.plot(kind="bar")
plt.title("Top 10 Loss-Making Products (Negative Profit)")
plt.xlabel("Product Name")
plt.ylabel("Total Profit")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../images/top_10_loss_products.png")
plt.show()