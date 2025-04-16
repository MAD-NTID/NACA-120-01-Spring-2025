def sum_count_up(n, stop):
    print(f"sum count up currently at {n}")
    # base case
    if n == stop:
        return stop
    
    return n + sum_count_up(n + 1, stop)

def sum_simplified(n):
    print(f"sum simplified currently at {n}")
    # base case
    if n == 1:
        return 1
    
    return n + sum_simplified(n - 1)

def sum(total, counter):
    print(f"sum total currently at {total}")
    # base case
    if counter == 1:
        return total

    return sum(total + counter, counter - 1)

def sum_loops(counter):
    total = 0
    for i in range(1, counter + 1):
        print(f"sum loops currently at {total}")
        total += i

    return total

print(sum_count_up(1, 10))
print()

print(sum_simplified(10))
print()

print(sum(1, 10))
print()

print(sum_loops(10))
print()