import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
    'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
    'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']
}

df = pd.DataFrame(data)

# Hiển thị 3 dòng đầu tiên
print('First Three Rows: ')
print(df.head(3))
print('==========')

# Hiển thị 5 dòng đầu tiên
print('First Five Rows: ')
print(df.head())
print('==========')

# Hiển thị 3 dòng cuối
print('Last Three Rows: ')
print(df.tail(3))
print('==========')

# Hiển thị 5 dòng cuối
print('Last Five Rows: ')
print(df.tail())
print('==========')

# Lấy thông tin dữ liệu
df.info()

