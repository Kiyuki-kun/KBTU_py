import os

def list_directories_and_files(path):
    directories = []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
    
    return directories, files

def list_all_directories_and_files(path):
    all_directories_files = []
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            all_directories_files.append(os.path.join(root, directory))
        for file in files:
            all_directories_files.append(os.path.join(root, file))
    
    return all_directories_files

specified_path = 'C:\D_Files\KBTU_coding\Python\PP2_2024-Serikbai-'

directories, files = list_directories_and_files(specified_path)
print("Directories:")
for directory in directories:
    print(directory)
print("\nFiles:")
for file in files:
    print(file)

all_directories_files = list_all_directories_and_files(specified_path)
print("\nAll Directories and Files:")
for item in all_directories_files:
    print(item)
