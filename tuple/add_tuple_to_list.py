list = []

tuple_1 = ("some tuple", "some value", 5)
tuple_2 = ("another tuple", "some value", 10)

list.append(tuple_1)
list.append(tuple_2)

print(f"List Before: {list}")

temp_tuple = list[0]

list[0] = list[1]
list[1] = temp_tuple

print(f" List After: {list}")