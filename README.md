# RTL-Timing-Analyzer   
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
```

### 2️⃣ Extract RTL Features  
```bash
python extract_rtl_features.py
```

### 3️⃣ Train ML Model  
```bash
python train_and_test.py
```

### 4️⃣ Predict Logic Depth & Timing Violations  
```bash
python predict_logic_depth.py
```

## 🏆 Key Features  
✅ **No full synthesis required** – significantly reduces analysis time.  
✅ **Predicts combinational logic depth per signal** using ML.  
✅ **Flags timing violations** based on **clock constraints**.  
✅ **Works on unseen RTL files** with high accuracy.  

## 📌 Example Output  
| RTL File  | Signal  | Logic Depth | Fan-in | Fan-out | Timing Violation |
|-----------|--------|------------|--------|--------|------------------|
| `cpu_core.v` | `alu_op` | 18 | 3 | 2 | ❌ |
| `alu.v` | `sum_out` | 15 | 2 | 2 | ✅ |

## 📊 Model Performance  
| **Model**        | **MAE (Lower is Better)** | **R² Score (Higher is Better)** |
|-----------------|--------------------------|-------------|
| **RandomForest** | **0.0149**                | **0.9346**  |
| **XGBoost**     | **0.0154**                | **0.9339**  |
| **DecisionTree** | 0.0152                    | 0.9105      |
| **LinearRegression** | 0.0670               | 0.6847      |

🎯 **RandomForest performed best**, achieving the lowest **MAE** and highest **R² score**, making it the chosen model.  

## 🛠️ Future Improvements  
- Support for **multi-clock domains**.  
- Enhanced **RTL feature extraction** (e.g., gate delay modeling).  
- Expansion of ML models for **higher accuracy and robustness**.  

## 👨‍💻 Contributing  
Contributions are welcome! Feel free to open an **issue** or submit a **pull request**.  


🚀 **Developed by [@annikaasinha](https://github.com/annikaasinha/)**  
```

