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