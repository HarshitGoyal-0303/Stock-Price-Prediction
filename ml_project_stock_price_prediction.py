# -*- coding: utf-8 -*-
"""ML Project Stock Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zJgarN4T6xLro1Vda8XQ61FF-cj2fXeb
"""

!pip install seaborn
import seaborn as sns

"""# **Mounting Script and Google Drive**"""

from google.colab import drive
drive.mount('/content/drive')

"""# **Import necessary libraries**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error, explained_variance_score, confusion_matrix, ConfusionMatrixDisplay

"""# **Function to handle missing values**"""

def handle_missing_values(df, target_col, feature_cols):
    df = df.dropna(subset=[target_col])  # Drop rows where target is missing
    for col in feature_cols:
        df[col] = df[col].fillna(df[col].median())  # Fill missing values with median
    return df

"""# **Function to remove duplicates**"""

def remove_duplicates(df):
    return df.drop_duplicates()

"""# **Function to handle outliers using the IQR method**"""

def handle_outliers(df, feature_cols):
    for col in feature_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] < lower_bound, lower_bound, df[col])
        df[col] = np.where(df[col] > upper_bound, upper_bound, df[col])
    return df

"""# **Function to extract date features**"""

def extract_date_features(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], format='%Y-%m-%d')
    df['day'] = df[date_col].dt.day
    df['month'] = df[date_col].dt.month
    df['year'] = df[date_col].dt.year
    return df.drop(columns=[date_col])

"""# **Function to scale features**"""

def scale_features(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X) #ttry to change mean to 0 and sd to 1
    return X_scaled, scaler

"""# **Function to perform PCA**"""

def apply_pca(X, n_components):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    return X_pca, pca

#Dimensionality Reduction

"""# **Function to calculate and evaluate metrics**"""

def calculate_metrics(y_test, y_pred):
    # Mean Absolute Error
    mae = mean_absolute_error(y_test, y_pred)

    # Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)

    # Root Mean Squared Error
    rmse = np.sqrt(mse)

    # Mean Absolute Percentage Error
    mape = mean_absolute_percentage_error(y_test, y_pred) * 100  # Convert to percentage

    # R-squared
    r2 = r2_score(y_test, y_pred)

    # Adjusted R-squared
    n = len(y_test)  # Number of observations
    p = X_train.shape[1]  # Number of predictors
    if n - p - 1 != 0:
        adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))
    else:
        adj_r2 = r2  # If the formula is invalid, set adj_r2 to r2

    # Explained Variance Score
    evs = explained_variance_score(y_test, y_pred)

    # Accuracy within ±5%
    accuracy = np.mean(np.abs((y_pred - y_test) / y_test) < 0.05)

    return mae, mse, rmse, mape, r2, adj_r2, evs, accuracy

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae, mse, rmse, mape, r2, adj_r2, evs, accuracy = calculate_metrics(y_test, y_pred)
    return mae, mse, rmse, mape, r2, adj_r2, evs, accuracy, y_pred

"""# **Function to plot actual vs predicted prices**"""

def plot_actual_vs_predicted(y_test, y_pred, model_name):
    # Calculate errrors
    residuals = y_test - y_pred

    # Set up the plot
    plt.figure(figsize=(10, 6))

    # Create a box plot for residuals
    sns.boxplot(data=residuals, color="orange", width=0.5)


    plt.title(f'{model_name} - Residuals Box Plot (Actual vs Predicted)', fontsize=16, fontweight='bold')
    plt.xlabel('Residuals', fontsize=14)
    plt.ylabel('Values', fontsize=14)

    plt.tight_layout() #Gives Spacing
    plt.show()

"""# **Function to create a confusion matrix**"""

def create_confusion_matrix(y_test, y_pred, model_name):
    y_test_diff = y_test.diff().fillna(0)
    y_pred_diff = pd.Series(y_pred).diff().fillna(0)

    y_test_class = np.where(y_test_diff > 0, "Increase", "Decrease")  # Positive difference = "Increase", otherwise "Decrease"
    y_pred_class = np.where(y_pred_diff > 0, "Increase", "Decrease")

    y_test_class = y_test_class[:len(y_pred_class)]  # Truncate y_test_class to match the length of y_pred_class

    cm = confusion_matrix(y_test_class, y_pred_class, labels=["Increase", "Decrease"])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Increase", "Decrease"])
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f'Confusion Matrix for {model_name}')
    plt.show()

"""# **Implementing Linear Regression**"""

class ManualLinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add a column of ones to X
        self.weights_ = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
        self.intercept_ = self.weights_[0]  # Intercept is the first weight
        self.coef_ = self.weights_[1:]  # Coefficients are the remaining weights

    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        return X_b @ self.weights_

"""# **Implementing KNN Function**"""

class ManualKNN:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X):
        y_pred = []
        for x in X:
            # Calculaing distances from the point to all training points
            distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]

            # Sorting by distance and get the indices of the k nearest neighbors
            neighbors_idx = np.argsort(distances)[:self.n_neighbors]

            # Getting the target values of the k nearest neighbors
            k_nearest_labels = self.y_train[neighbors_idx]

            # Predicting the mean for regression
            y_pred.append(np.mean(k_nearest_labels))
        return np.array(y_pred)

"""# **Main Script**"""

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/TESLA_STOCK_DATA.csv')

# Preprocessing
target_col = 'Close'
feature_cols = ['Open', 'High', 'Low', 'Volume', 'Adj Close']

data = handle_missing_values(data, target_col, feature_cols)
data = remove_duplicates(data)
data = handle_outliers(data, feature_cols)
data = extract_date_features(data, 'Date')

# Prepare features and target
X = data[['Open', 'High', 'Low', 'Volume', 'Adj Close', 'day', 'month', 'year']]
y = data['Close']

X_scaled, scaler = scale_features(X)
X_pca, pca = apply_pca(X_scaled, n_components=5)

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "KNN Algorithm": ManualKNN(n_neighbors=5),
    "SVM": SVR(kernel='rbf', C=100, gamma='scale'),
    "Linear Regression": ManualLinearRegression()
}


# Evaluate models
best_model_name, best_model, best_accuracy, best_mse = "", None, -np.inf, np.inf

for model_name, model in models.items():
    mae, mse, rmse, mape, r2, adj_r2, evs, accuracy, y_pred = evaluate_model(
        model, X_train, X_test, y_train, y_test
    )
    print(f"{model_name} Metrics:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
    print(f"R² Score: {r2:.2f}")
    print(f"Adjusted R² Score: {adj_r2:.2f}")
    print(f"Accuracy within ±5%: {accuracy * 100:.2f}%\n")

    # Track the best model based on accuracy and MSE
    if (accuracy > best_accuracy) or (accuracy == best_accuracy and mse < best_mse):
        best_accuracy = accuracy
        best_model_name = model_name
        best_model = model
        best_mse = mse

    # Plot Actual vs Predicted
    plot_actual_vs_predicted(y_test, y_pred, model_name)

#Final Prediction
print(f"\nTraining the best model: {best_model_name}...")
best_model.fit(X_pca, y)

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

new_data_scaled = scaler.transform(new_data)
new_data_pca = pca.transform(new_data_scaled)

def classify_price_movement(y_true, y_pred):
    y_true_class = np.where(np.diff(y_true) > 0, "Increase", "Decrease")  # Compare consecutive true prices
    y_pred_class = np.where(np.diff(y_pred) > 0, "Increase", "Decrease")  # Compare consecutive predicted prices
    return y_true_class, y_pred_class

# Classify the actual and predicted stock price movements
y_test_class, y_pred_class = classify_price_movement(y_test.values, y_pred)

# Create confusion matrix
cm = confusion_matrix(y_test_class, y_pred_class, labels=["Increase", "Decrease"])

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Increase", "Decrease"])
disp.plot(cmap=plt.cm.Blues)
plt.title(f'Confusion Matrix for {best_model_name}')
plt.show()
predicted_price = best_model.predict(new_data_pca)
print(f"Predicted Stock Price for new data: {predicted_price[0]:.2f}")