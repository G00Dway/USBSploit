import os
import time
import subprocess
import sys
import colorama
from colorama import Fore
from subprocess import getoutput
path = "/usr/share/usbsploit"
exec = ['chmod +x /usr/share/usbsploit/bin/consoleusb/usbconsole',
'chmod +x /usr/share/usbsploit/bin/consoleusb/usbcc',
'cp -r /usr/share/usbsploit/bin/consoleusb/usbconsole /usr/bin',
'cp -r /usr/share/usbsploit/bin/consoleusb/usbcc /usr/bin']
driver = "/usr/share/usbsploit-drivers"

clean = ['rm -rf /usr/share/usbsploit/setup-usbsploit.sh',
'rm -rf /usr/share/usbsploit/uninstall-usbsploit.sh',
'rm -rf /usr/share/usbsploit/README.md',
'rm -rf /usr/share/usbsploit/LICENSE']
os.system(f'rm -rf {driver}')
os.system('rm -rf /usr/bin/usbconsole')
os.system('rm -rf /usr/bin/usbcc')
for i in exec:
    os.system(i)
os.system('mkdir /usr/share/usbsploit-drivers')
os.system(f'python3 {path}/usb/install/driver_install.py')
os.system('mkdir /usr/share/usbsploit-drivers/DRIVERS')
os.system('python3 /usr/share/usbsploit/usb/opt/load_driver.py')
copy = getoutput(f'bash {path}/src/bus.sh &>> mkdir.log')
os.system('python3 /usr/share/usbsploit/modules/bus/update_modules.py')
for i in clean:
    os.system(i)
try:
    with open(path+'/VERSION.txt', 'r') as v:
        version = v.read()
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Successfully updated to version: '+version)
except:
    pass
print(Fore.MAGENTA+'[!]'+Fore.RESET+' Please restart framework to setup updated changes!')
sys.exit()