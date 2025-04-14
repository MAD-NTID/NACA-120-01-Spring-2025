TODO_STATUS = "todo"
COMPLETE_STATUS = "completed"


def complete_task(task_name):
    # Get the task from the task list
    task = get_task(task_name)

    # Task is not None means we found the task by name
    if task is not None:
        # Update the task by creating a new tuple
        # with the same task name, but completed status
        task_complete = (task_name, COMPLETE_STATUS)

        # Update the task in the task list with the new
        # completed task and return true 
        task_list_index = get_task_index(task_name)
        task_list[task_list_index] = task_complete


def add_task(task_name, status=TODO_STATUS):
    # append accepts 1 value, so make it a tuple
    task_list.append(
        (task_name, status)
    )


def get_task(task_name):
    for task in task_list:
        # we know that a task is a tuple and we want to compare the task name
        # and then return it
        if task[0] == task_name:
            return task
    
    return None


def get_task_index(task_name):
    for index in range(len(task_list)):
        if task_list[index][0] == task_name:
            return index

    # this is for not found
    return -1


def size():
    return len(task_list)

task_list = []