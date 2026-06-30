import pandas as pd

# Load dataset
df = pd.read_csv("DATA/SampleSuperstore.csv")
# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe()) 