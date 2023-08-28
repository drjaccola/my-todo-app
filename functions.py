FILEPATH = "todos.txt"


def get_todos(filename: object = FILEPATH) -> object:
    """ Read a text file and
    return a list of to-do items"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    """ Write the to-dos items in the text file."""
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
