import re

def split_at_uppercase(string):
    split_string = re.findall('[A-Z][^A-Z]*', string)
    return split_string

file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt" 
with open(file_path, 'r') as file:
    file_contents = file.read()

split_contents = split_at_uppercase(file_contents)
print("Original contents:")
print(file_contents)
print("\nSplit contents:")
for substring in split_contents:
    print(substring)
