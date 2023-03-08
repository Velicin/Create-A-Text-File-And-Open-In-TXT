import os

file_name = input("Enter the file name: ")

with open(file_name, 'w') as file:
    pass

os.system("notepad.exe " + file_name)
