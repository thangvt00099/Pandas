import pandas as pd
df = pd.read_fwf('data.txt', colspecs=[(0, 5), (5, 10), (10, 15)], names=['Name', 'Age', 'Height'])
print(df)
print()

df1 = pd.read_table('data.txt', sep='\s+', names=['Name', 'Age', 'Height'])
print(df1)