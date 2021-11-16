

def odd():


    # Checking if input is number
    while True:
        number = input("Pick a number: ")
        if number.isdigit() == True:
            number = float(number)
            break
        else:
             print("That's not a number!")

    # checking if input matches conditions
        
        if number % 2 !=0 and number % 3 ==0:
            print("Yes you're number is odd and divisible by 3. good job")
            return True
        else:
            print("Try again!")
            return False

odd()