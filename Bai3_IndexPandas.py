import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

print("====> Default index:")
df = pd.DataFrame(data)
print(df)

print("====> Setting index")
df.set_index('Name', inplace=True) # set_index đưa cột được chỉ định thành index (ở đây là cột Name)
print(df)

print("====> Range index")
df = pd.DataFrame(data, index=pd.RangeIndex(5, 8, name='Index'))
print(df)
print()

print("==========> Rename index <==========")
df1 = pd.DataFrame(data)
print("===> Original DataFrame")
print(df1)
print()

df1.rename(index={0: 'A', 1: 'B', 2: 'C'}, inplace=True)
print("===> Modified  DataFrame")
print(df1)
print()

print("==========> Reset index <==========")
df1.reset_index(inplace=True)
print("===> Modified  DataFrame")
print(df1)
print()

print("=======> Truy cập hàng và cột")
second_row = df1.iloc[1]
print(second_row)

print("=======> Truy cập index")
print(df1.index)
print(df1.index.values)
