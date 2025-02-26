import pandas as pd
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("rtl_features_dataset.csv")

# Select features
features = ['avg_fan_in', 'avg_fan_out']  # ✅ Use new extracted features
X = df[features]
y = df['logic_depth']  # ✅ Predicting logic depth

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define models
models = {
    "XGBoost": xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=4),
    "RandomForest": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42),
    "DecisionTree": DecisionTreeRegressor(max_depth=8, random_state=42),
    "LinearRegression": LinearRegression()
}

# Train & evaluate models
results = []
best_model = None
best_mae = float("inf")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Evaluate model
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{name} - MAE: {mae:.4f}, R²: {r2:.4f}")

    # Save results
    results.append({"Model": name, "MAE": mae, "R²": r2})

    # Save best model
    if mae < best_mae:
        best_mae = mae
        best_model = model

# Save best model
if best_model:
    joblib.dump(best_model, "best_model.pkl")
    print("Best model saved as best_model.pkl")

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("model_results.csv", index=False)
print("Model evaluation results saved as model_results.csv")


