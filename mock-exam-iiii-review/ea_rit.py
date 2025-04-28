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
def is_valid_date(date):
    regex = r'\d{2}-\d{2}-\d{4}'

    return re.match(regex, date) is not None

def create_sale():
    name_of_game = input("Enter the name of the game: ")
    platform_of_game = input("Enter the name of the platform: ")
    
    # while(True):
    #     date_of_sale = input("Enter the date of sale as MM-DD-YYYY: ")

    #     if is_valid_date(date_of_sale):
    #         break
    
    date_of_sale = ""
    while(not is_valid_date(date_of_sale)):
        date_of_sale = input("Enter the date of sale as MM-DD-YYYY: ")

    cost_of_game = input("Cost of the game: ")

    sale = {
        "name":name_of_game, 
        "platform":platform_of_game,
        "date":date_of_sale,
        "cost":cost_of_game
    }

    games_records.append(sale)

def remove_record():
    name_of_game = input("Enter the name of the game: ")
    platform_of_game = input("Enter the name of the platform: ")
    removed_game = None

    for i in range(len(games_records)):
        if name_of_game == games_records[i]["name"] and platform_of_game == games_records[i]["platform"]:
            removed_game = games_records.pop(i)
            break

    if removed_game is not None:
        print(f"Game '{removed_game}' was removed")
    else:
        print(f"Game '{name_of_game}' was not found")

def show_sales():
    if len(games_records) == 0:
        print("The list is currently empty")

    for record in games_records:
        print(record)

# Approach #1 - Using a filtered list
def filter_by_platform_rec(record_list, target, filtered_list):
    # stop recursion if length of list is 0
    if len(record_list) == 0:
        return filtered_list
    
    # check that the platform key's value matches the target or not
    if record_list[0]["platform"] == target:
        # copy the item from record list and append it to filtered list
        # because it matched the target
        filtered_list.append(record_list[0])

    # slice the record list from index position 1 and ahead
    # hence, cutting off index position 0 which we already checked for above
    record_list = record_list[1:]

    # finally, recur
    filter_by_platform_rec(record_list, target, filtered_list)

# Approach #2 - Using a filtered list and index
def filter_by_platform_with_index(target, filtered_list, index):
    # base
    if index >= len(games_records):
        return filtered_list
    
    if games_records[index]["platform"] == target:
        filtered_list.append(games_records[index])

    # finally, recur
    filter_by_platform_with_index(target, filtered_list, index + 1)

def filter_by_platform():
    target = input("Enter the target platform to filter by: ")
    
    filtered_rec = []
    filtered_index = []

    # Approach #1
    filter_by_platform_rec(games_records, target, filtered_rec)

    # Approach #2
    filter_by_platform_with_index(target, filtered_index, 0)

    if filtered_rec == filtered_index:
        print("Both Approach Worked")

    print("Filtered By Platform Recursion")
    print(filtered_rec)

    print()

    print("Filtered By Platform Index")
    print(filtered_index)

def main():
    while True:
        selected = menu_selection()

        if selected == 1:
            create_sale()
        elif selected == 2:
            remove_record()
        elif selected == 3:
            show_sales()
        elif selected == 4:
            filter_by_platform()
        else:
            print("Thank you for using our program")
            break

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\n\nUser Ended the program abruptly")