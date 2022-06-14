import os
import time
import colorama
from colorama import Fore
import sys
from subprocess import getoutput

try:
    pull = getoutput('cd /usr/share/usbsploit && git pull')
    if "Failed" in pull or "failed" in pull:
        print(Fore.RED+'[-]'+Fore.RESET+' Failed to update using GIT...')
        print(Fore.BLUE+'[i]'+Fore.RESET+' Updating using "GIT CLONE"...')
        os.system('python3 /usr/share/usbsploit/bus/base/update_base.py')
    else:
        with open("/usr/share/usbsploit/VERSION.txt", "r") as v:
            version = v.read()
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Successfully Updated to version: '+version)
        print(Fore.MAGENTA+'[!]'+Fore.RESET+' Please restart framework to setup updated changes!')
except:
    pass

sys.exit()