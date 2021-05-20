import subprocess
import time


current_time = time.strftime('%H:%M:%S', time.localtime())

if '01:00:00' < current_time < '15:00:00':
    print(current_time)

else:
    cmd = 'taskkill /f /im Butterfly.Shell.exe'
    process_cmd = subprocess.Popen(cmd)

    time.sleep(3)

    start_prog = 'C:\Program Files (x86)\YSF\Butterfly-All\Butterfly.Shell.exe'
    process_prog = subprocess.Popen(start_prog)





