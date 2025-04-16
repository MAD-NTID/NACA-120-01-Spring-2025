def recursion(n = 1):
    print(f"n is {n}")
    return recursion(n + 1)

# invoke the recursion function
recursion(1)