# Pop (remove) and return the element at position 0
def pop():
    if empty():
        return None
    
    return stack.pop(0)

# Get the Top element
def top():
    if empty():
        return None
    
    return stack[0]

# Push an element into the stack
def push(element):
    stack.insert(0, element)

# Check if the stack is empty or not
def empty():
    return size() <= 0

# Get Size
def size():
    return len(stack)

# Create a list to hold stack values
stack = []