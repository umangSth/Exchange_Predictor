import pandas as pd

# Read the raw data from the text file
file_path = 'raw.txt'

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process the lines to extract the date and rate
data = []
for line in lines[1:]:  # Skip the header line
    date, rate = line.strip().split('\t')
    data.append([date, float(rate)])

# Create a DataFrame from the processed data
df = pd.DataFrame(data, columns=['Date', 'Rate'])

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Save the DataFrame to a CSV file
output_csv_path = 'exchange_rate_data.csv'
df.to_csv(output_csv_path, index=False)

print(f"Data has been successfully written to {output_csv_path}")
