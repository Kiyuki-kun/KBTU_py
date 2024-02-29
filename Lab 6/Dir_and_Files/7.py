def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            contents = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(contents)
        
        print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 6\Dir_and_Files\list.txt'

destination_file = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-\Lab 6\Dir_and_Files\copied.txt'

copy_file(source_file, destination_file)
