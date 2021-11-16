meal = {
    #(key) : #(value) 
    "drink" : "beer",
    "appetizer" : "chips",
    "entree" : "fajita",
    "desert" : "flan",
    "paid" : False,
    "tip" : 20,
    
}

    #accessing key value
print(meal["entree"])

print(f"I will have the {meal['appetizer']} with a ")
    #check if key exists inside of dictionary
if "desert" in meal:
    print("You're getting another desert?")
else:
    print("You can definitely fit that in your macros, go on.... ")

    #adding new value
meal["steak"] = False
    #updating existing value    
meal["appetizer"] = "shrimp"
    #deleting existing value
del meal["desert"]
print(meal)

# fullname = {
#     "firstname" : "Justin",
#     "lastname" : "Jung"
# }

# # print(f"First Name Last Name \nHello my name is {fullname['lastname']}, {fullname['firstname']}")

# firstname = str(input("Enter your first name: "))
# lastname = str(input("Enter your last name: "))

# print(firstname + " " + lastname)
# print("My name is " + fullname['lastname'] + "," + ' ' + fullname['firstname'])



# meal = {
#     #(key) : #(value) 
#     "drink" : "beer",
#     "appetizer" : "chips",
#     "entree" : "fajita",
#     "desert" : "flan",
#     "paid" : False,
#     "tip" : 20,
#     # list
#     "guest_info" : {
#         "first_name" : "Justin",
#         "last_name" : "Jung",
#         "favorite_bartender":["Sharon", "Jeremy", "Pryce"]
#     }
# }

#     # accessing a list
# # print(meal["favorite_bartender"][1])
# print(meal["guest_info"]["last_name"])
# print(meal["guest_info"]["favorite_bartender"][1])


# name = {
#     "first_name" : "Justin",
#     "last_name" : "Jung",
#     "Address" : {
#         "Company_name" : "Avengers HQ",
#         "Street" : "123 Marvel Rd",
#         "City" : "Houston",
#         "State" : "TX",
#         "Country" : "USA"
#     }
# }

# print(f"Name: {name['first_name']}, {name['last_name']}")
# print(f"Address: {name['Address']['Company_name']}, \n\t {name['Address']['Street']}, \n\t {name['Address']['City']}, {name['Address']['State']}, {name['Address']['Country']}")