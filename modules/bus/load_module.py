import os
import time
import colorama
import sys
from colorama import Fore
if len(sys.argv) < 3:
    exit()


module = sys.argv[1]
send = sys.argv[2]
try:
    if os.path.exists("/usr/share/usbsploit/data"):
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' DATA path does not exists, exiting...')
        sys.exit()
except:
    pass

try:
    if os.path.exists('/usr/share/usbsploit/'+module):
        os.system('python3 /usr/share/usbsploit/data/'+module+' '+send+' '+module)
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' There was error while loading module: "'+send+'"')
except:
    pass
sys.exit()