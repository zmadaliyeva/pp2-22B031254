import os


def check_path(path):
    if os.path.exists(path):
        print("Path exists!")
        dir_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        print("Directory portion of path:", dir_name)
        print("Filename portion of path:", file_name)
    else:
        print("Path does not exist!")

# Example usage
path = "/path/to/file.txt"
check_path(path)