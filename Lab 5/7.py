def snake_to_camel(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str

file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt"
with open(file_path, 'r') as file:
    file_contents = file.read()

replaced_contents = snake_to_camel(file_contents)
print("Snake case string:", file_contents)
print("Camel case string:", replaced_contents)
