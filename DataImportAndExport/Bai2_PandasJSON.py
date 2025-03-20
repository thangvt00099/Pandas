import pandas as pd
df = pd.read_json('data.json')
print(df)
print()

df1 = pd.read_json('data1.json', orient='records', lines=True)
print(df1)