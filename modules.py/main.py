from flip_a_coin import flip_coin
from roll_a_die import roll_dice

def main():
    user_choice = input("""Please choose an option:
    1 - flip a coin
    2 - roll a die
    q - exit   
    : """)
    
    if user_choice == "1":
        flip_coin()
    elif user_choice == "2":
        roll_dice()
    elif user_choice == "q":
            exit()
    main()
main()