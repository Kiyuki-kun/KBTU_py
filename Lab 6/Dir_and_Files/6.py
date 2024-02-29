import os
import string

def generate_files_in_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        for letter in string.ascii_uppercase:
            file_name = letter + ".txt"
            with open(os.path.join(folder_path, file_name), 'w') as file:
                file.write(f"This is file {file_name}.")
        print(f"Files have been successfully created in the folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 6\Dir_and_Files\A_to_Z files'

generate_files_in_folder(folder_path)
