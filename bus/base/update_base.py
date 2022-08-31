import os
import time
import sys
from subprocess import getoutput
import random
import colorama
from colorama import Fore
path = "/usr/share/usbsploit"
update_path = "/usr/share/usbsploit-update"
mk = "/usr/share/usbsploit/src/bus.sh"
url = "https://github.com/G00Dway/USBSploit"
add = ""
try:
    if os.path.exists(update_path):
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Update path does not exists, database is corrupted, exiting...')
        sys.exit()
except:
    pass

while True:
    name = random.randint(1, 100000)
    get = os.listdir(update_path)
    add = "usbsploit_OLD"+str(name)
    if add in get:
        continue
    else:
        os.mkdir(update_path+'/'+add)
        break
try:
    copy = getoutput(f'mv {path} {update_path}/{add}')
    try:
        clone = getoutput(f'git clone {url} {path}')
        load = getoutput(f'python3 {path}/bus/base/rename.py')
        sys.exit()
    except:
        pass
except:
    pass