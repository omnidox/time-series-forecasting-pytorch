from alpha_vantage.timeseries import TimeSeries

# Function to read API key from a file
def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Path to your API key file
api_key_file_path = 'AlphaVantage.txt'  # Update this to the actual path of your api_key.txt file

# Read API key from the file
api_key = get_api_key(api_key_file_path)

# Initialize the TimeSeries class
ts = TimeSeries(key=api_key)

# Retrieve the daily adjusted data for a specific stock symbol
data, meta_data = ts.get_daily('IBM', outputsize='compact')

# Print the keys from the first entry to see available data variables
first_entry = next(iter(data.values()))
print(first_entry.keys())

# dict_keys(['1. open', '2. high', '3. low', '4. close', '5. volume'])