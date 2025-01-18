import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Height': ['165', '178', '185', '171'],
    'Profession': ['Engineer', 'Entrepreneur', 'Unemployed', 'Actor'],
    'Marital Status': ['Single', 'Married', 'Divorced', 'Engaged']
}

data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Height': ['165', '178', '185', '171'],
    'Profession': ['Engineer', 'Entrepreneur', 'Unemployed', 'Actor'],
    'Marital Status': ['Single', 'Married', 'Divorced', 'Engaged']
}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print('Original DataFrame: ')
print(df)
print('============')

# Xóa cột tuổi
df.drop('Age', axis=1, inplace=True)

# Xóa cột Marital Status
df.drop(columns='Marital Status', inplace=True)

# Xóa cột Height và Profession
df.drop(['Height', 'Profession'], axis=1, inplace=True)
print('Modified DataFrame: ')
print(df)
print('============')

print('Original DataFrame1: ')
print(df1)

# Đổi tên cột Name
df1.rename(columns={'Name': 'First_Name'}, inplace=True)

# Đổi tên nhiều cột
df1.rename(mapper={'Age': 'Number', 'City': 'Address'}, axis=1, inplace=True)
print('Modified DataFrame1: ')
print(df1)
