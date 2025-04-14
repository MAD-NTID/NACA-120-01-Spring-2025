import todo_list

def test_get_tasks_size():
    todo_list.add_task("new task", "todo")

    actual = todo_list.size()

    expected_size = 1

    assert actual == expected_size


def test_add_task():
    # we add to the task list by sending two values
    todo_list.add_task("my new task")

    # retrieve the task
    actual = todo_list.get_task("my new task")

    # we expecte tuple from the todo_list
    expected_tuple = ("my new task", "todo")

    assert actual == expected_tuple


def test_get_task():
    actual = todo_list.get_task("some task that doesn't exist")

    expected_none = None

    assert actual == expected_none


def test_complete_task():
    # we add to the task list by sending two values
    todo_list.add_task("my new task")

    actual_task_status = todo_list.get_task("my new task")
    expected_task_status = todo_list.TODO_STATUS

    # 1st Sub Test - Status is "todo"
    assert actual_task_status[1] == expected_task_status

    todo_list.complete_task("my new task")

    actual_task_status = todo_list.get_task("my new task")
    expected_task_status = todo_list.COMPLETE_STATUS

    # 2nd Sub Test - Status is "complete"
    assert actual_task_status[1] == expected_task_status