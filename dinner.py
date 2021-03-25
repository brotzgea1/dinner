import random

show_menu = True
approved = []
filted_list = []
filt_approved = approved.copy()

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

def menu():
    print("Welcome to DinDin!")
    print("1. See what's for dinner!")
    print("2. Not in the mood for something? Let us know.")
    print("3. Add a restaurant from the list.")
    print("4. Delete a restaurant from the list.")
    print("5. Exit")
    selector = input("What would you like to do? Pick a number. ")
    if selector == "1":
        randomize()
    elif selector == "2":
        filter()
    elif selector == "3":
        addrest()
    elif selector == "4":
        delrest()
    elif selector == "5":
        raise SystemExit

def addrest():
    name = input("What is the name of the restaurant? ")
    cuisine = input("What type of restaurant is it? ")

    first = Restaurant(name, cuisine)
    approved.append(first)

def delrest():
    rest_one = input("What is the name of the restaurant? ")
    for item in approved:
        if rest_one == item.name:
            approved.remove(item)

def filter():
    filt_one = input("What aren't you in the mood for? ")
    for item in approved:
        if item == filt_one:
            filt_approved.remove(item)
            
def randomize():
    rando = random.choice(filt_approved)
    for item in filt_approved:
        if item == rando:
            print(item.name)

# while show_menu:
#     menu()
