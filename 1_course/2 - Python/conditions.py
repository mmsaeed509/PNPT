#!/bin/python3

# Conditional Statements #

def drink(money):
  if money >= 2:
    return "You've got yourself a drink!"
  else:
    return "NO drink for you!"

print(drink(10))
print(drink(1))

print("\n#########\n")

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "We need more money!"
    elif (age < 21 ) and (money >= 5):
        return "you're too little!"
    else:
        return "you're too Fuckin pooooor ,Fuckin young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(15,5))
print(alcohol(20,4))
