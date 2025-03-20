import pandas as pd
data = {
    'Name': ['John', 'Anna', 'John', 'Anna', 'John'],
    'Age': [28, 24, 28, 24, 19],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# sử dụng duplicated() để kiểm tra sự trùng lặp
print(df.duplicated())
print()

# kiểm tra trùng lặp dựa vào cột Name và Age
print(df.duplicated(subset=['Name', 'Age']))

# sử dụng drop_duplicates() để xóa trùng lặp
df.drop_duplicates(keep='last', inplace=True)
print(df)