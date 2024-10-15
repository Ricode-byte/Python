# Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
# Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
import numpy as np

# Input data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35°C)
hot_days_indices = np.where(temperatures > 35)[0] + 1
hot_days_temperatures = temperatures[temperatures > 35]

# Identify cold days (temperature < 5°C)
cold_days_indices = np.where(temperatures < 5)[0] + 1
cold_days_temperatures = temperatures[temperatures < 5]

# Output the results
print("Hot Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(hot_days_indices, hot_days_temperatures):
    print(f"{day}\t{temp}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for day, temp in zip(cold_days_indices, cold_days_temperatures):
    print(f"{day}\t{temp}")


# Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes.
import numpy as np

# Input data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the data to have 4 rows (quarters) and 3 columns (months per quarter)
quarterly_sales = monthly_sales.reshape(4, 3)

# Output the results
print("Quarter 1 Sales (in thousands of dollars):", quarterly_sales[0])
print("Quarter 2 Sales (in thousands of dollars):", quarterly_sales[1])
print("Quarter 3 Sales (in thousands of dollars):", quarterly_sales[2])
print("Quarter 4 Sales (in thousands of dollars):", quarterly_sales[3])

#. Suppose you have a dataset containing customer data, and you want to split this data into two groups: 
# one group for customers who made a purchase in the last 30 days and another group for customers who haven't made a purchase in the last 30 days.
import numpy as np

# Input data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Identify active customers (last purchase < 30 days ago)
active_customers = customer_ids[last_purchase_days_ago < 30]

# Identify inactive customers (last purchase >= 30 days ago)
inactive_customers = customer_ids[last_purchase_days_ago >= 30]

# Output the results
print("Active Customers (Last Purchase < 30 days ago):", active_customers)
print("Inactive Customers (Last Purchase ≥ 30 days ago):", inactive_customers)


# Suppose you have two sets of employee data-one containing information about
# full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis.
# Input:
# # Employee data for full-time employees
# full_time_employees = np.array([
# [101, 'John Doe', 'Full-Time', 55000],
# [102, 'Jane Smith', 'Full-Time', 60000],

import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine the two datasets
combined_employees = np.vstack((full_time_employees, part_time_employees))

# Output the combined data
print("Combined Employee Data:")
for employee in combined_employees:
    print(f"Employee ID: {employee[0]}, Name: {employee[1]}, Type: {employee[2]}, Salary: {employee[3]}")
