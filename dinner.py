import random
# from consolemenu import *
# from consolemenu.items import *

# menu = ConsoleMenu("DinDin", "It's what's for dinner!")

# function_item = FunctionItem("See what's for dinner!", input, ["Enter an input"])

# menu.append_item(function_item)

# menu.show()

approved = []

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

def addrest():
    name = input("What is the name of the restaurant? ")
    cuisine = input("What type of restaurant is it? ")

    first = Restaurant(name, cuisine)
    approved.append(first)

def delrest():
    value = input("What is the name of the restaurant? ")
    for item in approved:
        if value == item.name:
            approved.remove(item)

def randomize():
    value = random.choice(approved)
    for item in approved:
        if item == value:
            print(item.name)

addrest()
addrest()
randomize()