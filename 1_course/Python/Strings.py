#!/bin/python3

name = "Mahmoud"

print(name[0])

full_name = "Mahmoud Mohamed Saeed Ahmed"

print(full_name)

# print first word #
print(full_name[0:7])
print(full_name[:7])

# split name (default to remove is space ' ') #
print(full_name.split())


full_name_split = full_name.split()

# add spce ' ' #
full_name_join = ' '.join(full_name_split)

print(full_name_join)

words_with_qoutes = "He said, \"give me all your money\""
print(words_with_qoutes)

words_with_qoutes_2 = "He said, 'give me all your money'"
print(words_with_qoutes_2)

words_with_qoutes_3 = 'He said, "give me all your money"'
print(words_with_qoutes_3)

words_with_qoutes_4 = 'He said, \'give me all your money\''
print(words_with_qoutes_4)

# remove too much space #
too_much_space = "          Hello          "
print(too_much_space)
print(too_much_space.strip())

# check if exist #

print("A" in "Apple")
print("a" in "Apple")
print("A " in "Apple")
print("a " in "Apple")

letter = "A"
word = "Apple"

print(letter.lower() in word.lower())

fav_movie = "The Hangover"
print("My favorite movie is " + fav_movie + ".")
print("My favorite movie is {}.".format(fav_movie))

