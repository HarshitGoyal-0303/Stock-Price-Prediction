# Stock-Price-Prediction
This project predicts Tesla's stock prices using various machine learning models. It preprocesses historical stock data, evaluates multiple regression algorithms, and identifies the best model for predicting future prices. The implementation also classifies stock price movements as "Increase" or "Decrease" and visualizes the results.

DATA SET LINK: https://drive.google.com/file/d/17eMncREfpF5pulCQLnCTLCMbw0HjW-ut/view?usp=sharing
 
Features
•	Handles missing values, duplicates, and outliers.
•	Extracts features from date columns (day, month, year).
•	Scales features and applies PCA for dimensionality reduction.
•	Trains and evaluates:
o	Random Forest Regressor
o	K-Nearest Neighbors (KNN)
o	Support Vector Regressor (SVM)
o	Linear Regression
•	Calculates metrics like MAE, MSE, RMSE, R², Adjusted R², and MAPE.
•	Visualizes residuals and confusion matrix for model evaluation.
•	Predicts stock prices for new data.
 
Getting Started
Prerequisites
Ensure the following Python libraries are installed:
bash
Copy code
pip install pandas numpy matplotlib seaborn scikit-learn
Dataset
Download the TESLA_STOCK_DATA.csv file and upload it to your Google Drive. This file should contain the following columns:
•	Date: Stock date in YYYY-MM-DD format.
•	Open: Opening stock price.
•	High: Highest stock price of the day.
•	Low: Lowest stock price of the day.
•	Close: Closing stock price.
•	Volume: Volume of stocks traded.
•	Adj Close: Adjusted closing price.
 
Usage
1.	Mount Google Drive
The script accesses the dataset from your Google Drive. Ensure your drive is mounted:
python
Copy code
from google.colab import drive
drive.mount('/content/drive')
2.	Run the Code Open the Python script and execute all the cells sequentially. The code:
o	Preprocesses the data.
o	Trains and evaluates models.
o	Selects the best-performing model for prediction.
3.	Predict New Stock Prices Replace the values in the new_data dictionary with your custom input for predictions:
python
Copy code
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
 
Project Structure
bash
Copy code
Tesla_Stock_Prediction/
│
├── TESLA_STOCK_DATA.csv     # Dataset (upload to Google Drive)
├── README.md                # Project Documentation
└── stock_price_prediction.py # Python Script
 
Results
The script will output:
•	Metrics for each model.
•	Visualization of residuals (Actual vs. Predicted).
•	Confusion Matrix for stock price movement classification.
•	Predicted stock price for new input data.

Submitted To:

Dr Sonu Lamba

Submitted By:

Harshit Goyal
![image](https://github.com/user-attachments/assets/4d6ee468-4231-4f0e-94ae-fbbdb6c40121)
