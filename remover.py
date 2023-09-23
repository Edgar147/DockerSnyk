import os

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

def remove_files(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            if count_lines(file_path) < 5:
                os.remove(file_path)
                print(f"Supprimé {file_path}")


directory = "results"
remove_files(directory)

