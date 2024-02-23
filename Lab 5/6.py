import re

def replace_with_colon(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt"
with open(file_path, 'r') as file:
    file_contents = file.read()

replaced_contents = replace_with_colon(file_contents)
print("Original contents:")
print(file_contents)
print("\nContents with replaced characters:")
print(replaced_contents)

