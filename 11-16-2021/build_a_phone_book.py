# build a phone book with menu

phone_book = {
    "Steve" : "111-111-1111",
    "Mark" : "222-222-2222",
    "Justin" : "333-333-3333"
}

def display_menu():
    print("""
    $ python3 phonebook.py.
    Electronic Phone Book.
    ======================
    1. Look up an entry
    2. Set an Entry 
    3. Delete an entry 
    4. List all entries 
    5. Quit 
    Choose one of the followings
    """)

display_menu()
entry_list = []


def entry_task():
    for n in range(0,len(entry_list)):
        entry = entry_list[n]
        print(f"{n + 1} - {entry['name']} - {entry['number']}")

while True:
    menu = input("Please choose one of the options above: ")

    if menu == "1":
        name = input("What is the person's name?")
        if name in phone_book:
            print(f"{name}:  {phone_book[name]}")
            

    elif menu == "2":
        name = input("What is your name?")
        number = input("What is your phone number?")
        phone_book[name] = number
        entry = {"name":name , "number":number}
        entry_list.append(entry)
        print(f"Entry stored for {name}")
    
    elif menu == "3":
        entry_task()
        delete = int(input("Which entry would you like to delete: "))
        del entry_list[delete - 1]
        print(f"Deleted entry for {name}")

    elif menu == "4":
        if entry_list == []:
            print("You have no entries")
            print(phone_book)
            continue
        else:
            entry_task()

    elif menu == "5":
            break

    else:
        print("You can only choose between 1-5!")

print("Thanks for using Electronic Phone book!")