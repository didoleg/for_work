import os, re

file_list = os.listdir()
search_file = re.compile(r'\d{4}_\d{2}-\d{2}=\d{2}-\d{2}-\d{2}')

for file in file_list:
    if search_file.search(file) is not None:
        folder_path = os.path.join(os.getcwd(), f'{file[0:5]}\\{file[13:15]}\\{file[16:18]}')
        if not os.path.exists(f'{folder_path}'):
            os.makedirs(f'{folder_path}')

        new_file = f'_{file[16:18]}_{file[13:15]}_{file[8:12]}-{file[19:21]}.{file[22:24]}.{file[25:27]}.avi'
        tree_folder = os.listdir(f'{folder_path}')

        if new_file not in tree_folder:
            os.replace(file, f'{folder_path}/{new_file}')
        else:
            new_file_name = f'_{file[16:18]}_{file[13:15]}_{file[8:12]}-{file[19:21]}.{file[22:24]}.{file[25:27]}_({str(len(tree_folder))}).avi '
            os.replace(file, f'{folder_path}/{new_file_name}')


