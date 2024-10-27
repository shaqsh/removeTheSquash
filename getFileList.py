import os

input_dir = 'input'
file_list = os.listdir(input_dir)

for file in file_list:
    print(f'File: {file}')