import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 28, 24],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Score': [85, 90, 75, 80, 95]
}
df = pd.DataFrame(data)

# chọn hàng có Age > 25
selected_rows = df[df['Age'] > 25]
print(selected_rows)
print('==============')

# sử dụng query()
selected_rows_query = df.query('Age > 25')
print(selected_rows_query)
print('==============')

# tạo 1 danh sách tên để chọn
names_to_filter = ['Bob', 'David']

# sử dụng isin() để chọn hàng dựa trên cột
selected_rows_isin = df[df['Name'].isin(names_to_filter)]
print(selected_rows_isin)
