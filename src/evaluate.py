import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib
import os

def evaluate_model(input_path, model_path):
    # Load the data
    data = pd.read_csv(input_path)

    # Split the data
    X = data.drop(columns=['TotalPremium'])  # Replace with your target variable
    y = data['TotalPremium']

    # Load the model
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate the model.")
    parser.add_argument("--input", type=str, required=True, help="Path to preprocessed dataset")
    parser.add_argument("--model", type=str, required=True, help="Path to the trained model")

    args = parser.parse_args()

    evaluate_model(args.input, args.model)
