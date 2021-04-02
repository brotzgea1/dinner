from os import system, name
from time import sleep
import random

# Variables and lists:
show_menu = True
approved = []
filt_approved = []

# Class for the program
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

# Function that calls the main menu
def menu():
    system('cls')
    print("Welcome to DinDin!")
    print("")
    print("1. See what's for dinner!")
    print("2. Not in the mood for someting? Let us know.")
    print("3. Add a restaurant from the list.")
    print("4. Delete a restaurant from the list.")
    print("5. Exit")
    print("")
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

# Adds a new restaurant to both lists
def addrest():
    name = input("What is the name of the restaurant? ")
    cuisine = input("What type of restaurant is it? ")
    first = Restaurant(name, cuisine)
    approved.append(first)
    filt_approved.append(first)

# Deletes restaurant from both lists
def delrest():
    rest_one = input("What is the name of the restaurant? ")
    for item in filt_approved:
        if rest_one == item.name:
            filt_approved.remove(item)
    for item in approved:
        if rest_one == item.name:
            approved.remove(item)

# Clears filtered list, then filters by name or cuisine based on user input
def filter():
    filt_one = input("Not in the mood for something? Let us know. ")
    filt_approved.clear()
    for item in approved:
        if item.cuisine != filt_one and item.name != filt_one:
            filt_approved.append(item)

# tries to select a random element from filtered list, if empty it tries again with the regular list   
def randomize():
    try:
        rando = random.choice(filt_approved)
        for item in filt_approved:
            if item == rando:
                print(item.name)
    except:
        rando = random.choice(approved)
        for item in approved:
            if item == rando:
                print(item.name)
    sleep(5)

# class instantiation
first_restaurant = Restaurant("ChiChi's", "Mexican")
second_restaurant = Restaurant("Taco Bell", "Mexican")
third_restaurant = Restaurant("McDonald's", "American")
fourth_restaurant = Restaurant("Burger King", "American")
fifth_restaurant = Restaurant("China Castle", "Chinese")
sixth_restaurant = Restaurant("Mussel Burger", "American")
seventh_restaurant = Restaurant("Taco Luchador", "Mexican")
eighth_restaurant = Restaurant("Brasserie Provence", "French")

# initial list appends
approved.append(first_restaurant)
approved.append(second_restaurant)
approved.append(third_restaurant)
approved.append(fourth_restaurant)
approved.append(fifth_restaurant)
approved.append(sixth_restaurant)
approved.append(seventh_restaurant)
approved.append(eighth_restaurant)

# master loop
while show_menu:
    menu()
