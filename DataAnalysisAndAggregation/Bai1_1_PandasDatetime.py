import pandas as pd
df = pd.DataFrame({
    'year': [2021, 2022, 2023],
    'month': [1, 2, 3],
    'day': [1, 2, 3],
    'hour': [10, 11, 12],
    'minute': [30, 45, 0],
    'second': [0, 0, 0]
})
# combine date and time columns to create a datetime column
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute', 'second']])
print(df)