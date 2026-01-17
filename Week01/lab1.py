# Sample Coding Questions 01 Week 01
# Arman Milani - 101555606

# Defining Variables: Define an array with elements 1, 4, 7, 9
Arr = [1, 4, 7, 9]

# Order of Operations
a = 1 
b = 2 
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = ((a - ((b ** c) // d)) + (a % c))
print("The value of e is:", e)
# Formatting: Print temperature with 3 decimal places
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Common Functions: Ask for age and filter by that age
userAge = int(input("Please enter your age: ")) + 22
print("Now showing the shop items filtered by age:", userAge)
