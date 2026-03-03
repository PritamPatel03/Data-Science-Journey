import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 1) Load dataset
df = pd.read_csv("../data/House Price Prediction Dataset.csv", encoding="latin1")

# 2) Separate features (X) and target (y)
y = df["Price"]

# Drop Id because it's just an identifier, not a useful feature
X = df.drop(columns=["Price", "Id"])

# 3) Convert categorical columns to numeric (One-Hot Encoding)
# Location, Condition, Garage are categorical
X = pd.get_dummies(X, drop_first=True)

print("Final feature columns:", X.columns.tolist())
print("X shape:", X.shape)

# 4) Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5) Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6) Predict
y_pred = model.predict(X_test)

# 7) Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n===== MODEL PERFORMANCE =====")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# 8) Plot: Actual vs Predicted (save + show)
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted House Prices")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.tight_layout()
plt.savefig("../images/actual_vs_predicted.png")
plt.show()

# 9) Feature importance (Linear Regression coefficients)
coef_df = pd.DataFrame({
    "feature": X.columns,
    "coefficient": model.coef_
}).sort_values(by="coefficient", ascending=False)

print("\n===== TOP POSITIVE COEFFICIENTS =====")
print(coef_df.head(10))

print("\n===== TOP NEGATIVE COEFFICIENTS =====")
print(coef_df.tail(10))

# 10) Random Forest model (usually better)
rf = RandomForestRegressor(n_estimators=300, random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

print("\n===== RANDOM FOREST PERFORMANCE =====")
print("RF MAE:", round(rf_mae, 2))
print("RF RMSE:", round(rf_rmse, 2))

# Plot RF: Actual vs Predicted (save + show)
plt.scatter(y_test, rf_pred)
plt.title("Random Forest: Actual vs Predicted")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.tight_layout()
plt.savefig("../images/rf_actual_vs_predicted.png")
plt.show()

print("\nPrice Statistics:\n", df["Price"].describe())