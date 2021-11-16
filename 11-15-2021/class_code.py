# table = [
#     {
#         "name" : "Steve Rogers",
#         "meal" : "Quesadilla",
#         "seat" : 1
#     },
#     {
#         "name" : "Tony Stark",
#         "meal" : "Burrtio",
#         "seat" : 2
#     },
#     {
#         "name" : "Bruce Banner",
#         "meal" : "Many Burrito",
#         "seat" : 3
#     },
# ]

    # Accessing a property inside a dictionary inside a list

# print(table[1]["main"])

# for guest in table:
#     # print(guest["meal"])
#     # print("Tony Stark at seat 2 is getting the Buritto")
#     print(f"{guest['name']} at seat {guest['seat']} is getting the {guest['meal']}")



    #Think about other properties that an eCommerce website would need for their customers. 
    #Add as many properties as you think would be necessary for successful interaction with these customers.

customer_info = [
    {
        "first name" : "Scott",
        "last name" : "Jackson",
        "username" : "python1",
        "email" : "python1@bootcamp.com",
        "product" : "pythonbook",
        "promotional" : False,
        "credit_card" : 1234,
        "address" : {
            "company" : "DigitalCraft",
            "street" : "123 python rd",
            "city" : "Houston",
            "state" : "TX",
            "country" : "USA"
        }

    },
    {
        "first name" : "Steve",
        "last name" : "Jobs",
        "username" : "java",
        "email" : "java@bootcamp.com",
        "product" : "javabook",
        "promotional" : False,
        "credit_card" : 4569,
        "address" : {
            "company" : "JavaScript",
            "street" : "123 java rd",
            "city" : "Houston",
            "state" : "TX",
            "country" : "USA"
        }
    },
    {
        "first name" : "Michael",
        "last name" : "Jordan",
        "username" : "CCC",
        "email" : "CCC@bootcamp.com",
        "product" : "C++book",
        "promotional" : False,
        "credit_card" : 2468,
        "address" : {
            "company" : "C++Craft",
            "street" : "123 CCC rd",
            "city" : "Houston",
            "state" : "TX",
            "country" : "USA"
        }
    }
]

for contact_card in customer_info:
    print(f"Customer name: {contact_card['first name']} {contact_card['last name']} \nCustomer Address: {contact_card['address']['company']}, {contact_card['address']['street']},{contact_card['address']['state']},{contact_card['address']['country']},")
    print(f"Customer Username: {contact_card['username']} \nCustomer's Product: {contact_card['product']} \nCustomer's last 4 card#: {contact_card["credit_card"]} ")