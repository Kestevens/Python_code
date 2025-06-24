# file_path = "example.txt"
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print(f"File '{file_path}' not found")

# output_path = "output.txt"
# data_to_write = "This is the line we want to write"
# try:
#     with open(output_path, "w") as file:
#         file.write(data_to_write)
#     print(f"Data written to '{output_path}'")
# except Exception as e:
#     print("An exception occurred: ", e)
# append_path = "append.txt"
# data_to_append = "\nThis is an appended line"
# try:
#     with open(append_path, "a") as file:
#         file.write(data_to_append)
#     print(f"Data appended to '{append_path}")
# except Exception as e:
#     print("An exception happened: ", e)
# line_file_path = "lines.txt"
# try:
#     with open(line_file_path, "r") as file:
#         lines = file.readlines()
#     print("Lines from the file: ")
#     for line in lines:
#         print(line.strip())
# except FileNotFoundError:
#     print(f"File '{line_file_path}' not found")

explicit_file_path = "lines.txt"
file = open(explicit_file_path, "r")
content = file.read()
print(content)
file.close()
print("File closed")