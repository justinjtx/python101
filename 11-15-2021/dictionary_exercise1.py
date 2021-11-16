    # Given the following dictionary, representing a mapping from names to phone numbers

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# Write code to the following and print the dictionary after each change

    #1.Print Elizabeth's phone number.

print(phonebook_dict['Elizabeth'])

    # #2.Add an entry to the dictionary: Kareem's number is 938-489-1234

phonebook_dict["Kareem"] = "938-489-1234"
print(phonebook_dict)

    #3. delete Alice's phone entry

del phonebook_dict['Alice']
print(phonebook_dict)

    #4. Change Bob's phone number to '968-345-2345'

phonebook_dict["Bob"] = "968-345-2345"
print(phonebook_dict)

    #5. Print all the phone entries using a loop

for numbers in phonebook_dict.items():
    print(numbers)
    

    # Nested dictionary

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
    { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
    { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
]
}

    #1. write a python expression that gest the email address of Ramit

print(ramit['email'])

    #2. write a python expression that gest the first of Ramit's interests

print(ramit['interests'][0])

    #3. write a python expression that gets the email address of Jasmine

print(ramit['friends'][0]['email'])

    #4. write a python expression that gest the second of Jan's two interests

print(ramit['friends'][1]['interests'][1])


