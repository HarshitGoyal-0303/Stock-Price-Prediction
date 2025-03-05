# Stock Price Prediction

This project predicts **Tesla's stock prices** using various machine learning models. It preprocesses historical stock data, evaluates multiple regression algorithms, and identifies the best model for predicting future prices. The implementation also classifies stock price movements as **"Increase"** or **"Decrease"** and visualizes the results.

## Dataset
Download the dataset from the following link:
[Dataset Link](https://drive.google.com/file/d/17eMncREfpF5pulCQLnCTLCMbw0HjW-ut/view?usp=sharing)

### Dataset Columns:
- **Date**: Stock date in YYYY-MM-DD format
- **Open**: Opening stock price
- **High**: Highest stock price of the day
- **Low**: Lowest stock price of the day
- **Close**: Closing stock price
- **Volume**: Volume of stocks traded
- **Adj Close**: Adjusted closing price

## Features
- Handles missing values, duplicates, and outliers.
- Extracts features from date columns (**day**, **month**, **year**).
- Scales features and applies **Principal Component Analysis (PCA)** for dimensionality reduction.
- Trains and evaluates multiple machine learning models:
  - Random Forest Regressor
  - K-Nearest Neighbors (KNN)
  - Support Vector Regressor (SVM)
  - Linear Regression
- Calculates performance metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score
  - Adjusted R² Score
  - Mean Absolute Percentage Error (MAPE)
- Visualizes:
  - Residuals Plot (Actual vs. Predicted)
  - Confusion Matrix for Stock Price Movement Classification
- Predicts stock prices for new data

## Prerequisites
Ensure the following Python libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Project Structure
```bash
Tesla_Stock_Prediction/
│
├── TESLA_STOCK_DATA.csv     # Dataset (Upload to Google Drive)
├── README.md                # Project Documentation
└── stock_price_prediction.py # Python Script
```

## Getting Started
### 1. Mount Google Drive
The dataset is accessed from Google Drive. Make sure your drive is mounted.

```python
from google.colab import drive
drive.mount('/content/drive')
```

### 2. Run the Code
Execute the Python script in Google Colab or any Python environment. The code will:
- Preprocess the data
- Train and evaluate models
- Select the best-performing model for prediction

### 3. Predict New Stock Prices
To predict new stock prices, replace the values in the `new_data` dictionary with custom input:

```python
new_data = pd.DataFrame({
    'Open': [299.14],
    'High': [328.70],
    'Low': [297.66],
    'Volume': [203590100],
    'Adj Close': [321.22],
    'day': [8],
    'month': [11],
    'year': [2024]
})
```

## Results
The output includes:
- Model performance metrics
- Residual plots
- Confusion matrix for stock price classification
- Predicted stock price for custom inputs

## Author
**Harshit Goyal**

## Acknowledgements
Submitted to **Dr. Sonu Lamba** as part of the academic project.

