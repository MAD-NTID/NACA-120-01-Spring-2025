def loop_start_end(start, ending):
    sum = 0
    for i in range(start, ending):
        print("Currently Printing", i)
        sum += i # sum = sum + i

    return sum

def main():
    start = int(input("Enter a Starting Value: "))
    ending = int(input("Enter an Ending Value: "))

    print("The sum is", loop_start_end(start, ending))

main()