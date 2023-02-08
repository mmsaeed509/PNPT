#!/bin/python3

moves = ["Hangover", "The Perkins", "Spiderman 3", "The Hunger Games", "The Exorcist"]

# print all items #
print(moves)

# print items No. 3 (as start from 0) #
print(moves[2])

# print from items No. 2 to items No. 4 #
print(moves[1:3])

# print items from No.2 to end #
print(moves[2:])

# print from items No. 2 to items No. 2 (print no thing) #
print(moves[2:2])

# print from first items to items No. 2 #
print(moves[:2])

# print last item #
print(moves[-1])

# print the lenght of the list #
print(len(moves))
print("The lenght of the list = " + str(len(moves)))

# add new item to list #
moves.append("OZIL")

print(moves)

# delete last item #
moves.pop()

print(moves)

# delete the 3rd item #
moves.pop(2)

print(moves)

