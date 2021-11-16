def valid():
    name = input("What is your user name?")
    if 3 < len(name) < 18:                           #len = legnth
        print("user name is valid")
    else:
        print("invalid username")

valid()