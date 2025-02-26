# RTL-Timing-Analyzer 🚀  
### AI-powered Combinational Logic Depth Prediction for RTL  

## 🔍 Overview  
**RTL-Timing-Analyzer** predicts **combinational logic depth per signal** in an RTL module **without requiring full synthesis**. By extracting **structural features (fan-in, fan-out) from Verilog files**, it leverages **Machine Learning (ML) models** to estimate logic depth and detect **timing violations early**, making RTL design more efficient.  

## 📂 Repository Contents  
📌 **`extract_rtl_features.py`** → Parses RTL files to extract **fan-in, fan-out, and logic dependencies**.  
📌 **`train_and_test.py`** → Trains **RandomForest/XGBoost** models for **logic depth prediction**.  
📌 **`predict_logic_depth.py`** → Predicts **logic depth for new RTL files** and flags **timing violations**.  
📌 **`rtl_files/`** → Sample **RTL Verilog files** for testing.  
📌 **`model_results.csv`** → ML model performance comparison.  
📌 **`predicted_depth_with_violations_rtl.csv`** → Final predictions with **timing violations flagged**.  

## ⚡ Quick Start  

### 1️⃣ Install Dependencies  
```bash
pip install pandas numpy scikit-learn joblib xgboost
