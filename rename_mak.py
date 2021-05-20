import os
import re

file_list = os.listdir()
print(file_list)

RE_NAME = re.compile(r'(\d{4}).(\d{2}).(\d{2})-(\d{2}).(\d{2}).(\d{2})')

for file_name in file_list:
    if RE_NAME.search(file_name) is not None:
        date_time = RE_NAME.search(file_name)
        new_file_name = f'_{date_time.group(3)}_{date_time.group(2)}_{date_time.group(1)}-{date_time.group(4)}.{date_time.group(5)}.{date_time.group(6)}.avi'
        print(new_file_name)
        os.rename(file_name, new_file_name)





