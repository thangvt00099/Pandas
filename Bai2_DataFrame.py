import pandas as pd
"""
    DataFrame giống như 1 bảng có hàng và cột (Mảng 2 chiều)
"""
print("========>Tạo DataFrame sử dụng Dictionary")
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

print("========>Tạo DataFrame sử dụng mảng 2 chiều")
data1 = [['John', 25, 'New York'],
         ['Alice', 30, 'London'],
         ['Bob', 35, 'Paris']]
df1 = pd.DataFrame(data1, columns=['Name', 'Age', 'City'])
print(df1)

print("========>Tạo DataFrame rỗng")
df2 = pd.DataFrame()
print(df2)