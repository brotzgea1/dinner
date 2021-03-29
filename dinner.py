from os import system, name
from time import sleep
import random

show_menu = True
approved = []
filt = ""

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

def menu():
    # system('cls')
    print("Welcome to DinDin!")
    print("1. See what's for dinner!")
    print("2. Not in the mood for something? Let us know.")
    print("3. Add a restaurant from the list.")
    print("4. Delete a restaurant from the list.")
    print("5. Exit")
    selector = input("What would you like to do? Pick a number. ")
    if selector == "1":
        randomize()
        # sleep(3)
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
    filt_one = input("What are you not in the mood for? ")
    for item in approved:
        if item.cuisine == filt_one:
            filt = item
            return filt
            
def randomize():
    filt_approved = []
    for item in approved:
        if item.cuisine != filt:
            filt_approved.append(item)
    rando = random.choice(filt_approved)
    for item in filt_approved:
        if item == rando:
            print(item.name)
        else:
            continue
    
first_restaurant = Restaurant("ChiChi's", "Mexican")
second_restaurant = Restaurant("Taco Bell", "Mexican")
third_restaurant = Restaurant("McDonald's", "American")
fourth_restaurant = Restaurant("Burger King", "American")
fifth_restaurant = Restaurant("China Castle", "Chinese")
sixth_restaurant = Restaurant("Mussel Burger", "American")
seventh_restaurant = Restaurant("Taco Luchador", "Mexican")
eighth_restaurant = Restaurant("Brasserie Provence", "French")
approved.append(first_restaurant)
approved.append(second_restaurant)
approved.append(third_restaurant)
approved.append(fourth_restaurant)
approved.append(fifth_restaurant)
approved.append(sixth_restaurant)
approved.append(seventh_restaurant)
approved.append(eighth_restaurant)


while show_menu:
    menu()
