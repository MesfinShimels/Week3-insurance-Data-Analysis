import pandas as pd

def txt_to_csv(input_txt_file, output_csv_file, delimiter="\t"):
    """
    Converts a .txt file to a .csv file.

    Parameters:
        input_txt_file (str): Path to the input .txt file.
        output_csv_file (str): Path to the output .csv file.
        delimiter (str): Delimiter used in the .txt file. Default is tab (\t).

    Returns:
        None
    """
    try:
        # Read the .txt file into a DataFrame
        data = pd.read_csv(input_txt_file, delimiter=delimiter)
        
        # Save the DataFrame to a .csv file
        data.to_csv(output_csv_file, index=False)
        print(f"File converted successfully! Saved as {output_csv_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:

