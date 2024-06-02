import json

# Load the newline-delimited JSON data from the provided file
data = []
with open('eve.json') as f:
    for line in f:
        data.append(json.loads(line))

# Print a few records to understand the structure
print(data[:3])
