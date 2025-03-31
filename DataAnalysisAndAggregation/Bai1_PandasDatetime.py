import pandas as pd
date_string = '2001-12-24 12:38'
print("String: ", date_string)

# convert string to datetime
date = pd.to_datetime(date_string)
print("Datetime: ", date)
print(type(date))
print()

df = pd.DataFrame({
    'date': ['2021-01-13', '2022-10-22', '2023-12-03'],
    'date1': ['13-02-2021', '22-03-2022', '30-04-2023'],
    'date2': ['2023-10-02', '2025-03-28', '2025-03-29']
})
# df['date1'] = pd.to_datetime(df['date1'], dayfirst=True) #dayfirst=True hoạt động với format DD/MM/YYYY
df['date2'] = pd.to_datetime(df['date2'], format='%Y-%m-%d') #format là định dạng của dữ liệu vào
print(df)

