# Data Types
# String
# print("Hello"[0]) # This line prints H. Subscripting is a method of pulling out a particular element from a string
#
# #  Integer
# # The computer reads 123_456_789 as 123456789
# print(123 + 123)
#
# # Float 3.14159
# # Boolean
# True
# False
#
# # Type conversation or casting is the process of changing a piece of data from one data type to another
#
# # len(12345) # len function doesn't like working with integers
#
# num_char = len(input("What is your name? "))
#
# new_num_char = str(num_char) # Converting integer  to string
#
# # print("Your name has " + num_char + " characters") # This line will show an error because string can only be concatenated with string
#
# print("Your name has " + new_num_char + " characters")
#
# # type function provides the data type
#
# print(type(num_char))
#
# print(70 + float("100.5"))
#
# num = input("Type a two digit number: ")
# num1 = int(num[0])
# num2 = int(num[1])
# sum1 = num1 + num2
# print(sum1)
#
# # Mathematical operations /*-+
# print(6/3)# Note whenever you divide any two numbers, you end with a floating point number
# print(2 ** 2)# ** means exponent

# Mathematical operations have priorities
# PEMDAS from left to right
# Parenthesis
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

# print(3 * (3 + 3) / 3 - 3)

# BMI CALCULATOR
# BMI = weight(kg)/height **2 (m^2)
# height = float(input("Enter your height in m: "))
# weight = int(input("Enter your weight in kg: "))
# bmi = int(weight / height ** 2)
# print(bmi)

# Rounding up and rounding down
# print(round(8 / 3)) #rounds 2.6666 to 3
# print(round(8 / 3, 2)) # 2 here specifies the number of decimal places you want to round it to. Note that the data type here is float
# print( 8 // 3 ) # // is a floor division meaning it rounds up to an integer. Note that the data type here is integer
#
# # f-strings makes it easy to mix strings and different data types
# age = 20
# print(f"hello my name is lacmago and I am {age} years old")

#
# yearly_days = 365
# yearly_weeks = 52
# yearly_months = 12
# current_age = int(input("What is your current age? "))
# years_remaining = 90 - current_age
# daysLeft = years_remaining * 365
# weeksLeft = years_remaining * 52
# monthsLeft = years_remaining * 12
# print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")

# Project Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00/5) * 1.12

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip = bill * percentage_tip / 100
total_bill = (bill + tip) / number_of_people
print(f"Each person should pay:", round(total_bill, 2))