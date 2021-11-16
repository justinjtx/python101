from random import randint

user_input = input("1 - flip coin, 2 - exit")

while user_input == "1":
    print("You flipped a coin!")
    value = randint(0,1)
    if value == 1:
        print("It is heads!")
    else:
        print("It is Tails!")

    user_input = input("1 - flip a coin, 2 - exit: ")
    