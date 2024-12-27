# src/clean_data.py

import pandas as pd
import argparse

def clean_data(input_path, output_path):
    # Read the input CSV file
    data = pd.read_csv(input_path)
    
    # Perform data cleaning
    # Example: Drop rows with missing values
    data = data.dropna()
    
    # Save the cleaned data to the output file
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean the data.")
    parser.add_argument("--input", type=str, required=True, help="Input CSV file path")
    parser.add_argument("--output", type=str, required=True, help="Output CSV file path")
    
    args = parser.parse_args()
    clean_data(args.input, args.output)
