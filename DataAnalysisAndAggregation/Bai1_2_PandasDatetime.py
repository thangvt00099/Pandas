import pandas as pd
df = pd.DataFrame({
    'datetime': ['2020-01-01', '2022-02-02', '2023-03-03']
})
df['datetime'] = pd.to_datetime(df['datetime'])

df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day

# get the day of the week
df['day_of_week'] = df['datetime'].dt.day_name()

# get the week of the year
df['week_of_year'] = df['datetime'].dt.isocalendar().week

# check for leap year
df['leap_year'] = df['datetime'].dt.is_leap_year
# print(df)

dates = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']
# create a DataFrame with DatetimeIndex
df1 = pd.DataFrame({'value': [10, 20, 30, 40, 50]}, index=pd.to_datetime(dates))
print(df1)