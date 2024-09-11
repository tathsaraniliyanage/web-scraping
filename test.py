import csv
import os

# Data to be written
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

try:
    # Write data to CSV file
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"File created successfully at: {os.path.abspath('output.csv')}")
except Exception as e:
    print(f"An error occurred: {e}")
