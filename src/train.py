import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

def preprocess_data(data):
    # Convert TransactionMonth and VehicleIntroDate to numeric (UNIX timestamp)
    if 'TransactionMonth' in data.columns:
        data['TransactionMonth'] = pd.to_datetime(data['TransactionMonth'], errors='coerce').astype('int64') / 10**9
    
    if 'VehicleIntroDate' in data.columns:
        data['VehicleIntroDate'] = pd.to_datetime(data['VehicleIntroDate'], errors='coerce').astype('int64') / 10**9

    # Handle categorical columns using one-hot encoding
    categorical_columns = data.select_dtypes(include=['object', 'bool']).columns
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    # Fill missing values
    data = data.fillna(0)

    return data

def train_model(input_path, output_path):
    # Load the data
    data = pd.read_csv(input_path)

    # Split features and target
    X = data.drop(columns=['TotalPremium'])  # Replace with your target variable
    y = data['TotalPremium']

    # Preprocess the features
    X = preprocess_data(X)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    # Save the model
    joblib.dump(model, output_path)
    print(f"Model saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train the model.")
    parser.add_argument("--input", type=str, required=True, help="Path to preprocessed dataset")
    parser.add_argument("--output", type=str, required=True, help="Path to save the trained model")

    args = parser.parse_args()

    train_model(args.input, args.output)
import pandas as pd

def missing_value(df):
    # Calculate the number of missing values for each column
    missing_values = df.isnull().sum()
    total_entries = len(df)  # Total number of rows in the DataFrame
    missing_percentage = (missing_values / total_entries) * 100  # Calculate the percentage of missing values

    # Combine missing value count and percentage into a DataFrame for better readability
    missing_data = pd.DataFrame({
        'Missing Values': missing_values,
        'Missing Percentage': missing_percentage,
    })

    # Sort by the number of missing values (optional)
    missing_data_sorted = missing_data.sort_values(by='Missing Values', ascending=False)
    
    # Identify columns with missing percentage greater than 60%
    columns_to_drop = missing_data[missing_data['Missing Percentage'] > 60].index.tolist()
    
    # Drop those columns from the DataFrame
    cleaned_df = df.drop(columns=columns_to_drop)
    
    return cleaned_df, columns_to_drop
