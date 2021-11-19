#     # Create an app that supports multiple Shopping Lists.
#     # Each SHopping list will contain multiple items.

# create_list = []
# import sys
# from create_list import create_list
# from add_item import add_item
shopping_lists = {
        "Kroger": ["egg", "milk", "bread", "juice"],
        "Walmart": ["lightbulb", "toy", "snacks"],
        "Target" : ["shampoo", "clothes", "energy drink"]
}


def main():  
    print("""SHOPPING LIST
Select a number for the action you would like to do

1. Create shopping list
2. Add item to shopping list
3. Remove item from shopping list
4. Clear shopping list
5. Exit
""")

    selection = input("Make your selection: ")

    if selection == "1":
        while True:
            store_name = input("Store Name: ")
            if store_name not in shopping_lists:
                shopping_lists[store_name] = []
                print(f"List added: {store_name}")
                print(shopping_lists)
                break
            else:
                print(f"List with name '{store_name}' already exists")
    else:
        print("You did not make a valid selection.")
    

    if selection == "2":
        while True:
            add_item = input("Name of the item: ")
            if add_item not in shopping_lists[{}]:
                add_item.append = [{}]
                print(f"Item added. {add_item} ")
                print(add_item)
                break
            else:
                print(f"List with name '{add_item}' already exists ")

            

main()


# def add_item ():
#     item = input("Enter the item you wish to add to the shopping list: ")
#     shopping_list.append(item)
#     print(item + " has been added to the shopping list. ")

# def remove_item ():
#     item = input("Enter the item you would like to remove from the shopping list: ")
#     shopping_list.remove(item)
#     print(item + " has been removed from the shopping list. ")
