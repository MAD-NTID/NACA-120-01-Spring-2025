def print_menu():
    print("1. Add Pet")
    print("2. Remove Pet")
    print("3. List All Pets")
    print("4. List Specific Pet")
    print("5. List All Data")
    print("6. Exit")


def select_menu():
    while True:
        try:
            option = int(input("Select an Option (1-6): "))

            if option >= 1 and option <= 6:
                return option
            else:
                print("Invalid Option, Select from 1 - 6")
        except:
            print("Your input is not a number from 1 - 6")


def main(pets):
    while True:
        print_menu()

        option = select_menu()

        # Add a Pet - Prompt user for pet type, pet name, pet age, pet patient number
        # Collect Pet information and add to the dictionary
        if option == 1:
            pet_type = input("Enter Pet Type: ")
            pet_name = input("Enter Pet Name: ")
            pet_age = int(input("Enter Pet Age: "))
            pet_patient_number = input("Enter Pet Patient Number (abc1234): ")
            
            if pet_patient_number in pets:
                print("Pet Patient Number is already used. Enter a different pet patient number")
                print()
                continue

            # this creates a tuple
            # pets[pet_patient_number] = (pet_type, pet_name, pet_age)
            pets[pet_patient_number] = {
                "pet_type": pet_type,
                "pet_name": pet_name,
                "pet_age": pet_age
            }

            print(f"Pet {pet_name} was added to the system")

        # Remove a Pet - Prompt user for pet patient number
        # Collect Pet information and remove from the dictionary
        elif option == 2:
            pet_patient_number = input("Enter Pet Patient Number to Remove: ")

            # this retrieves a tuple
            pet_removed = pets.pop(pet_patient_number)

            # print(f"Pet {pet_removed[1]} was removed from the system")
            print(f"Pet {pet_removed.get('pet_name')} was removed from the system")
            
        # Iterate each pet and print its details
        elif option == 3:
            for key, value in pets.items():
                print(f"{key} - {value}")

        # List a Pet - Prompt user for pet patient number
        # Collect Pet information and print pet details from the dictionary
        elif option == 4:
            pet_patient_number = input("Enter Pet Patient Number to Show: ")
            pet = pets.get(pet_patient_number)
            print(pet)

        # List All Data in Dictionary
        elif option == 5:
            print(pets)

        else:
            print("Thank you for using our Pet Management System")
            break

        # add spacing per each loop
        print()

pets = {
    "abc1234": {
        "pet_type": "Dog",
        "pet_name": "Floffy",
        "pet_age": 5
    },

    "abc1235": {
        "pet_type": "Bird",
        "pet_name": "Tweety",
        "pet_age": 3
    }
}
main(pets)