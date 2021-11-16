#  Write a script that asks the user for two numbers, then prints all of the 
# odd numbers including and between both numbers

# num1 = int(input("enter a number:"))
# num2 = int(input("enter anohter number: "))
# count = 0
# while count <= abs(num2 - num1):
#     print(min(num1, num2) + count)
#     count = count +1


num1 = int(input("enter a number:"))
num2 = int(input("enter another number: "))
count = num1

while count <= num2:
    print(count)
    count = count +1