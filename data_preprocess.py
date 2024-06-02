import json
import pandas as pd

# Load the newline-delimited JSON data from the provided file
data = []
with open('eve.json') as f:
    for line in f:
        data.append(json.loads(line))

# Load and preprocess the data
df = pd.json_normalize(data)

# Convert timestamps to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract alert categories and severity
df['category'] = df['alert.category']
df['severity'] = df['alert.severity']

# Save preprocessed data to a new file
df.to_csv('preprocessed_data.csv', index=False)
