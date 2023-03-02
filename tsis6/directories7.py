def copy_file(src_file, dest_file):
    with open(src_file, 'r') as f1, open(dest_file, 'w') as f2:
        contents = f1.read()
        f2.write(contents)

# Example usage
src_file = "example.txt"
dest_file = "copy.txt"
copy_file(src_file, dest_file)
print("Contents of", src_file, "copied to", dest_file)