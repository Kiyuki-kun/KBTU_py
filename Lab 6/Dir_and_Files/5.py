def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List has been successfully written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = ['apple', 'banana', 'orange', 'grape']

file_path = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 6\Dir_and_Files\list.txt'

write_list_to_file(file_path, my_list)
