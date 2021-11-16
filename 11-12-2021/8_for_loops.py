# names each name individually in differnet lines

# names = ["John","Bob", "Mosh", "Sarah", "Mary"]

# for name in names:                                          
#     print("Hello " + name)


# numbers = [8,2897,78632,2,10]
# total = 0
# for num in numbers:
#     total = total + num
#     print(total)


# pick up bucket
# start with number 1
    # take out an orange
    # slice the orange
        #take slice 1  
        # hand it out

menu = [
    ["pancakes", "waffles", "toast", "grits"],
        ["sandwich","salad"],
        ["lasagna", "steak", "burger", "soup"]
]

for group in menu:
    for item in group:
        print(item)

# *******      <<< what we're looking for
# *******
# *******
# *******
# *******

height = 5
width = 7

for i in range(0, height):
    row = ""
    for j in range(0, width):
        row += "*"
    print(row)


