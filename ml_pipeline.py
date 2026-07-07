import os
import json
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import nbformat as nbf

# Set seaborn style for plots
sns.set_theme(style="whitegrid")

# Create directories
os.makedirs("model", exist_ok=True)
os.makedirs("plots", exist_ok=True)
os.makedirs("notebook", exist_ok=True)

print("Loading dataset...")
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target

print("Performing EDA and saving plots...")

# 1. Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('plots/correlation_heatmap.png')
plt.close()

# 2. Histograms
df.hist(bins=50, figsize=(15, 10))
plt.suptitle('Histograms for Numerical Features', fontsize=16)
plt.tight_layout()
plt.savefig('plots/histograms.png')
plt.close()

# 3. Boxplots
plt.figure(figsize=(15, 10))
sns.boxplot(data=df, orient="h")
plt.title('Boxplots for Outlier Detection')
plt.tight_layout()
plt.savefig('plots/boxplots.png')
plt.close()

# 4. Pairplot (Important features only due to size: MedInc, AveRooms, HouseAge, MedHouseVal)
important_features = ['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal']
sns.pairplot(df[important_features])
plt.suptitle('Pairplot of Important Features', y=1.02)
plt.tight_layout()
plt.savefig('plots/pairplot.png')
plt.close()

print("Training Model...")
# Train-Test Split
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("Evaluating Model...")
# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

metrics = {
    'MAE': mae,
    'MSE': mse,
    'RMSE': rmse,
    'R2 Score': r2
}

# Save metrics for doc generation
with open('plots/metrics.json', 'w') as f:
    json.dump(metrics, f)

# 5. Actual vs Predicted
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.tight_layout()
plt.savefig('plots/actual_vs_predicted.png')
plt.close()

# 6. Residual Plot
plt.figure(figsize=(8, 6))
residuals = y_test - y_pred
sns.histplot(residuals, kde=True, bins=30)
plt.xlabel('Residuals (Error)')
plt.ylabel('Frequency')
plt.title('Residual Distribution')
plt.tight_layout()
plt.savefig('plots/residual_plot.png')
plt.close()

# Save model
print("Saving model...")
with open('model/house_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Generating Jupyter Notebook...")
nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell("# House Price Prediction using Linear Regression\n\nThis notebook demonstrates a complete Machine Learning workflow using the California Housing Dataset to predict house prices using Linear Regression."),
    
    nbf.v4.new_markdown_cell("## 1. Import Libraries\n\nImporting all necessary libraries for data manipulation, visualization, and machine learning."),
    nbf.v4.new_code_cell("import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom sklearn.datasets import fetch_california_housing\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\nimport pickle\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Set visualization style\nsns.set_theme(style='whitegrid')"),
    
    nbf.v4.new_markdown_cell("## 2. Load Dataset\n\nLoading the California Housing dataset from `sklearn.datasets`."),
    nbf.v4.new_code_cell("california = fetch_california_housing()\ndf = pd.DataFrame(california.data, columns=california.feature_names)\ndf['MedHouseVal'] = california.target\n\n# Display first five rows\ndf.head()"),
    
    nbf.v4.new_markdown_cell("## 3. Exploratory Data Analysis (EDA)\n\n### 3.1 Dataset Overview"),
    nbf.v4.new_code_cell("print('Dataset Shape:', df.shape)"),
    
    nbf.v4.new_markdown_cell("### 3.2 Dataset Information"),
    nbf.v4.new_code_cell("df.info()"),
    
    nbf.v4.new_markdown_cell("### 3.3 Statistical Summary"),
    nbf.v4.new_code_cell("df.describe()"),
    
    nbf.v4.new_markdown_cell("### 3.4 Missing Values\n\nChecking for any null values in the dataset."),
    nbf.v4.new_code_cell("df.isnull().sum()"),
    
    nbf.v4.new_markdown_cell("### 3.5 Duplicate Values\n\nChecking for duplicate rows in the dataset."),
    nbf.v4.new_code_cell("print('Duplicate Rows:', df.duplicated().sum())"),
    
    nbf.v4.new_markdown_cell("### 3.6 Correlation Heatmap\n\nVisualizing the correlation matrix to understand the linear relationships between features and the target variable."),
    nbf.v4.new_code_cell("plt.figure(figsize=(10, 8))\ncorrelation_matrix = df.corr()\nsns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)\nplt.title('Correlation Heatmap')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("### 3.7 Histograms\n\nPlotting histograms to analyze the distribution of each numerical feature."),
    nbf.v4.new_code_cell("df.hist(bins=50, figsize=(15, 10))\nplt.suptitle('Histograms for Numerical Features', fontsize=16)\nplt.show()"),
    
    nbf.v4.new_markdown_cell("### 3.8 Boxplots\n\nIdentifying potential outliers in the dataset using boxplots."),
    nbf.v4.new_code_cell("plt.figure(figsize=(15, 10))\nsns.boxplot(data=df, orient='h')\nplt.title('Boxplots for Outlier Detection')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("### 3.9 Pairplot\n\nVisualizing pairwise relationships for important features."),
    nbf.v4.new_code_cell("important_features = ['MedInc', 'AveRooms', 'HouseAge', 'MedHouseVal']\nsns.pairplot(df[important_features])\nplt.suptitle('Pairplot of Important Features', y=1.02)\nplt.show()"),
    
    nbf.v4.new_markdown_cell("## 4. Data Preprocessing & Train-Test Split\n\nSplitting the data into features (X) and target (y), and then into training and testing sets (80:20)."),
    nbf.v4.new_code_cell("X = df.drop('MedHouseVal', axis=1)\ny = df['MedHouseVal']\n\n# Train-Test Split (80:20)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nprint('Training set shape:', X_train.shape)\nprint('Testing set shape:', X_test.shape)"),
    
    nbf.v4.new_markdown_cell("## 5. Model Training\n\nTraining a Multiple Linear Regression model on the training data."),
    nbf.v4.new_code_cell("model = LinearRegression()\nmodel.fit(X_train, y_train)\nprint('Model training complete.')"),
    
    nbf.v4.new_markdown_cell("## 6. Model Evaluation\n\nPredicting on test data and evaluating performance using standard regression metrics."),
    nbf.v4.new_code_cell("y_pred = model.predict(X_test)\n\nmae = mean_absolute_error(y_test, y_pred)\nmse = mean_squared_error(y_test, y_pred)\nrmse = np.sqrt(mse)\nr2 = r2_score(y_test, y_pred)\n\nprint(f'Mean Absolute Error (MAE): {mae:.4f}')\nprint(f'Mean Squared Error (MSE): {mse:.4f}')\nprint(f'Root Mean Squared Error (RMSE): {rmse:.4f}')\nprint(f'R² Score: {r2:.4f}')"),
    
    nbf.v4.new_markdown_cell("### 6.1 Feature Coefficients\n\nDisplaying the coefficients for each feature to understand their impact on house prices."),
    nbf.v4.new_code_cell("coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})\ncoefficients = coefficients.sort_values(by='Coefficient', ascending=False)\ncoefficients"),
    
    nbf.v4.new_markdown_cell("### 6.2 Actual vs Predicted Plot\n\nVisualizing how well the predicted prices match the actual prices."),
    nbf.v4.new_code_cell("plt.figure(figsize=(8, 6))\nplt.scatter(y_test, y_pred, alpha=0.5)\nplt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)\nplt.xlabel('Actual Prices')\nplt.ylabel('Predicted Prices')\nplt.title('Actual vs Predicted Prices')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("### 6.3 Residual Plot\n\nPlotting the distribution of residuals (errors) to check if they are normally distributed."),
    nbf.v4.new_code_cell("plt.figure(figsize=(8, 6))\nresiduals = y_test - y_pred\nsns.histplot(residuals, kde=True, bins=30)\nplt.xlabel('Residuals (Error)')\nplt.ylabel('Frequency')\nplt.title('Residual Distribution')\nplt.show()"),
    
    nbf.v4.new_markdown_cell("## 7. Save Model\n\nSaving the trained model using Pickle for future deployment."),
    nbf.v4.new_code_cell("import os\nos.makedirs('../model', exist_ok=True)\nwith open('../model/house_price_model.pkl', 'wb') as file:\n    pickle.dump(model, file)\nprint('Model saved successfully to ../model/house_price_model.pkl')")
]

with open('notebook/task1_ml_linear_regression.ipynb', 'w') as f:
    nbf.write(nb, f)
print("Jupyter Notebook created successfully!")
