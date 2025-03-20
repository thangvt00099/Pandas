import pandas as pd
df = pd.read_csv('data.csv', header=0) # header=0 để set dòng đầu làm phần header của mỗi cột
print(df)
print()

# read CSV file with some arguments
df1 = pd.read_csv('data1.csv', header=None, names=['col1', 'col2', 'col3'], skiprows=2)
print(df1)