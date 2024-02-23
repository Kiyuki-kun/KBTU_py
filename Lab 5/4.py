import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

file_path = "C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt" 
with open(file_path, 'r') as file:
    file_contents = file.read()

sequences = find_sequences(file_contents)
print("Sequences found:")
for sequence in sequences:
    print(sequence)
