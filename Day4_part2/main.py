import random
option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
random_number = random.randint(0,2)
print(random_number)

if option == 0:
    print("You chose rock")
    if random_number == 0:
        print("The computer chose rock")
        print("It's a draw")
    elif random_number == 1:
        print("The computer chose paper")
        print("You lose")
    else:
        print("The computer chose scissors")
        print("You won")
elif option == 1:
    print("You chose paper")
    if random_number == 0:
        print("The computer chose rock")
        print("You won")
    elif random_number == 1:
        print("The computer chose paper")
        print("It's a draw")
    else:
        print("The computer chose scissors")
        print("You lose")

elif option == 2:
    print("You chose scissors")
    if random_number == 0:
        print("The computer chose rock")
        print("You lose")
    elif random_number == 1:
        print("The computer chose paper")
        print("You won")
    else:
        print("The computer chose scissors")
        print("It's a draw")
else:
    print("Option out of range")