import os

folder_path = os.path.join(os.getcwd(), 'folder')
file_size_dict = {}
type_file_100 = []
type_file_1000 = []
type_file_10000 = []
type_file_100000 = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        path_file = os.path.join(root, file)
        if os.stat(path_file).st_size <= 100:
            type_file_100 = []
            mask_file = os.path.join(root, file).split('.')[-1]
            if mask_file not in type_file_100:
                type_file_100.append(mask_file)
            if 100 not in file_size_dict.keys():
                file_size_dict.setdefault(100, (1, type_file_100))
            else:
                count = file_size_dict[100][0]
                count += 1
                file_size_dict[100] = (count, type_file_100)

        if 100 < os.stat(path_file).st_size <= 1000:
            mask_file = os.path.join(root, file).split('.')[-1]
            if mask_file not in type_file_1000:
                type_file_1000.append(mask_file)
            if 1000 not in file_size_dict.keys():
                file_size_dict.setdefault(1000, (1, type_file_1000))
            else:
                count = file_size_dict[1000][0]
                count += 1
                file_size_dict[1000] = (count, type_file_1000)

        if 1000 < os.stat(path_file).st_size <= 10000:
            mask_file = os.path.join(root, file).split('.')[-1]
            if mask_file not in type_file_10000:
                type_file_10000.append(mask_file)
            if 10000 not in file_size_dict.keys():
                file_size_dict.setdefault(10000, (1, type_file_10000))
            else:
                count = file_size_dict[10000][0]
                count += 1
                file_size_dict[10000] = (count, type_file_10000)

        if 10000 < os.stat(path_file).st_size <= 100000:
            mask_file = os.path.join(root, file).split('.')[-1]
            if mask_file not in type_file_100000:
                type_file_100000.append(mask_file)
            if 100000 not in file_size_dict.keys():
                file_size_dict.setdefault(100000, (1, type_file_100000))
            else:
                count = file_size_dict[100000][0]
                count += 1
                file_size_dict[100000] = (count, type_file_100000)

for item in file_size_dict.items():
    print(item)


