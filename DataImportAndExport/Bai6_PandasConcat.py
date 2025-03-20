import pandas as pd
data1 = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['Emily', 'Michael', 'Sophia', 'Rita'],
    'Age': [28, 32, 27, 22],
    'City': ['Berlin', 'Tokyo', 'Sydney', 'Delhi']
}
df2 = pd.DataFrame(data2)

result_ignore_index = pd.concat([df1, df2], ignore_index=True)
result_sort = pd.concat([df1, df2], sort=True)
result_outer = pd.concat([df1, df2], axis=1)
result_inner = pd.concat([df1, df2], axis=1, join='inner')

print("Ignore Index = True\n", result_ignore_index)
print("\nSort = True\n", result_sort)
print("\nHorizontal Axis Outer\n", result_outer)
print("\nHorizontal Axis Inner\n", result_inner)
