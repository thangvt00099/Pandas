import pandas as pd
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [32, 75, 30, 77],
    'Humidity': [80, 10, 85, 5]
}

df = pd.DataFrame(data)
print('Original DataFrame\n', df)
print()

pivot_df = df.pivot(index='Date', columns='City', values='Temperature')
print('Reshaped DataFrame\n', pivot_df)
print()

pivot_df1 = df.pivot(index='Date', columns='City')
print('Reshaped DataFrame Again\n', pivot_df1)