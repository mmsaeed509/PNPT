#!/bin/python3

# ----- Functions ----- #

## -------------------------------------- ##

print("\n########################\n")

# this is a function example #
def who_am_i():
    name = "Mahmoud Mohamed"
    age  = 23
    print( "Your Name : " + name     )
    print( "Your Age : "  + str(age) )

# call the function (execute) #
who_am_i()

## -------------------------------------- ##

print("\n########################\n")

# add parameter #
def add_on_hundred(num):
    print(num + 100)

# execute #
add_on_hundred(50)

## -------------------------------------- ##

print("\n########################\n")

# with multiple parameters #

# --- addition --- #
def addition(num_1,num_2):
    print(num_1 + num_2)

# --- multiplication --- #
def multiplication(num_1,num_2):
    return num_1 * num_2

# --- square root --- #
def square_root(num):
    print(num ** 0.5)
    
# execute #
addition(7,8.5)
addition(10,15)

print(multiplication(2,5))

square_root(9)
