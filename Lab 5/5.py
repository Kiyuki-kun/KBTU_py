import re

def match_pattern(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return True
    else:
        return False

test_strings = open('C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 5\sample.txt')
for test_string in test_strings:
    print(f"{test_string}: {match_pattern(test_string)}")
