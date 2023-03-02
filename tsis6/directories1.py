import os


def list_directories(path):
  
    directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return directories

def list_files(path):
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    
    all_items = os.listdir(path)
    return all_items

# Example usage
path = '/path/to/folder'
directories = list_directories(path)
files = list_files(path)
all_items = list_all(path)

print("Directories:")
print(directories)

print("Files:")
print(files)

print("All items:")
print(all_items)