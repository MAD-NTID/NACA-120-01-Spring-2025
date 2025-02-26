def sum(num1, num2):
    return num1 + num2

# getinputnum1 - hard to read
# get_input_num_1 - eary to read
def get_input_num_1():
    return int (input("Enter Num 1: "))

def get_input_num_2():
    return int (input("Enter Num 2: "))

print("Hello, enter two numbers to add\n")
num1 = get_input_num_1()
num2 = get_input_num_2()

result = sum(num1, num2)

print("The result of num1", num1, "plus num2", num2, "is", result)