
# SUPERVISED LEARNING PRACTICAL
# House Price Prediction using Linear Regression

# =========================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =========================================================
# STEP 2: DATA COLLECTION AND PREPROCESSING
# =========================================================

# Sample labeled dataset
data = {
    'Area': [
        500, 600, 700, 800, 900,
        1000, 1100, 1200, 1300, 1400,
        1500, 1600, 1700, 1800, 1900, 2000
    ],

    'Price': [
        25, 30, 35, 40, 45,
        50, 55, 60, 65, 70,
        75, 80, 85, 90, 95, 100
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Define input and output
X = df[['Area']]       # Feature
y = df['Price']        # Target


# =========================================================
# STEP 3: DIVISION OF DATA
# =========================================================

# 80% training data and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# =========================================================
# STEP 4: CHOOSING THE MODEL
# =========================================================

# Since the target is a continuous value (house price),
# Linear Regression is selected.

model = LinearRegression()

print("\nModel selected: Linear Regression")


# =========================================================
# STEP 5: MODEL TRAINING
# =========================================================

# Train the model using training data
model.fit(X_train, y_train)

print("\nModel training completed.")

print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)


# =========================================================
# STEP 6: MODEL ASSESSMENT
# =========================================================

# Predict prices for test data
y_pred = model.predict(X_test)

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(np.round(y_pred, 2))


# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 2))


# =========================================================
# STEP 7: HYPERPARAMETER TUNING
# =========================================================

# Linear Regression has very few hyperparameters.
# For demonstration, we compare different
# Ridge Regression alpha values.

alpha_values = [0.01, 0.1, 1, 10, 100]

best_alpha = None
best_score = -float('inf')

for alpha in alpha_values:

    ridge_model = Ridge(alpha=alpha)

    ridge_model.fit(X_train, y_train)

    score = ridge_model.score(X_test, y_test)

    print(
        "Alpha:", alpha,
        "R2 Score:", round(score, 4)
    )

    # Select the alpha value with the highest R2 score
    if score > best_score:
        best_score = score
        best_alpha = alpha

print("\nBest Alpha:", best_alpha)
print("Best R2 Score:", round(best_score, 4))


# =========================================================
# STEP 8: FINAL MODEL SELECTION
# =========================================================

final_model = Ridge(alpha=best_alpha)

final_model.fit(X_train, y_train)

print("\nFinal model trained successfully.")


# =========================================================
# STEP 9: DEPLOYMENT / NEW PREDICTION
# =========================================================

# Suppose a new house has an area of 1750 sq.ft.

new_house = pd.DataFrame({
    'Area': [1750]
})

predicted_price = final_model.predict(new_house)

print("\nNew House Area:", new_house['Area'].iloc[0], "sq.ft.")
print(
    "Predicted Price:",
    round(predicted_price[0], 2),
    "Lakhs"
)


# =========================================================
# STEP 10: VISUALIZATION
# =========================================================

plt.scatter(
    X,
    y,
    label="Actual Data"
)

plt.plot(
    X,
    model.predict(X),
    label="Regression Line"
)

plt.xlabel("Area (sq.ft.)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")

plt.legend()
plt.show()
