cars = {}

cars["honda"] = {
    "model": "civic",
    "year": 1995
}

cars["kia"] = {
    "model": "elantra",
    "year": 2015
}

print("Showing All Keys in Cars")
print(cars.keys())

print("Show All Values in Cars")
print(cars.values())

# for car in cars:
#     print(f"Processing {car} - {cars[car]}")

for key, value in cars.items():
    print(f"Processing {key} - {value}")

print("Completed Processing Cars")
print()

if "honda" in cars:
    print("Yes, the honda exists")

# del cars["honda"]
car_brand_deleted = cars.pop("honda")
print(f"Car Brand: '{car_brand_deleted}' was deleted")

# try:
#     print(cars["toyota"])
# except KeyError:
#     print("Coult not find that car brand")

print(cars)