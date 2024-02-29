import os

def check_access_and_delete(file_path):
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        if os.access(file_path, os.F_OK):
            print(f"The file '{file_path}' is accessible.")
            try:
                os.remove(file_path)
                print(f"The file '{file_path}' has been successfully deleted.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print(f"Error: The file '{file_path}' is not accessible.")
    else:
        print(f"Error: The file '{file_path}' does not exist.")

file_path = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 6\Dir_and_Files\copied.txt'

check_access_and_delete(file_path)
