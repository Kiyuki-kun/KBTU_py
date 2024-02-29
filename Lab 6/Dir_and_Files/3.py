import os

def analyze_path(given_path):
    if os.path.exists(given_path):
        print(f"The given path '{given_path}' exists.")
        directory, filename = os.path.split(given_path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The given path '{given_path}' does not exist.")

given_path = input("Enter a path from File Explorer:")

analyze_path(given_path)
