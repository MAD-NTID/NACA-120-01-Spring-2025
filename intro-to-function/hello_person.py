# functions should be declared at the top level first
def greet(i_can_name_this_whatever):
    print("Hello, your name is", i_can_name_this_whatever)

person_name = input("Enter your name? ")

greet(person_name)