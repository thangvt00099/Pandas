import pandas as pd
data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value1': [10, 15, 20, 25, 30, 35],
    'Value2': [5, 8, 12, 15, 18, 21]
}
df = pd.DataFrame(data)

# calculate total sum of the Value column
total_sum = df['Value1'].aggregate('sum')
print("Total Sum: ", total_sum)

# calculate the mean of the Value column
average_value = df['Value1'].aggregate('mean')
print("Average Value: ", average_value)

# calculate the maximum value in the Value column
max_value = df['Value1'].aggregate('max')
print("Maximum Value: ", max_value)

# applying multiple aggregation functions to a single column
result = df.groupby('Category')['Value1'].agg(['sum', 'mean', 'max', 'min'])
print(result)
print()

# applying different aggregation functions for other columns
agg_funcs = {
    'Value1': 'sum',
    'Value2': ['mean', 'max']
}
result1 = df.groupby('Category').aggregate(agg_funcs)
print(result1)