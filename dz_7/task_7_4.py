import os

folder_path = os.path.join(os.getcwd(), 'folder')
file_size_dict = {}

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path_file = os.path.join(root, file)
        if os.stat(path_file).st_size <= 100:
            if 100 not in file_size_dict.keys():
                file_size_dict.setdefault(100, 1)
            else:
                file_size_dict[100] += 1
        if 100 < os.stat(path_file).st_size <= 1000:
            if 1000 not in file_size_dict.keys():
                file_size_dict.setdefault(1000, 1)
            else:
                file_size_dict[1000] += 1
        if 1000 < os.stat(path_file).st_size <= 10000:
            if 10000 not in file_size_dict.keys():
                file_size_dict.setdefault(10000, 1)
            else:
                file_size_dict[10000] += 1
        if 10000 < os.stat(path_file).st_size <= 100000:
            if 100000 not in file_size_dict.keys():
                file_size_dict.setdefault(100000, 1)
            else:
                file_size_dict[100000] += 1

print(file_size_dict)



