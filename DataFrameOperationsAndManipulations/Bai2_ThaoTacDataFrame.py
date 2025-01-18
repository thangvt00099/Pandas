import pandas as pd
data = {
    'Name': ['John', 'Emma', 'Michael', 'Sophia'],
    'Height': [5.5, 6.0, 5.8, 8.3],
    'Qualification': ['BSc', 'BBA', 'MBA', 'BSc'],
}
df = pd.DataFrame(data)
address = ['New York', 'London', 'Sydney', 'Toronto']

# Thêm cột mới
df['Address'] = address
print(df)
print('=================')

print('Original DataFrame: ')
print(df)

# Thêm hàng mới
df.loc[len(df.index)] = ['Army', 5.2, 'BIT', 'Manchester']
print('Modified DataFrame: ')
print(df)