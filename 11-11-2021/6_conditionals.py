pancakes = int(input("How many pancakes? "))

if (pancakes <10):               #expression
    print('acceptable amount of pancakes')
elif(pancakes < 100):
    print('some one is a greedy guts')
elif(pancakes < 1000):
    print("wow now, that's too many")
else: 
    print('Too many pancakes emoji')

print('here: ' + ('p' * pancakes))

pancakes = 5

if (pancakes < 5):
    print('<5')

if (pancakes > 5):
    print('>5')

if (pancakes <= 5):
    print('<=5')

if (pancakes >= 5):
    print('>=5')

if (pancakes == 5):
    print('==5')   
