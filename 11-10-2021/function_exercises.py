def greetings(first_name, last_name):
    print("top of the morning to you, " + first_name + " " + last_name)

greetings("Justin", "Jung")
greetings("Steve", "Jobs")

def email(first_name, last_name, domain):
    print(first_name[0] + "." + last_name + domain)

email("J","Jung","@gmail.com")
email("S","Jobs","@yahoo.com")

def username(first_name, last_name):
    print(first_name[:3] + "_" + last_name[:5])

username("bob","Porterson")
username("steve","Jackson")

def contact(first_name, last_name, domain):
    greetings(first_name, last_name)
    print("Email:")
    email(first_name[0], last_name, domain)
    print("Username:")
    username(first_name[:3], last_name[5])

contact_info =("Justin" + "Jung" + "domain")


first = input('Last Name: ')
last    = input('Last Name: ')
domain = input('Domain: ')

contact_info(first, last, domain)
    