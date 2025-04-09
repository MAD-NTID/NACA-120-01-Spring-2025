# Dequeue (remove) and return the element at position 0
def dequeue():
    if empty():
        return None
    
    return queue.pop(0)

# Get the front element
def peek():
    if empty():
        return None
    
    return queue[0]

# Enqueue an element into the queue
def enqueue(element):
    queue.append(element)

# Check if the queue is empty or not
def empty():
    return size() <= 0

# Get Size
def size():
    return len(queue)

# A variable to store the front
front = None
last = None

# Create a list to hold queue values
queue = []