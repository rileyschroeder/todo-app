FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Returns the contents of .txt file as a list."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a todo item list in the .txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())