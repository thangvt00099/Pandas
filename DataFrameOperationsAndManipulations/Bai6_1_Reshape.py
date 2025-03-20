import pandas as pd
data = {
    'Date': ['2023-08-01', '2023-08-02'],
    'Category_A': [10, 20],
    'Category_B': [30, 40]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# set cột Date làm index
df.set_index('Date', inplace=True)

# sử dụng stack - xếp các cột thành hàng
stacked_df = df.stack()
print('Stack:\n', stacked_df)
print()

# sử dụng unstack - xếp hàng thành cột
unstacked_df = stacked_df.unstack()
print('Unstack:\n', unstacked_df)

data1 = {
    'Name': ['Alice', 'Bob'],
    'Math': [90, 85],
    'History': [75, 92]
}
df1 = pd.DataFrame(data1)
print("Original DataFrame:\n", df1)
print()

# sử dụng melt() - chuyển dữ liệu từ dạng rộng sang dài
melted = pd.melt(df1, id_vars='Name', var_name='Subject', value_name='Score')
print("Melted:\n", melted)