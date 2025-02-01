import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 27, 29],
    'Salary': [50000, 60000, 45000, 55000, 52000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
}

df = pd.DataFrame(data)

# Chọn 1 cột
name_column = df['Name']
print('Selecting single column: Name')
print(name_column)
print('==============')

# Chọn nhiều cột
age_salary_columns = df[['Age', 'Salary']]
print('Selecting multiple column: Age and Salary')
print(age_salary_columns.to_string(index=False))
print('==============')

# Chọn hàng sử dụng slicing
selected_rows = df[1:4]
print('Selecting rows 1 to 3:')
print(selected_rows.to_string(index=False))
print('==============')

print(f"Original DataFrame \n {df} \n")

# sử dụng loc để chọn hàng và cột bằng nhãn
# chọn hàng 1 -> 3 và cột Name và Tuổi
selected_data_loc = df.loc[1:3, ['Name', 'Age']]
print(selected_data_loc.to_string(index=False))
print('==============')

# sử dụng iloc để chọn hàng và cột bằng index
# chọn hàng 1 -> 3 và cột Name và Age
selected_data_iloc = df.iloc[1:4, 0:2]
print(selected_data_iloc.to_string(index=False))
print('==============')