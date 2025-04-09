import custom_queue

PEOPLE = "Person"
count = 10

for i in range(count):
    custom_queue.enqueue(f"{PEOPLE} - {i + 1}")

print(f"Clinic Line has {custom_queue.size()}")
print(f"Clinic Line is empty? {custom_queue.empty()}")
print(f"Front of the line is person {custom_queue.peek()}")
print()

# Person 1 gets processed
person_1 = custom_queue.dequeue()
print(f"{person_1} has been processed")
print(f"Next person in line is {custom_queue.peek()}")
print()

for i in range(custom_queue.size()):
    person_processed = custom_queue.dequeue()

    print(f"{person_processed} has been processed")

print(f"Clinic Line has {custom_queue.size()}")
print(f"Clinic Line is empty? {custom_queue.empty()}")
print(f"Front of the line is person {custom_queue.peek()}")
print()