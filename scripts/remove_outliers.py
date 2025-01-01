import pandas as pd
import argparse
from scipy.stats import zscore

def remove_outliers(input_path, output_path):
    # Read the input CSV file
    data = pd.read_csv(input_path)
    
    # Perform outlier removal using z-score
    numeric_cols = data.select_dtypes(include=['float64', 'int64'])
    data = data[(zscore(numeric_cols) < 3).all(axis=1)]
    
    # Save the cleaned data to the output file
    data.to_csv(output_path, index=False)
    print(f"Outliers removed and data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove outliers from the data.")
    parser.add_argument("--input", type=str, required=True, help="Input CSV file path")
    parser.add_argument("--output", type=str, required=True, help="Output CSV file path")
    
    args = parser.parse_args()
    remove_outliers(args.input, args.output)
