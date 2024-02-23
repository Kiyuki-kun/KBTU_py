import re

def camel_to_snake(text):    
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
    
file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt"
with open(file_path, 'r') as file:
    file_contents = file.read()

snake_case_contents = camel_to_snake(file_contents)
print("Original contents:")
print(file_contents)
print("\nSnake case contents:")
print(snake_case_contents)
