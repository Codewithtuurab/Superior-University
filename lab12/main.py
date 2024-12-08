import csv
import json
import pandas as pd

# Load CSV data into a Pandas DataFrame
filenameCsv = 'train.csv'
csv_data = pd.read_csv(filenameCsv)

# Display basic information about CSV data
print("First 10 rows of CSV data:")
print(csv_data.head(10))

print("\nLast 10 rows of CSV data:")
print(csv_data.tail(10))

# Analyze specific columns in CSV data
column_name = 'Gender'
print(f"\nUnique values and count in column '{column_name}' of CSV data:")
print(csv_data[column_name].value_counts())

# Load JSON data into a Python object (list of dictionaries)
filenameJson = 'data.json'
with open(filenameJson, 'r') as file:
    json_data = json.load(file)

# Convert JSON data into a Pandas DataFrame
json_df = pd.DataFrame(json_data)

# Display basic information about JSON data
print("\nFirst 10 rows of JSON data:")
print(json_df.head(10))

print("\nLast 10 rows of JSON data:")
print(json_df.tail(10))

# Analyze specific columns in JSON data
column_name = 'Gender'
print(f"\nUnique values and count in column '{column_name}' of JSON data:")
print(json_df[column_name].value_counts())

# Descriptive statistics and information for both CSV and JSON data
print("\nDescriptive statistics for CSV data:")
print(csv_data.describe())

print("\nConcise summary of CSV data:")
print(csv_data.info())

print("\nDescriptive statistics for JSON data:")
print(json_df.describe())

print("\nConcise summary of JSON data:")
print(json_df.info())

# Handling missing data
print("\nColumns with missing data in CSV data:")
print(csv_data.isnull().sum())

print("\nColumns with missing data in JSON data:")
print(json_df.isnull().sum())

# Example data manipulations
# Here you can perform operations like dropping columns, handling missing values, creating new columns, etc.

# Example: Adding a new column to both datasets
csv_data['TotalIncome'] = csv_data['ApplicantIncome'] + csv_data['CoapplicantIncome']
json_df['TotalIncome'] = json_df['ApplicantIncome'] + json_df['CoapplicantIncome']

# Example: Dropping a column from both datasets
csv_data.drop('CoapplicantIncome', axis=1, inplace=True)
json_df.drop('CoapplicantIncome', axis=1, inplace=True)

# Example: Dropping a row based on a condition (assuming 'Loan_ID' exists)
csv_data.drop(csv_data[csv_data['Loan_ID'] == 1].index, inplace=True)
json_df.drop(json_df[json_df['Loan_ID'] == 1].index, inplace=True)

# Example: Separating features (X) and target variable (y) from CSV data
X = csv_data.drop('Loan_Status', axis=1)
y = csv_data['Loan_Status']

# Displaying the first few rows of X and y to verify separation
print("\nFirst 5 rows of X (features):")
print(X.head())

print("\nFirst 5 rows of y (target variable):")
print(y.head())
