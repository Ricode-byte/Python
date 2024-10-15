# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
# Input:
# temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
import numpy as np

# Given temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Find days where the temperature is either greater than 35 or less than 5
hot_days = temperatures > 35
cold_days = temperatures < 5

# Combine both conditions to find extreme temperature days
extreme_days = hot_days | cold_days

# Output the results
print("Hot days temperatures:", temperatures[hot_days])
print("Cold days temperatures:", temperatures[cold_days])
print("Extreme days temperatures:", temperatures[extreme_days])


# 2. Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes.
# Input:
# monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

import numpy as np

# Given monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the array into a 2D array where each row represents a quarter
quarterly_sales = monthly_sales.reshape(4, 3)

# Output the results
print("Quarterly sales data:")
print(quarterly_sales)


# 3. Suppose you have a dataset containing customer data, and you want to split this data into two groups:
#    one group for customers who made a purchase in the last 30 days and another group for customers who haven't made a purchase in the last 30 days.
#    Input:
# customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110]) last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])
import numpy as np

# Given customer data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Create a boolean mask for customers who made a purchase in the last 30 days
recent_purchase_mask = last_purchase_days_ago <= 30

# Split the customer IDs based on the mask
customers_recent = customer_ids[recent_purchase_mask]
customers_not_recent = customer_ids[~recent_purchase_mask]

# Output the results
print("Customers who made a purchase in the last 30 days:", customers_recent)
print("Customers who haven't made a purchase in the last 30 days:", customers_not_recent)


# 4. Suppose you have two sets of employee data-one containing information about
# full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis.
# Input:
# # Employee data for full-time employees
# full_time_employees = np.array([
# [101, 'John Doe', 'Full-Time', 55000],
# [102, 'Jane Smith', 'Full-Time', 60000],
# [103, 'Mike Johnson', 'Full-Time', 52000]
# ])
# # Employee data for part-time employees
# part_time_employees = np.array([
# [201, 'Alice Brown', 'Part-Time', 25000], [202, 'Bob Wilson', 'Part-Time', 28000], [203, 'Emily Davis', 'Part-Time', 22000]
# 1)

import numpy as np

# Given data
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Concatenate the arrays along the vertical axis (axis=0)
combined_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

print(combined_employees)