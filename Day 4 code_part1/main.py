# Randomization
import random
# random is a module that the python team created

# import my_module # This imports the code from my_module file
# #
#
# random_integer = random.randint(1, 10) # randint is a function
# print(random_integer)
#
#
# print(my_module.pi) # calling my_module file

# Generating random floating point numbers
# random_float = random.random() * 5 # This line generates a random floating point number between 0.0 and 4.99
# print(random_float)

# Heads or Tails program
# print("Welcome to a virtual coin toss program")
# random_num = random.randint(0, 1)
#
# if random_num == 1:
#     print("You played a heads")
# else:
#     print("You played a tails")



# Python list is a data structure
# You can use a list to store many pieces of related data

# states_of_america = ["Delaware", "Pennsylvania"]
# states_of_america.append("Alabama") #append adds an element at the last position of the list
# states_of_america.append("Chicago")
# states_of_america.insert(0, "Colorado")

# when using insert, ensure you indicate the position you want the add you're add occupy

# pop removes last element on the list except a specific index is mentioned
# states_of_america.pop()

# indexing helps to select a particular element in a list
# negative indexing selects the last element on the list

# print(states_of_america[-1])

# You can change or alter the items in the list
# states_of_america[0] = "North Dakota"
#
#
# # extend is used to extend an original list
# states_of_america.extend(["New Jersey","Connecticut", "Harizona"])
# print(states_of_america)


# Split string method
# names_string = input("Give me everybody's names, separated by a comma: ")
# names = names_string.split()
# names_len = len(names) #this line gets the length of the list
# random_name = random.randint(0, names_len - 1)
#
# print(f"{names[random_name]} is going to pay")


# Nested lists
# fruits = ["apple", "banana", "cherry"]
# vegetables = ["spinach", "kale", "Tomatoes", "Celery"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

#  Treasure Map
row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]
map1 = [row1, row2, row3]

# print(map1[1][2])
# print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row = int(position[0])
column = int(position[1])
map1[row - 1][column - 1] = "X"
# print(map1) # This line of code produces the same output like the line below it but this line prints the output horizontally
print(f"{row1}\n{row2}\n{row3}")

























