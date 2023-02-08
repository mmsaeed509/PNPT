#!/bin/python3

# Dictionaries take key/value pairs {} #

# drink name -> key, price -> value #
drinks = {"schweppes gold":6, "Coca Cola":5, "fayrouz":7}
print(drinks)

# update value #
drinks["fayrouz"] = 10
print(drinks)

# employees = {"Finance":["omar", "Hassan"],"IT":["Hashem","Hassan"],"Cybersecurity":["ozil", "abdallah"]}

employees = {

    "Finance":["omar", "Hassan"],
    "IT":["Hashem","Hassan"],
    "Cybersecurity":["ozil", "abdallah"],

}

print(employees)
# add new key/value #
employees["HR"] = ["Mona", "Sara"]
print(employees)

employees.update({"Sales":["Ali", "Ahmed"]})
print(employees)

# print a specific key/value #
print(employees.get("Cybersecurity"))
