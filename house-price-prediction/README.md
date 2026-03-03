# House Price Prediction (Machine Learning)

## Overview
This project predicts house prices using Machine Learning models.

Dataset contains 2000 records with features such as:
- Area
- Bedrooms
- Bathrooms
- Floors
- Year Built
- Location
- Condition
- Garage

Target variable: **Price**

## Tools Used
- Python
- Pandas
- Matplotlib
- Scikit-learn

## Models Implemented

### 1️ Linear Regression
Baseline regression model.

### 2️ Random Forest Regressor
Improved tree-based model.

## Model Performance

- Mean House Price: 537,676
- Random Forest MAE: 250,841
- Random Forest RMSE: 290,842

## Outputs
Saved in:
- images/actual_vs_predicted.png
- images/rf_actual_vs_predicted.png

## How To Run

```bash
cd house-price-prediction/src
python house_price_model.py