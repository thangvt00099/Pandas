import pandas as pd
data = {
    'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Sử dụng pivot method
pivot_df = df.pivot(index='Date', columns='Category', values='Value')
print("Reshape DataFrame:\n", pivot_df)

data1 = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df1 = pd.DataFrame(data1)
print("Original DataFrame:\n", df1)

# Sử dụng pivot_table()
pivot_table_df1 = df1.pivot_table(index='Category', values='Value', aggfunc='mean')
print("Reshape DataFrame:\n", pivot_table_df1)