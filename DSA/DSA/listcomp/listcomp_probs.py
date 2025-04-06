#https://www.tutorjoes.in/Python_example_programs/create_a_list_of_lengths_of_words_in_a_sentence_in_python
#remove odd numbers from lists

# numbers = [3,5,45,97,32,22,10,19,39,43]

# res = [num for num in numbers if num % 2 == 0]

# print(res)

#find all the numbers from 1 - 100 that are divisble by 7

#seven = [x for x in range(1, 100) if x % 7 == 0]

#print(seven)

#find all the numbers from 1 - 100 that have a 3 in them

# three = [x for x in range(1, 100) if '3' in str(x)]

# print(three)

#Count the number of spaces in a string

# string = 'Akhilesh is learning to code  !!! He will Improve'

# spaces = len([x for x in string if x == ' '])

# spaces_count = string.count(' ')
# print(spaces)
# print(spaces_count)

#Create a list of all the consonants in the string 

# string_consonants = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

# consonants = [x for x in string_consonants.lower() if x not in 'aeiou' and x.isalpha()]

# consonants_1 = []
# for x in string_consonants.lower():
#     if x not in 'aeiou' and x.isalpha():
#         consonants.append(x)

# print(consonants_1)

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)

# my_list = [ 'hi' , 4, 8.99, 'apple', ('t' ,'b' ,'n')]

# fruits = ['apple', 'banana', 'cherry']
# indexed_fruits = list(enumerate(fruits))
# # Result: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# print(indexed_fruits)
# my_list = ["hi", 4, 8.99, 'apple', ('b','n')]
# result = [(index, value) for index, value in enumerate(my_list)]
# print(result)


#Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

# list_a = [1, 2, 3, 4]

# list_b = [2, 3, 4, 5]

# list_comm = []
# list_uncomm = []

# for item in list_a:
#     if item in list_b:
#         list_comm.append(item)
#     else:
#         list_uncomm.append(item)

# # print("Common numbers:", list_comm)
# # print("Uncommon numbers:", list_uncomm)

# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# List comprehension for common elements
# list_comm = [item for item in list_a if item in list_b]

# # List comprehension for uncommon elements
# list_uncomm = [item for item in list_a if item not in list_b]

# print("Common numbers:", list_comm)
# print("Uncommon numbers:", list_uncomm)


#Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’

# sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

# numInSentence = [int(word) for word in sentence.split() if word.isdigit()]
 
# print(numInSentence)


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’

# oddeven = ['even' if num % 2 == 0 else 'odd' for num in range(20)]
# print(oddeven)
# Key Points:
# The if-else must go before the for loop in a list comprehension.
# Without an else, the condition acts as a filter (e.g., [x for x in range(20) if x % 2 == 0] would only include even numbers).


# Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)

# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_b = [2, 7, 1, 12]

# # Create a list of tuples for matching numbers
# matching_tuples = [(num, num) for num in list_a if num in list_b]

# print(matching_tuples)



# sentence = "The fox jumps over the lazy dog"

# # Split the sentence into words and filter those with length < 4
# short_words = [word for word in sentence.split() if len(word) < 4]

# print(short_words)


#Create a list of reversed strings from another list

# Source Code
# words = ["apple", "banana", "cherry"]
# reversed_words = [word[::-1] for word in words]
# print(words)
# print(reversed_words)
# Output
# ['apple', 'banana', 'cherry']
# ['elppa', 'ananab', 'yrrehc']

# even_sum_tuples = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 2 == 0]
# print(even_sum_tuples)