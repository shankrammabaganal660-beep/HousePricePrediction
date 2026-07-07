# House Price Prediction using Linear Regression

## Introduction
Welcome to the **House Price Prediction** project! This project demonstrates a complete Machine Learning workflow using the California Housing Dataset. It is part of an internship assignment focusing on practical implementation of Machine Learning algorithms, specifically Linear Regression, to predict house prices based on various features.

## Problem Statement
The objective of this project is to build a predictive model that can accurately estimate the median house value in California districts. By analyzing various features such as median income, housing median age, and number of rooms, the goal is to uncover patterns and relationships that contribute to housing prices.

## Dataset
- **Source**: California Housing Dataset from `sklearn.datasets.fetch_california_housing()`.
- **Description**: This dataset contains housing data for California districts derived from the 1990 U.S. census.
- **Features**:
  - `MedInc`: Median income in block group
  - `HouseAge`: Median house age in block group
  - `AveRooms`: Average number of rooms per household
  - `AveBedrms`: Average number of bedrooms per household
  - `Population`: Block group population
  - `AveOccup`: Average number of household members
  - `Latitude`: Block group latitude
  - `Longitude`: Block group longitude
- **Target**: `MedHouseVal` (Median house value in units of 100,000)

## Workflow
1. **Data Loading & Overview**: Import libraries, load the dataset, and display basic information.
2. **Exploratory Data Analysis (EDA)**: Statistical summary, missing values, duplicate values, histograms, boxplots, correlation heatmap, and pairplots.
3. **Data Preprocessing**: Handling any data anomalies and selecting relevant features.
4. **Model Training**: Splitting the data into training (80%) and testing (20%) sets, and training a Linear Regression model.
5. **Model Evaluation**: Evaluating the model using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.
6. **Visualization**: Plotting Actual vs. Predicted values and Residual plots to visualize model performance.

## Technologies Used
- **Python 3**
- **Jupyter Notebook**
- **Pandas** & **NumPy** for Data Manipulation
- **Matplotlib** & **Seaborn** for Data Visualization
- **Scikit-learn** for Machine Learning

## Project Structure
```
HousePricePrediction/
│── notebook/
│   └── task1_ml_linear_regression.ipynb
│── report/
│   └── Project_Report.pdf
│── presentation/
│   └── Task1_Presentation.pptx
│── model/
│   └── house_price_model.pkl
│── requirements.txt
│── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
cd HousePricePrediction
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Jupyter Notebook:
```bash
jupyter notebook notebook/task1_ml_linear_regression.ipynb
```

## Results
The trained Linear Regression model provides insightful coefficients indicating the impact of each feature on the house price. Evaluation metrics such as R² Score and RMSE indicate the model's accuracy and the variance explained by the features.

## Conclusion
This project successfully implemented a complete Machine Learning workflow for predicting house prices using Linear Regression. The model achieved reasonable accuracy, and the EDA revealed significant correlations between features like Median Income and House Value.

## Future Scope
- **Advanced Models**: Implement Decision Trees, Random Forests, or Gradient Boosting models to capture non-linear relationships.
- **Feature Engineering**: Create new features combining existing ones for better predictive power.
- **Hyperparameter Tuning**: Optimize model parameters using Grid Search or Random Search techniques.
- **Deployment**: Deploy the trained model using Flask or FastAPI for a web-based prediction interface.
