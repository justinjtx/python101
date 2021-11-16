    # Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times 
    # each letter in the alphabet was used in the word.
    # EXAMPLE)
    # Please enter a word: Banana
    # {"a" : 3, "b" : 1. "n" : 2}


# word = input("Please enter a word: ")

# letter_amount = {}

# for i in word:
#     if i in letter_amount:
#         letter_amount [i] += 1
#     else:
#         letter_amount[i] = 1
# print(f"Each letter amount is: {(letter_amount)}")


    # Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing
    # the tally of how many times each word in the alphabet was used in the text.
    # EXAMPLE)
    # Please enter a sentence: To be or not to be do be do be do
    # {'to': 2, 'be': 4, 'or': 1, 'not': 1, 'do': 3}

# word = input("Please enter a sentence: ")

# letter_amount = {}
# word_amount = ()

# for i in word:
#     if i in letter_amount:
#         letter_amount[i] += 1
#     else:
#         letter_amount[i] = 1
#     if i in word_amount:
#         word_amount[i] += 1
#     else:
#         word_amount[i] = 1
# print(f"Word used are: {(letter_amount)} {(word_amount)}")


sentence = input('Enter a sentence: ')
word_tally = {}
words = sentence.split()
for word in words:
    if word.lower() in word_tally:
        word_tally[word.lower()] += 1
    else:
        word_tally[word.lower()] = 1
print(f'Count of letters is:\n {(word_tally)}')