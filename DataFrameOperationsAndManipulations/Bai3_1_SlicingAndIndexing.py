import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# df.iloc[row_indexer, column_indexer]
# Truy cập 1 hàng
single_row = df.iloc[2]
print('Single Row:')
print(single_row)
print('=============')

# Truy cập hàng 0, 3, 4
row_list = df.iloc[[0, 3, 4]]
print('List of Rows:')
print(row_list)
print('=============')

# Truy cập cột 0 và 2
column_list = df.iloc[:, [0, 2]]
print('List of Columns:')
print(column_list)
print('=============')

# Truy cập 1 vị trí bất kì
specific_value = df.iloc[1, 0]
print('Specific Value:')
print(specific_value)
print('=============')

