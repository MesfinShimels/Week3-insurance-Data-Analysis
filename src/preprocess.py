import pandas as pd
import os

def preprocess_data(input_path, output_path):
    # Load the data
    data = pd.read_csv(input_path)

    # Example preprocessing steps
    data['TransactionMonth'] = pd.to_datetime(data['TransactionMonth'], errors='coerce')
    data.fillna(0, inplace=True)  # Fill missing values with 0
    data = pd.get_dummies(data, drop_first=True)  # Encode categorical variables

    # Save the processed data
    data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess the data.")
    parser.add_argument("--input", type=str, required=True, help="Path to input dataset")
    parser.add_argument("--output", type=str, required=True, help="Path to save preprocessed dataset")

    args = parser.parse_args()

    preprocess_data(args.input, args.output)
