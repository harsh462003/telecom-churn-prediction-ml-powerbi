# Telecom Customer Churn Prediction (Machine Learning + Power BI)

Predict whether a telecom customer will churn using tabular service/billing data, then visualize churn drivers and risk segments using a Power BI dashboard to support retention decisions.

## Project Highlights
- End-to-end ML pipeline: cleaning → preprocessing → model training → evaluation → hyperparameter tuning
- Compared models: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost
- Evaluation with Precision/Recall/F1 + ROC-AUC and diagnostic plots (Confusion Matrix, ROC, PR)
- Exported churn probabilities + risk segments for a 5-page Power BI dashboard

## Dataset
This repo does not commit the full dataset by default.

Place the dataset at:
`data/WA_Fn-UseC_-Telco-Customer-Churn.csv`

A small sample is included at:
`data/sample_telco.csv`

## Notebooks (run in order)
1. `notebooks/01_eda.ipynb`
2. `notebooks/02_preprocessing.ipynb`
3. `notebooks/03_modeling_evaluation.ipynb`
4. `notebooks/04_hyperparameter_tuning.ipynb`
5. `notebooks/05_powerbi_export.ipynb`

## Outputs
- `outputs/model_metrics.csv`
- `outputs/tuned_model_metrics.csv`
- `outputs/predictions_for_powerbi.csv`

## Power BI (5 Pages)
1) Churn Overview  
2) Churn Drivers  
3) Risk Segmentation  
4) Tenure & Revenue Impact  
5) Customer Drill-Down  

Store:
- `powerbi/Telco_Churn_Dashboard.pbix`
- `powerbi/dashboard_screenshots/*.png`

## Local Setup
```bash
pip install -r requirements.txt
```

## Interview line
“Recall matters because missing a churner often costs more than contacting a loyal customer.”
