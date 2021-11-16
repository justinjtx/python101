# user_num = int(input("Enter a number: "))
# count = 1

# while count <= user_num:
#     output = ""
#     if count % 3 ==0:
#         output += 'fizz'
#     if count % 5 ==0:
#         output += 'buzz'
#     if output == '':
#         output = str(count)
#     print(output)
#    count+=1


number = input("give me a number")
count = 1
while count <= int(number):
    if count % 3 == 0 and count % 5 == 0:
        print('fizzbuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
        count= count + 1