# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("You can't ride the rollercoaster")



# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")



# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height > 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are ${bill}.")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are ${bill}.")
#     else:
#         bill = 12
#         print(f"Adult tickets are ${bill}.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y" or wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
# else:
#     print("You can't ride the rollercoaster")



# BMI CALCULATOR
# BMI = weight(kg)/height **2 (m^2)
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / height ** 2)
#
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}")
#     print("You are underweight")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}")
#     print("You are normal")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}")
#     print("You are overweight")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}")
#     print("You are obese")
# else:
#     print("You are clinically obese")



# Leap year calculator
# year = int(input("Enter year: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         elif year % 400 != 0:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")



# Pizza order practice

# print("Welcome to Python Pizza Deliveries!")
#
# size = input("What pizza size do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want cheese? Y or N: ")
#
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is ${bill}")


# Love Calculator
print("Welcome to the Love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()


t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l" )
o = combined_string.count("o")
v = combined_string.count("v")
e1 = combined_string.count("e")

love = l + o + v + e1

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score} you are alright together.")
else:
    print(f"Your score is {love_score}")