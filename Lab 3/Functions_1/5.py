from itertools import permutations

def print_permutations(input_str):
    print("All permutations of the string:")
    for permuted_string in permutations(input_str):
        print(''.join(permuted_string))

user_input = input("Enter a string: ")
print_permutations(user_input)
