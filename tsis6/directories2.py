import os


def check_access(path):
    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"

    # Check if path is readable
    if not os.access(path, os.R_OK):
        return "Path is not readable"

    # Check if path is writable
    if not os.access(path, os.W_OK):
        return "Path is not writable"

    # Check if path is executable
    if not os.access(path, os.X_OK):
        return "Path is not executable"

    return "Path is accessible"

# Example usage
path = "/path/to/folder"
result = check_access(path)

print(result)