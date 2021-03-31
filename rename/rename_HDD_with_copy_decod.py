import os, re, subprocess, shlex


file_list = os.listdir()
search_file = re.compile(r'\d{4}_\d{2}-\d{2}=\d{2}-\d{2}-\d{2}')

for file in file_list:
    if search_file.search(file) is not None:
        folder_path = os.path.join(os.getcwd(), f'{file[0:5]}\\{file[13:15]}\\{file[16:18]}')
        if not os.path.exists(f'{folder_path}'):
            os.makedirs(f'{folder_path}')

        new_file = f'_{file[16:18]}_{file[13:15]}_{file[8:12]}-{file[19:21]}.{file[22:24]}.{file[25:27]}.avi'
        tree_folder = os.listdir(f'{folder_path}')

        if new_file not in tree_folder and os.path.getsize(file) > 1300000000:
            cmd = f'ffmpeg -i {file} {new_file}'
            args = shlex.split(cmd)
            convert = subprocess.Popen(args, stdout=subprocess.PIPE)
            subprocess.Popen.wait(convert)
            os.replace(new_file, f'{folder_path}/{new_file}')
            os.remove(file)

        elif new_file in tree_folder and os.path.getsize(file) > 1300000000:
            new_file_name = f'_{file[16:18]}_{file[13:15]}_{file[8:12]}-{file[19:21]}.{file[22:24]}.{file[25:27]}_({str(len(tree_folder))}).avi '
            cmd = f'ffmpeg -i {file} {new_file_name}'
            args = shlex.split(cmd)
            convert = subprocess.Popen(args, stdout=subprocess.PIPE)
            subprocess.Popen.wait(convert)
            os.replace(new_file_name, f'{folder_path}/{new_file_name}')
            os.remove(file)

        elif new_file not in tree_folder:
            os.replace(new_file, f'{folder_path}/{new_file}')
            os.remove(file)

        elif new_file in tree_folder:
            new_file_name = f'_{file[16:18]}_{file[13:15]}_{file[8:12]}-{file[19:21]}.{file[22:24]}.{file[25:27]}_({str(len(tree_folder))}).avi '
            os.replace(file, f'{folder_path}/{new_file_name}')



