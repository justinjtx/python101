# flipping coin
from random import randint


def flip_coin():
    print("You flipped a coin! ")
    value = randint(0,1)
    if value == 1:
        print("It's heads!")
    else:
        print("It's tails!")



# flip_coin = input("flip a coin")       << original sample 
# while flip_coin == "1":
#     print("You flipped a coin! ")
#     value = randint(0,1)
#     if value == 1:
#         print("It's heads!")
#     elif value == "q":
#         break
#     else:
#         print("It's tails!")
#     flip_coin = input("1 - flip a coin, q - exit ")


