# AI/ML Task 2: Feature Engineering, Model Optimization & Performance Comparison

This repository contains the complete implementation for **Task 2** of the MainCrafts Technology Artificial Intelligence & Machine Learning Internship. The goal of this task is to perform feature engineering, train multiple regression models, optimize performance, and evaluate them on the California Housing Dataset.

## 📂 Project Structure

```text
HousePricePrediction/
├── notebook/
│   └── AI_ML_Task2_Model_Comparison.ipynb  # Core ML pipeline (EDA, Training, Evaluation)
├── plots/
│   ├── correlation_heatmap.png             # Generated EDA visualization
│   └── Task2_Actual_vs_Predicted.png       # Best model performance visualization
├── report/
│   ├── AI_ML_Task2_Model_Comparison_Report.pdf # Final professionally formatted report
│   └── AI_ML_Task2_Comparison_Table.csv    # Exported evaluation metrics table
├── generate_task2_report.py                # Python script to programmatically generate the PDF report
└── README_Task2.md                         # This documentation file
```

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed. The following libraries are required to run the Jupyter Notebook and the PDF report generator:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter nbformat reportlab
```

### 2. Running the Jupyter Notebook
The primary machine learning pipeline is documented comprehensively in a Jupyter Notebook. It runs sequentially and requires no manual edits.
1. Open your terminal and navigate to the project directory.
2. Launch Jupyter Notebook or open the file in VS Code:
   ```bash
   jupyter notebook notebook/AI_ML_Task2_Model_Comparison.ipynb
   ```
3. Select **"Run All"** to execute the pipeline. The notebook will automatically:
   - Load and split the California Housing Dataset.
   - Standardize the features.
   - Train Linear Regression, Ridge Regression, and Decision Tree algorithms.
   - Calculate RMSE and R² metrics.
   - Save the comparison table to the `report/` folder and graphs to `plots/`.

### 3. Generating the Professional PDF Report
A custom Python script using the `reportlab` library was created to dynamically run the models, extract the *exact* performance metrics, and build a university-grade internship report.
1. In your terminal, ensure you are in the root directory (`HousePricePrediction/`).
2. Run the script:
   ```bash
   python generate_task2_report.py
   ```
3. The newly generated PDF will be saved as `report/AI_ML_Task2_Model_Comparison_Report.pdf`.

## 📊 Methodology & Results

- **Data Preprocessing:** Handled missing values, explored dataset correlations using Seaborn heatmaps, and scaled features using `StandardScaler` to ensure optimal model convergence.
- **Models Evaluated:** Linear Regression (baseline), Ridge Regression (L2 Regularization), and Decision Tree Regressor (Non-linear).
- **Best Model Identification:** 
  - The script programmatically evaluates all models based on **Root Mean Squared Error (RMSE)** and **R-squared (R²)** scores. 
  - Ridge Regression and Decision Trees often perform best; the exact winning metrics and a justification for selection are automatically injected into the final PDF.
- **Visualizations:** Actual vs. Predicted scatter plots are generated to visually diagnose the model's accuracy.

## 🏆 Internship Standards
This task enforces professional engineering standards:
- **PEP 8** compliance across all Python code.
- Fully automated reporting pipeline to avoid "magic numbers" or hardcoded estimates.
- High-quality, formatted `.pdf` documentation ready for strict evaluation.
