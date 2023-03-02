def count_lines(filename):
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            count += 1
        return count

# Example usage
filename = "example.txt"
line_count = count_lines(filename)
print("Number of lines in", filename, "is", line_count)