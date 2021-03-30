import re, os

file_list = os.listdir()
search_file = re.compile(r'\d{4}_\d{2}-\d{2}=\d{2}-\d{2}-\d{2}')

for file_name in file_list:
    if search_file.search(file_name) is not None:

        folder_path = os.path.join(os.getcwd(), f'{file_name[0:5]}\\{file_name[13:15]}\\{file_name[16:18]}')
        if not os.path.exists(f'{folder_path}'):
            os.makedirs(f'{folder_path}')

        new_file_name = f'_{file_name[16:18]}_{file_name[13:15]}_{file_name[8:12]}-{file_name[19:21]}.{file_name[22:24]}.{file_name[25:27]}.avi'
        os.rename(file_name, new_file_name)
        os.replace(new_file_name, f'{folder_path}/{new_file_name}')

