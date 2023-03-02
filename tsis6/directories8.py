import os


def delete_file(path):
    if os.access(path, os.F_OK):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully")
        else:
            print("Permission denied to delete file")
    else:
        print("File not found")

# Example usage
path = "example.txt"
delete_file(path)