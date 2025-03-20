import pandas as pd

# create dataframes from the dictionaries
data1 = {
    'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'Name': ['John Doe', 'Jane Smith', 'Peter Brown', 'Tom Johnson', 'Rita Patel'],
    'DeptID': ['D001', 'D003', 'D001', 'D002', 'D006'],
}
employees = pd.DataFrame(data1)

data2 = {
    'DeptID': ['D001', 'D002', 'D003', 'D004'],
    'DeptName': ['Sales', 'HR', 'Admin', 'Marketing']
}
departments = pd.DataFrame(data2)

# left merge the dataframes
df_merge = pd.merge(employees, departments, how = 'cross')

print(df_merge)
