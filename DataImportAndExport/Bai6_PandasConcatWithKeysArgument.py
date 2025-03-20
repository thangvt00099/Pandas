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

result = pd.concat([df1, df2], keys=['from_df1', 'from_df2'])
print(result)