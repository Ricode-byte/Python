#1) Write a Python program to find the number of times 4 appears in the tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

count_of_4 = tuplex.count(4)

print(count_of_4)



#2) Write a Python program to convert a list to a tuple

listx = [5, 10, 7, 4, 15, 3]

tuplex = tuple(listx)

print(tuplex)


 #3) Write a Python program to calculate the sum of the numbers in a given tuple
 

numbers = (5, 10, 7, 4, 15, 3)


total_sum = sum(numbers)


print(total_sum)

 
 #4) Write a python program and iterate the given tuples
 
employee1 = ("Siddharth Mehta", 27, "Data", 60000)
employee2 = ("Rahul", 27, "Marketing", 55000)
employee3 = ("Ashu", 26, "Engineering", 75000)


employees = [employee1, employee2, employee3]


for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name: {name}, ID: {emp_id}, Department: {department}, Salary: {salary}")

