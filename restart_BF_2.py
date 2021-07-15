import subprocess
import time

cmd = 'taskkill /f /im Butterfly.Shell.exe'
process_cmd = subprocess.Popen(cmd)

time.sleep(5)

start_prog = 'C:\Program Files (x86)\YSF\Butterfly-All\Butterfly.Shell.exe'
process_prog = subprocess.Popen(start_prog)
