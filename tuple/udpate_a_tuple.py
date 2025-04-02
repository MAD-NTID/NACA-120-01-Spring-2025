# how to update a tuple
def main():
    tuple = ("hello world", "original", 5)
    print(f"Original Tuple Value: {tuple}")

    # you can keep the original values and modify the one you need
    tuple = (tuple[0], "modified", tuple[2])
    print(f"Modified Tuple Value: {tuple}")


main()