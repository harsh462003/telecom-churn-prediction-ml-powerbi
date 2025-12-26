# Telecom Customer Churn Prediction and Retention Insights using Machine Learning and Power BI

## 📌 Overview
Customer churn is a critical challenge for telecom companies, as acquiring new customers is significantly more expensive than retaining existing ones.  
This project builds an **end-to-end machine learning pipeline** to predict customer churn using tabular telecom data and provides **actionable retention insights** through an interactive **Power BI dashboard**.

The solution combines classical machine learning models with business intelligence to support **data-driven customer retention decisions**.

---

## 🎯 Problem Statement
Predict whether a telecom customer is likely to churn based on service usage, billing, and contract information, and visualize churn drivers and customer risk segments to assist business stakeholders in designing targeted retention strategies.

---

## 🧩 Dataset
- Public telecom customer churn dataset
- Tabular data containing customer demographics, service subscriptions, billing details, and churn labels
- Target variable: **Churn (Yes / No)**

> Note: The full dataset is not committed to this repository.  
A small sample dataset is included for structure verification.

---

## 🧹 Data Preprocessing
Key preprocessing steps include:

- Handling missing values in numerical features
- Converting data types (e.g., TotalCharges)
- Encoding categorical variables using One-Hot Encoding
- Feature scaling using StandardScaler
- Feature engineering:
  - Average monthly spend
  - Tenure-based customer buckets
- Train-test split with class stratification
- Handling class imbalance using class weights

---

## 🤖 Machine Learning Models
The following models were trained and evaluated:

- Logistic Regression (baseline, interpretable)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

Hyperparameter tuning was performed using **GridSearchCV** and **RandomizedSearchCV** to improve model performance.

---

## 📊 Model Evaluation
Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix
- ROC and Precision-Recall curves

**Business focus:**  
Recall is prioritized to minimize missed churners, as losing a customer is costlier than contacting a loyal one.

---

## 📈 Power BI Integration
Model predictions are exported and visualized in a **5-page Power BI dashboard**:

### Dashboard Pages
1. **Churn Overview**  
   - Total customers  
   - Churn rate  
   - High-risk customers  

2. **Churn Drivers**  
   - Churn by contract type  
   - Churn by payment method  
   - Churn by internet service  

3. **Risk Segmentation**  
   - Low / Medium / High risk customers  
   - Revenue distribution by risk group  

4. **Tenure & Revenue Impact**  
   - Churn probability vs tenure  
   - Estimated revenue at risk  

5. **Customer Drill-Down**  
   - Customer-level churn probability  
   - Interactive filters for business analysis  

---

## 📤 Project Structure
telecom-churn-prediction-ml-powerbi/
├─ notebooks/
│ ├─ 01_eda.ipynb
│ ├─ 02_preprocessing.ipynb
│ ├─ 03_modeling_evaluation.ipynb
│ ├─ 04_hyperparameter_tuning.ipynb
│ └─ 05_powerbi_export.ipynb
├─ data/
├─ outputs/
├─ powerbi/
├─ reports/
├─ src/
├─ README.md
├─ requirements.txt
├─ .gitignore
└─ LICENSE

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Power BI

---

## 🧠 Key Business Insights
- Month-to-month contracts show the highest churn rates
- Customers with low tenure are at higher risk of churn
- Lack of value-added services increases churn probability
- High monthly charges combined with short tenure indicate high churn risk

---

## 🚀 How to Run
1. Place the dataset in the `data/` folder  
2. Run notebooks in order from `01_eda.ipynb` to `05_powerbi_export.ipynb`  
3. Use the exported CSV from `outputs/` to build the Power BI dashboard  

---

## 🎤 Interview Talking Point
> “This project demonstrates how machine learning and business intelligence can be combined to not only predict customer churn but also deliver actionable insights for retention strategy.”

---

## 📌 Author
Harshith Nagaraj
