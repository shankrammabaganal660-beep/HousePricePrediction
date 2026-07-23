# AI/ML Task 3: Model Validation, Overfitting Control & Hyperparameter Tuning

This repository contains the complete implementation for **Task 3** of the Artificial Intelligence & Machine Learning Internship. The goal of this task is to train a Decision Tree Regressor on the California Housing Dataset, detect overfitting, perform Cross-Validation, tune hyperparameters using GridSearchCV, and evaluate the final optimized model.

## 📂 Project Structure

```text
HousePricePrediction/
├── notebook/
│   └── AI_ML_Task3_Model_Validation.ipynb  # Core ML pipeline (Training, Tuning, Evaluation)
├── plots/
│   ├── Task3_Overfitting_Detection.png     # Train vs Test RMSE comparison
│   ├── Task3_CV_Scores.png                 # 5-Fold Cross-Validation Scores
│   └── Task3_Model_Comparison.png          # Final model comparison (RMSE)
├── report/
│   └── AI_ML_Task3_Model_Validation_Report.pdf # Final professionally formatted 3-page report
├── generate_notebook_task3.py              # Script to automatically generate the Task 3 notebook
├── generate_task3_report.py                # Script to automatically generate the PDF report and plots
├── run_task3.bat                           # Batch script to execute the pipeline
└── README_Task3.md                         # This documentation file
```

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed. The required libraries are listed in `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 2. Quick Start
To generate all artifacts automatically, simply double-click or run the batch script:
```bash
run_task3.bat
```
This will:
1. Generate the Jupyter Notebook (`notebook/AI_ML_Task3_Model_Validation.ipynb`).
2. Run the Machine Learning pipeline to generate plots (`plots/`).
3. Compile the professional PDF report (`report/AI_ML_Task3_Model_Validation_Report.pdf`).

### 3. Manual Execution
If you prefer running the scripts manually:
```bash
python generate_notebook_task3.py
python generate_task3_report.py
```

## 📊 Methodology & Results
- **Overfitting Detection**: Analyzed the gap between Train RMSE and Test RMSE on a default Decision Tree.
- **Cross-Validation**: Implemented 5-Fold CV to validate model stability and robustness.
- **Hyperparameter Tuning**: Utilized `GridSearchCV` to optimize `max_depth` and `min_samples_split`, preventing the tree from overfitting.
- **Model Comparison**: The tuned Decision Tree was compared with Linear Regression and Ridge Regression models from Task 2.
- **Conclusion**: The tuned model effectively balanced the bias-variance tradeoff, generalizing much better on unseen data than the default model.
