shopping_list = [
    {
        "Kroger": ["egg", "milk", "bread", "juice"]
    }
]

def add_item ():
    item = input("Enter the item you wish to add to the shopping list")
    shopping_list.append(item)
    print(item + " has been added to the shopping list. ")