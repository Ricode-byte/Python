# Write a Python program to Get Only unique items from two sets. 
# Input: set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70} 
# Output: {70, 40, 10, 50, 20, 60, 30} 

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1 | set2  
print("Unique items from both sets:", unique_items)


# 2. Write a Python program to Return a set of elements present in Set A or B, but not both. 
# Input: set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70}
# Output: {20, 70, 10, 60} 

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
unique_items = set1 ^ set2  # You can also use set1.symmetric_difference(set2)

print("Elements present in either set1 or set2, but not both:", unique_items)


# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements. 
# Input: set1 = {10, 20, 30, 40, 50} 
# set2 = {60, 70, 80, 90, 10} 
# Output: {10}

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find common elements (intersection of two sets)
common_elements = set1 & set2  # You can also use set1.intersection(set2)

# Display the common elements if any
if common_elements:
    print("Common elements between set1 and set2:", common_elements)
else:
    print("No common elements between set1 and set2.")



# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
# Input: set1 = {10, 20, 30, 40, 50} 
# set2 = {30, 40, 50, 60, 70} 
# Output: {40, 50, 30}

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find common elements (intersection of two sets)
common_elements = set1 & set2  # You can also use set1.intersection(set2)

set1 = common_elements
print("Updated set1 with only common elements:", set1)
