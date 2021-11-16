# write a function that returns true if the two input strings start witt the same letter
# write a script that asks the user for their name. Ask them for the food they are bringing to the picnic
# 

what_is_your_name = input("what is your name? ")
what_food = input("what food are you bringing" )

def checkGuestInvite(what_is_your_name, what_food):
    if (what_is_your_name[0] == what_food[0]):
        return True
    else:
        return False

print ("Are you invited to the party? " + str(checkGuestInvite(what_is_your_name, what_food)))

# def guest_is_allowed(name, food):             **Lachlan's example"**
#     if name[0] == food[0]:
#         return True
#     else:
#         return False

# user_name = input("Name? ")
# user_food = input("Food?" )

# if guest_is_allowed(user_name, user_food):
#     print("You're in!")
# else:
#     print("Try a different food! ")