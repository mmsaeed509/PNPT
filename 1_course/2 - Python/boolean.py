#!/bin/python3

# Boolean Expressions #

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)

print(type(bool1))

print("\n#########\n")

# Relational and Boolean Operators #

greater_than = 7 > 5
less_than =  5 < 7
greater_than_equal_to = 7 >= 7 
less_than_equal_to = 7 <= 7

test_and1 = (7 > 5) and (5 < 7)  # True
test_and2 = (7 < 5) and (7 > 5)  # False
test_or =  (7 > 5) or (5 < 7)  # True
test_or2 = (7 < 5) or (5 > 7)  # False

test_not = not True  # False

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)
print(test_and1,test_and2,test_or,test_or2)
print(test_not)
