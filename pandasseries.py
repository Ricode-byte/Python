import pandas as pd

#1: Create the DataFrame and set Name as the index
data = {
    'Name': ['John', 'Jane', 'Jim', 'Jack'],
    'Age': [28, 32, 24, 29],
    'Department': ['IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 55000, 60000, 52000]
}

df = pd.DataFrame(data)
df.set_index('Name', inplace=True)

#2: Select all rows where the Department is 'IT'
it_department = df[df['Department'] == 'IT']
print("Rows where the Department is 'IT':")
print(it_department)

#3: Select all rows where the Age is greater than 28
age_greater_than_28 = df[df['Age'] > 28]
print("\nRows where Age is greater than 28:")
print(age_greater_than_28)

#4: Add a new column called Bonus, which is 10% of the Salary
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding the Bonus column:")
print(df)

#5: Increase the Salary of all employees in the Finance department by 5%
df.loc[df['Department'] == 'Finance', 'Salary'] *= 1.05
print("\nDataFrame after increasing Salary by 5% for Finance department:")
print(df)

#s6: Set the Age of all employees in the HR department to 35
df.loc[df['Department'] == 'HR', 'Age'] = 35
print("\nDataFrame after setting Age to 35 for HR department:")
print(df)
