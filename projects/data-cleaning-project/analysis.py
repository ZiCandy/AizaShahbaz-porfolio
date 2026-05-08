import pandas as pd

# Sample dataset (we simulate real messy data)
data = pd.DataFrame({
    'Age': [25, None, 30, 45, 50],
    'Income': [50000, 60000, None, 80000, 90000],
    'City': ['NY', 'LA', None, 'Chicago', 'Houston']
})

print("Original Data:")
print(data)

# Step 1: Handle missing values
data_cleaned = data.dropna()

# Step 2: Reset index
data_cleaned = data_cleaned.reset_index(drop=True)

print("\nCleaned Data:")
print(data_cleaned)

# Step 3: Simple analysis
print("\nAverage Age:", data_cleaned['Age'].mean())
print("Average Income:", data_cleaned['Income'].mean())
