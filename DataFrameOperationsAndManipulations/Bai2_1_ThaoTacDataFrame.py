import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Felipe', 'Rita'],
    'Age': [25, 30, 35, 40, 22, 29],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Bogota', 'Banglore']
}
df = pd.DataFrame(data)
print('Original DataFrame: ')
print(df)
print('===============')

# Xóa hàng với index 4 - Không sử dụng tham số index thì phải dùng axis để chỉ xóa hàng hay cột
df.drop(4, axis=0, inplace=True)

# Xóa hàng với index 5
df.drop(index=5, inplace=True)

# Xóa hàng 1 với 3
df.drop([1, 3], axis=0, inplace=True)

print('Modified DataFrame: ')
print(df)
print('===============')