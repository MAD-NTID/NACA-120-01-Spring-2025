import stack

CHIP = "chip"
counts = 100

for chip in range(counts):
    stack.push(f"{CHIP} - {chip + 1}")

print(f"Pringles container has {stack.size()}")
print(f"Pringles contains is empty? {stack.empty()}")
print(f"Top of pringles is chip {stack.top()}")
print()

# Pop the top pringle chip
print(f"Popped: {stack.pop()}")
print(f"Popped: {stack.pop()}")
print()

print(f"Pringles container has {stack.size()}")
print(f"Pringles contains is empty? {stack.empty()}")
print(f"Top of pringles is chip {stack.top()}")
print()

print("Let's eat it all up!")

for chip in range(stack.size()):
    print(f"I just ate {stack.pop()}")
print()

print(f"Pringles container has {stack.size()}")
print(f"Pringles contains is empty? {stack.empty()}")
print(f"Top of pringles is chip {stack.top()}")
print()