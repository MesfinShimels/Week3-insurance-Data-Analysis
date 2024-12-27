import pandas as pd

def convert_txt_to_csv(txt_file_path):
    # Read the .txt file into a DataFrame with '|' as the separator
    df = pd.read_csv(txt_file_path, delimiter='|')
    
    # Write the DataFrame to a .csv file
    # df.to_csv(csv_file_path, index=False)
    print(f"File has been converted to CSV")
    return df

    
