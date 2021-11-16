




#             # create a list of numbers, print their sum
# # sum = 0 
# # for n in numbers:
# #     sum = sum + n
# # print(sum)




#             # create a list of numbers, print the highest numbers
# # current_largest_number = numbers[0]

# # for i in range(len(numbers)):
# #     if numbers[i] > current_largest_number: 
# #         current_largest_number = numbers[i]




# # print(current_largest_number)




#             # create a list of numbers, print each number in the list that is even
# # even_numbers = []
# # for n in numbers:
# #     #check if n is even
# #     if n % 2 == 0:
# #         # add to the even_number list
# #         even_numbers.append(n)
# # print(even_numbers)


# numbers = [289, 12, -1, 8, 9999, 37, 0, -111, 9, -50, -9999,]

#             # create a list of numbers, print each number in the list that is greater than zero

# # positive_number = []
# # for n in numbers:
# #     #check if n is positive
# #     if n > 0:
# #         # add to the positive_number list
# #         positive_number.append(n)       
# # print(positive_number)



#             # create a list of numbers, create a new list which contains every number in the given list which is positive

# # list = []

# # for n in numbers:
# #     if n > 0:
# #         print(n, end= " ")
# #print()

# # print(list)

#             # print multiplication from 1 to 10

# # for n in range(1,11):

# #     for j in range(1,11):
# #         sum = n * j
# #         print(str(j) + " x " + str(n) + " = " + str(sum))


# #   greeting = "Hello there and good morning"
# #     def reverse(string):
# #         return string[::-1]
# #     print(reverse(greeting)

# txt = "hello world" [::-1]
# print(txt)

# # list = [9,1,3,5,6,7,9]
# # new_list = []
# # for n in list:
# #     if n not in new_list:
# #         new_list.append(list)

# # print(new_list)

#             # debub
#             # Given a list of numbers or strings, create a new list containing the same elements as the first list,
#             # except with any duplicate values removed. Print the list.

# # duplicate_list = ["d","a", "b" "q", "t"]
# # new_list = []

# # def remove_duplicates(duplicate_list):
# #     for i in duplicate_list:
# #         if i not in new_list:
# #             new_list.append(i)
# #         return new_list

# # print(remove_duplicates(duplicate_list))



# # Given a paragraph of text as a String, print the paragraph in leetspeak.

# # string = "I am a leet programmer"
# # translation = ""

# # for letter in string:
# #     if letter == "a" or letter == "A":
# #         translation += "4"
# #     elif letter == "e" or letter == "E":
# #         translation += "3"
# #     elif letter == "g" or letter == "G":
# #         translation += "6"
# #     elif letter == "i" or letter == "I":
# #         translation += "1"
# #     elif letter == "o" or letter == "O":
# #         translation += "0"
# #     elif letter == "s" or letter == "S":
# #         translation += "5"
# #     elif letter == "t" or letter == "T":
# #         translation += "7"
# #     else:
# #         translation += letter
# # print(translation)

# # Given a word as a string, print the result of extending any long vowels to the length of 5
# # Good, Cheese, Man, Spoon

    
# # word = input("Your word: ")
# # word = word.replace("oo", "ooooo")
# # word = word.replace("ee", "eeeee")
# # print(word)

# string = "Emma is a Cooper's mom"
# new_string = ""
# vowels = ["a", "e", "i", "o", "u"]

# for i in range(len(string)):
#     if string[i] in vowels:
#         if string[i] == string[i + 1]:
#             new_string += string[i * 4]
#         else:
#             new_string+= string[i]
#     else:
#         new_string += string[i]


# print(new_string)


# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

# cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"
# offset = 13
# decoded = ""
# for letter in cipher:
#     ascii_code =  ord(letter)
#     if ascii_code >= 97 and ascii_code <= 122:
#         decode_letter = ascii_code + offset
#         if decode_letter >= 122:
#             new_letter = chr(decode_letter - 26)
#         else:
#             new_letter = chr(decode_letter)
#     else:
#         new_letter = chr(ascii_code)
#     decoded += new_letter
# print(decoded)   

            # Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying
# the pairs of numbers in corresponding positions in the two lists. 

numbers_a = [2, 4, 5]
numbers_b = [2, 3, 6]
result = []

for i in range(len(numbers_a)):
    product = numbers_a[i] * numbers_b[i]
    result.append(product)
print(result) 

