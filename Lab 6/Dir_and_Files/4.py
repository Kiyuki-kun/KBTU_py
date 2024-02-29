def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

file_path = input("Enter a path from File Explorer:")

num_lines = count_lines(file_path)
if num_lines != -1:
    print(f"The file '{file_path}' contains {num_lines} lines.")
