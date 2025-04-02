def AddTask(tasks):
    task = input("Enter a new task")
    tasks.append(task)

    return tasks


def CompleteTask(tasks):
    completed_task = tasks.pop()

    print("Completed task", completed_task)

    return tasks


def main():
    tasks = []

    while(True):
        print("What would you like to do?")
        choice = input("1. Add Todo\n2. Complete Todo\n3. Next Task\n4. Exit\n\nEnter Choice: ")

        if choice == "1":
            tasks = AddTask(tasks)

        elif choice == "2":
            tasks = CompleteTask(tasks)

        elif choice == "3" and len(tasks) > 0:
            # this will give you the last item in the list
            print("Next task is", tasks[len(tasks) - 1])

        elif choice == "4":
            print("Thank you for using our app")
            break

        else:
            print("Invalid Choice")


main()