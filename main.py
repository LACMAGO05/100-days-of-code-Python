print("Hello world!"+ " " + "My name is Lacmago Rebecca") #concatenating strings
# or print("Hello world!" + " My name is Lacmago Rebecca") #concatenating strings
# or print("Hello world! " + "My name is Lacmago Rebecca") #concatenating strings
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# The input function used to get user input
#print("Hello " + input("What is your name?"))

name = input("What is your name? ")
print(len(name))
# or
name = input("What is your name? ")
length = len(name)
print(length)

# The line below performs the same thing as line 11 and 12
# print( len ( input("What is your name? ") ) )

# swapping values of variables
a = input("a: ")
b = input("b: ")
c = a # c here represents a variable that will hold the value of a. While it holds the value of a, a is now empty. Now that a is empty, we can now pass b to it
a = b
b = c
print("a:", a)
print("b:", b)

# A band name generator
print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + petName)
