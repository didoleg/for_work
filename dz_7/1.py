import os

folder_path = os.path.join(os.getcwd(), 'folder')
file_size_dict = {}
all_files_size = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path_file = os.path.join(root, file)
        all_files_size.append(os.stat(path_file).st_size)

    key_size_max = max(all_files_size)

for file_size in range(len(str(key_size_max))):
    key_size = 100 * 10 ** file_size
    file_size_dict.setdefault(key_size, 0)

for file in all_files_size:
    file_size_dict[10 * 10 ** len(str(file))] += 1

print(file_size_dict)

