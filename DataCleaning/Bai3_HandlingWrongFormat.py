import pandas as pd
data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
}
df = pd.DataFrame(data)
# convert temperature column to float
df['Temperature'] = df['Temperature'].astype(float)

# calculate the mean temperature
mean_temperature = df['Temperature'].mean()
print(mean_temperature)
print()

df_date = pd.DataFrame(
    {
        'date': ['2022-12-01', '01/02/2022', '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']
    }
)

# convert the date column to datetime format
df_date['date'] = pd.to_datetime(df_date['date'], format='mixed', dayfirst=True)
print(df_date)
