import random

def roll_dice():
    possible_results = [1, 2, 3, 4, 5, 6]
    result = input("How many sides would you like ")
    result = random.choice(possible_results)
    print("The result is......." + str(result))




