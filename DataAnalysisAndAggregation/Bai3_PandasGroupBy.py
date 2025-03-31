import pandas as pd
data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Sales': [1000, 500, 800, 300]
}
df = pd.DataFrame(data)

# group the DataFrame by the Category column and calculate the sum of Sales for each category
grouped = df.groupby('Category')['Sales'].sum()
# print(grouped)

data1 = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Grade': ['A', 'B', 'A', 'A', 'B'],
    'Score': [90, 85, 92, 88, 78]
}
df1 = pd.DataFrame(data1)
agg_functions = {
    'Score': ['mean', 'max']
}
grouped1 = df1.groupby(['Gender', 'Grade']).aggregate(agg_functions)
print(grouped1)