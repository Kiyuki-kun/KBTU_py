import re

def insert_spaces(string):
    modified_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return modified_string

file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt"
with open(file_path, 'r') as file:
    file_contents = file.read()

modified_contents = insert_spaces(file_contents)
print("Original contents:")
print(file_contents)
print("\nModified contents:")
print(modified_contents)
