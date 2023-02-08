#!/usr/bin/python3

# Variables & Methods #

print("\n#########\n")
words = "All is fair in love and war."
print(words + "\n") # print words as it's 
print(words.upper() + '\n') # print words in uppercase
print(words.lower() + '\n') # print words in lowercase
print(words.title() + '\n') # print words in title case

# lenght of words #
print('The Lenght Of is "Words Variables" is ' + str(len(words)) + '\n')


# Variables #

name = "Mahmoud" # String
age  = 23        # int
GPA  = 2.6       # float

print("\n#########\n")
print( "Your Name : " + name     )
print( "Your Age : "  + str(age) )
print( "Your GPA : "  + str(GPA) )

# print(name)
# print(age)
# print(GPA)

print("\n#########\n")

num = 30.45
print(num)
print(int(num))
print(float(num))

# print(30.45)
# print(int(30.45))
# print(float(30.45))

print("\n#########\n")

num_2 = 50
num_2 += 5
print(num_2)
num += num_2
print(num)
