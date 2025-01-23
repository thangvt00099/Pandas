import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}

df = pd.DataFrame(data)

# Truy cập 1 cột
names = df['Name']
print(names)
print('====================')

# Truy cập nhiều cột
name_city = df[['Name', 'City']]
print(name_city)
print('====================')

# df.loc[row_indexer, column_indexer]
# Truy cập 1 hàng đơn
single_row = df.loc[2]
print(single_row)
print('====================')

# Truy cập hàng 0, 3, 4
row_list = df.loc[[0, 3, 4]]
print(row_list)
print('====================')

# Truy cập 1 danh sách của cột
column_list = df.loc[:, ['Name', 'Age']]
print(column_list)
print('====================')

#  Truy cập hàng 2 cột Name
specific_value = df.loc[1, 'Name']
print(specific_value)
print('====================')

# Slicing sử dụng loc
# Cắt từ hàng 1 -> 3
slice_rows = df.loc[1:3]
print('Sliced Rows:')
print(slice_rows)
print('====================')

# Cắt từ 'Name' -> 'Age'
slice_columns = df.loc[:, 'Name':'Age']
print('Sliced Columns:')
print(slice_columns)
print('====================')

# Sử dụng Boolean với indexing bằng loc
boolean_index = df.loc[df['Age'] > 30]
print('Filtered DataFrame:')
print(boolean_index)
