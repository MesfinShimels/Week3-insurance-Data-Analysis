# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import shap
import numpy as np  # For square root calculation



def preprocess_data(data):
    """
    Preprocess the data by handling missing values, encoding, and feature engineering.
    """
    # Fill missing values for numeric and categorical columns
    fill_values = {
        col: data[col].mean() if data[col].dtype in ['float64', 'int64'] else "Unknown"
        for col in data.columns
    }
    data.fillna(fill_values, inplace=True)
    
    # Encoding categorical columns
    categorical_columns = data.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
    
    return data



# Train-Test Split
from sklearn.model_selection import train_test_split

def split_data(data, target_column):
    """
    Split the data into training and testing sets, excluding datetime columns from the independent variables.
    
    Parameters:
    data (pd.DataFrame): The input dataset.
    target_column (str): The name of the target column.

    Returns:
    tuple: Training and testing sets (X_train, X_test, y_train, y_test).
    """
    # # Exclude datetime columns from independent variables
    # datetime_cols = data.select_dtypes(include=['datetime']).columns
    # X = data.drop([target_column] + list(datetime_cols), axis=1)
    # y = data[target_column]
    

# Define features and target
    X = data.select_dtypes(include=['number']).drop(columns=[target_column])
    y = data[target_column]

    return train_test_split(X, y, test_size=0.2, random_state=42)


# Linear Regression Model
def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Decision Tree Model
def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree model.
    """
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

# Random Forest Model
def train_random_forest(X_train, y_train):
    """
    Train a Random Forest model.
    """
    model = RandomForestRegressor(random_state=42, n_estimators=100)
    model.fit(X_train, y_train)
    return model

# XGBoost Model
def train_xgboost(X_train, y_train):
    """
    Train an XGBoost model.
    """
    model = XGBRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model


# Evaluate Model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using R2, MAE, and RMSE metrics.
    """
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)  # Calculate MSE
    rmse = np.sqrt(mse)  # Calculate RMSE manually
    return {"R2": r2, "MAE": mae, "RMSE": rmse}


# Feature Importance Analysis
def feature_importance(model, X_train):
    """
    Analyze feature importance using SHAP.
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_train)
    shap.summary_plot(shap_values, X_train)





import pandas as pd

def handle_missing_data(df):
    """
    Handles missing data in a DataFrame:
    1. For numeric columns, fills missing values with the column mean.
    2. For non-numeric columns, fills missing values with the column mode.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The processed DataFrame.
    """
    # Handle missing values for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            try:
                mean_value = df[col].mean()
                df[col].fillna(mean_value, inplace=True)
            except Exception as e:
                print(f"Error handling numeric column '{col}': {e}")

    # Handle missing values for non-numeric columns
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        if df[col].isnull().sum() > 0:
            try:
                mode_value = df[col].mode()
                if not mode_value.empty:
                    df[col].fillna(mode_value[0], inplace=True)
                else:
                    print(f"Column '{col}' has no mode; skipping.")
            except Exception as e:
                print(f"Error handling non-numeric column '{col}': {e}")

    return df