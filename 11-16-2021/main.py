from greeter import greet_user


def main():
    user_choice = input("""Enter your choice
    1. Greet User
    q. Quit
    : """)
    if user_choice == "1":
            greet_user()
    elif user_choice == "q":
            exit()

main()