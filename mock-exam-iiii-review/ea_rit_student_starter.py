import re

# Predefined variables
games_records = [] #this will keep a list of all game sales


# Predefined function
def display_menu():
    print("Menu Options:")
    print("1. Create a new sale")
    print("2. Remove a record")
    print("3. Show all sales")
    print("4. Filter sale by platform")
    print("5. Exit")


# Predefined function
def menu_selection():
    display_menu()
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            
            return choice
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# functions to be completed by the student goes here