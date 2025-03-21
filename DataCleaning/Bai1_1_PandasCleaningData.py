import pandas as pd
data = {
    'A': [1, 2, 2, 3, 3, 4],
    'B': [5, 6, 6, 7, 8, 8]
}

data1 = {
    'A': [25, 30, 35],
    'B': ['John', 'Doe', 'Smith'],
    'C': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print("Original DataFrame:\n", df.to_string(index=False))

# detect duplicates
print("\nDuplicate Rows:\n", df[df.duplicated()].to_string(index=False))

# remove duplicates based on column 'A'
df.drop_duplicates(subset=['A'], keep='first', inplace=True)
print("\nDataFrame after removing duplicates based on column 'A':\n", df.to_string(index=False))
print()

# rename columns
df1.rename(columns={'A': 'Age', 'B': 'Name', 'C': 'Salary'}, inplace=True)
print(df1.to_string(index=False))