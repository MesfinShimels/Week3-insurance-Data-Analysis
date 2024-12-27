import pandas as pd
import matplotlib.pyplot as plt

# Assuming you already have `missing_data` DataFrame (as calculated in the previous step)
def missing_value(df):
# Assuming df is your DataFrame
 missing_values = df.isnull().sum()  # Calculate the number of missing values for each column
 total_entries = len(df)  # Total number of rows in the DataFrame
 missing_percentage = (missing_values / total_entries) * 100  # Calculate the percentage of missing values

# Combine both missing value count and percentage into a single DataFrame for better readability
 missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Missing Percentage': missing_percentage,
})

# Sort the result by the number of missing values (optional)
 missing_data_sorted = missing_data.sort_values(by='Missing Values', ascending=False)

# Display the result
 print(missing_data_sorted)
# Plotting the missing values count and missing percentage
 fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot for Missing Values Count
 ax[0].bar(missing_data.index[:-1], missing_data['Missing Values'][:-1], color='lightcoral')  # Exclude the 'Total' row for the bar chart
 ax[0].set_title('Missing Values Count per Column')
 ax[0].set_xlabel('Columns')
 ax[0].set_ylabel('Missing Values')
 ax[0].tick_params(axis='x', rotation=90)  # Rotate column names for better visibility

# Plot for Missing Values Percentage
 ax[1].bar(missing_data.index[:-1], missing_data['Missing Percentage'][:-1], color='lightblue')  # Exclude the 'Total' row for the bar chart
 ax[1].set_title('Missing Values Percentage per Column')
 ax[1].set_xlabel('Columns')
 ax[1].set_ylabel('Missing Percentage (%)')
 ax[1].tick_params(axis='x', rotation=90)  # Rotate column names for better visibility

# Show the plots
 plt.tight_layout()  # Adjust layout to avoid overlap
 plt.show()
