import os
import colorama
import getpass
from colorama import Fore
import sys
file = sys.argv[0]
current_path_2 = os.path.dirname(file)
colorama.init()
drivers_path = "/usr/share/usbsploit/usb/drivers"
user = os.environ["USER"]
user_via = getpass.getuser()

def copy():
    try:
        if os.path.exists("/usr/share/usbsploit") and os.path.exists("/usr/share/usbsploit-drivers"):
            pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' MAIN and DRIVERS Database path was not found! exiting...')
            exit()
    except:
        pass

    get_drv = os.listdir(drivers_path)
    for driver in get_drv:
        os.system('cp -r -v '+drivers_path+'/'+driver+' /usr/share/usbsploit-drivers &>> drv-copy.log')

copy()