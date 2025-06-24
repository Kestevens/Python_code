import os
import subprocess

current_directory = os.getcwd()
# print("Current dir is: ", current_directory)

# dir_contents = os.listdir(current_directory)
# print("Directory contents: ", dir_contents)

#new_dir = "new_folder"
# os.mkdir(new_dir)
# print(f"Created folder: '{new_dir}'")

# new_name = "renamed_folder"
# os.rename(new_dir, new_name)
# print(f"Renamed  folder to: {new_name}")

# command = "dir"
# res = subprocess.run(command, shell=True, text=True, capture_output=True)
# print("Command output: ", res.stdout)

#print("PATH environment variables: ", os.environ.get("PATH"))

# file_path = os.path.join(current_directory, "same_file.txt")
# if os.path.exists(file_path):
#     print("File exists")
# else:
#     print("File does not exist")

def list_files_recursively(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(os.path.join(root, file))

list_files_recursively(current_directory)