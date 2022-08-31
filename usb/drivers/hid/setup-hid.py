import os
import sys
import colorama
from colorama import Fore
path = "/usr/share/usbsploit-drivers/DRIVERS/HID"
if len(sys.argv) < 2:
    pass
else:
    get = "start"




def load():
    pass








def install():
    try:
        os.mkdir(path)
        os.system(f'cp -r {__file__} {path}')
        os.system(f'cp -r /usr/share/usbsploit-drivers/hid/hid.py {path}')
    except Exception as e:
        print(e)
        exit()




try:
    if os.path.exists(path):
        os.system(f'rm -rf {path}')
        install()
    else:
        install()
except:
    pass


exit()