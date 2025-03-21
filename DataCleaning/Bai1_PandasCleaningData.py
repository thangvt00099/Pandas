import pandas as pd
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}

data1 = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print("Original Data:\n", df)
print()

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n", df_cleaned)
print()

# use fillna() to fill NaN values with 0
df.fillna(0, inplace=True)
print("Data after filling NaN with 0:\n", df)
print()

# use aggregate function to fill NaN values
df1.fillna(df1.mean(), inplace=True)
print("Data after filling NaN with mean:\n", df1)