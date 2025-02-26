import pandas as pd
import joblib

# Load best trained model
model = joblib.load("best_model.pkl")

# Load extracted features from RTL
df = pd.read_csv("rtl_features_dataset.csv")

# Select features for prediction (Convert to NumPy array to avoid sklearn warning)
features = ['avg_fan_in', 'avg_fan_out']
X_new = df[features].values  # ✅ FIX: Convert to NumPy array

# Predict logic depth
df['predicted_logic_depth'] = model.predict(X_new)

# Define Timing Constraints
clock_period_ns = 10  # Modify as needed
gate_delay_ns = 0.5   # Modify based on technology node
max_allowed_depth = clock_period_ns / gate_delay_ns  # Compute max depth allowed

# Identify Timing Violations
df['timing_violation'] = df['predicted_logic_depth'] > max_allowed_depth

# Save predictions with timing violations flagged
df.to_csv("predicted_depth_with_violations_rtl.csv", index=False)

# Print summary
print("✅ Predictions saved to predicted_depth_with_violations_rtl.csv")
print(f"⚠️ Timing Violations Found: {df['timing_violation'].sum()}")
