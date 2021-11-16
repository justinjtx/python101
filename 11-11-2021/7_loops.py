password = input("Enter the password: ")

while password != "friend":                 #!= <<< not equal to 
    print("Try again")
    password = input("Enter the password: ")



# infinite loop with break


while True:
    print("""
1. Flip a coin
2. Roll a dice
3. exit""")

    choice = input(": ")
    if choice == "1":
        print("flipping a coin!")
    elif choice =="2":
        print("rolling a dice!")
    elif choice =="3":
        print("bye!")
        break 


# accumulation

count = 0 

while count < 10:
    print(count)
    count = count +1