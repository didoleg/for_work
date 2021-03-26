import re, os


file_list = os.listdir()

phone_num_regex = re.compile(r'\d{4}_\d{2}-\d{2}=\d{2}-\d{2}-\d{2}')

for file_name in file_list:
    if phone_num_regex.search(file_name) is not None:
        new_file_name = f'_{file_name[16:18]}_{file_name[13:15]}_{file_name[8:12]}-{file_name[19:21]}.{file_name[22:24]}.{file_name[25:27]}.avi'
        os.rename(file_name, new_file_name)




