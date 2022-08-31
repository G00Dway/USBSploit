import os
import time
import colorama
import usb
from usb import *
import pycparser
import re
import sys
from colorama import Fore
import subprocess
from subprocess import getoutput
from subprocess import check_output
info = ""
dev = ""
if len(sys.argv) < 2:
    pass
else:
    info = str(sys.argv[1])
    dev = str(sys.argv[1])
popular = ['autoconf.inf', 'autorun.inf', 'setup.exe', 'server.exe', 'BOOT', 'SERVER', 'SOURCE', 'MAIN', 'system.bat']
file_types = ['.exe', '.py', '.bat', '.vbs', '.inf', '.cpp', '.iso', '.jar', '.xml', '.html', '.sh', 'txt']
# busses = usb.busses()
device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
try:
    df = subprocess.check_output("lsusb")
except Exception as e:
    print(Fore.RED+'[-]'+Fore.RESET+' Error while scanning for USB devices: '+str(e))
    sys.exit()
devices = []
for i in df.split(b'\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
            

if devices == [] or devices == ['\n']:
    print(Fore.RED+'[-]'+Fore.RESET+' FATAL: No USB devices found!')
    sys.exit()


def more(name):
    print(Fore.BLUE+'[i]'+Fore.RESET+' Retrieving information about: '+name)
    time.sleep(0.5)
    print(Fore.BLUE+'[i]'+Fore.RESET+' Trying to unmount the device...')
    unmount = getoutput('umount '+name)
    if "Failed" in unmount or "failed" in unmount:
        print(Fore.RED+'[-]'+Fore.RESET+' Failed to unmount device, please check if the device works properly')
        sys.exit()
    time.sleep(0.7)
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Unmount success')
    print(Fore.BLUE+'[i]'+Fore.RESET+' Mounting to /devices/USB...')
    time.sleep(0.6)
    mount = getoutput('mount '+name+' /usr/share/usbsploit/devices/USB')
    if "Failed" in mount or "failed" in mount:
        print(Fore.RED+'[-]'+Fore.RESET+' Failed to mount device, please check if the device works properly')
        sys.exit()
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Successfully mounted device to /devices/USB')
    time.sleep(1)
    print(Fore.BLUE+'[i]'+Fore.RESET+' Gathering amount of all files in the device...')
    files = os.listdir("/usr/share/usbsploit/devices/USB")
    amount = 0
    dirs = 0
    for n in files:
        if os.path.isdir("/usr/share/usbsploit/devices/USB/"+n):
            dirs += 1
        else:
            amount += 1
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Amount of files in the device: '+amount)
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Amount of directories in the device: '+dirs)
    print(Fore.BLUE+'[i]'+Fore.RESET+' Checking file names...')
    dir = "/usr/share/usbsploit/devices/USB"
    check = os.listdir(dir)
    for get in popular:
        if get in check:
            print(Fore.BLUE+'[i]'+Fore.RESET+f' Found "{get}" folder/file in the device')
    for type in file_types:
        if type in check:
            print(Fore.BLUE+'[i]'+Fore.RESET+f' Found "{type}" file(s) in the device')
    list_file = 0
    get = os.listdir(dir)
    for file in get:
        list_file += 1
        sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+' Listing files/folders in the device: '+list_file)
        time.sleep(0.1)
    for show in get:
        if os.path.isdir(dir+'/'+get):
            print(Fore.BLUE+'[i]'+Fore.RESET+' Folder: "'+get+'"')
        else:
            print(Fore.BLUE+'[i]'+Fore.RESET+' File: "'+get+'"')
        time.sleep(0.1)
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Done.')
    
    


types = ['sda', 'sdb', 'sde', 'tty']
if "/dev" in dev:
    for typ in types:
        if typ in dev:
            more(dev)
            sys.exit()
    

if info == "":
    for name in devices:
        if 'tag' in name.keys():
            device_id = name['device'].split("/dev/bus/usb/")
            device_id = device_id.split("/")
            print(Fore.BLUE+'[i]'+Fore.RESET+' Found device: '+name['tag'], '- with bus (path) ID: '+device_id[1])
        else:
            if 'device' in name.keys():
                print(Fore.RED+'[-]'+Fore.RESET+' Unable to detect USB device name, printing bus (path) ID instead: '+name['device'])
        time.sleep(0.3)
else:
    print(Fore.BLUE+'[i]'+Fore.RESET+' Searching/Scanning all devices with name '+info+'...')
    time.sleep(1)
    detect_usb = False
    for detect in devices:
        if info in detect['tag'] or info in detect['device']:
            detect_usb = True
            device_id = detect['device'].split("/dev/bus/usb/")
            device_id = device_id.split("/")
            print(Fore.YELLOW+'[+]'+Fore.RESET+' USB device name: '+detect['tag'])
            print(Fore.YELLOW+'[+]'+Fore.RESET+' USB device ID: '+detect['id'])
            print(Fore.YELLOW+'[+]'+Fore.RESET+' USB device bus (path) ID: '+detect['device'])
            print(Fore.YELLOW+'[+]'+Fore.RESET+' USB device internal bus (path) ID: '+device_id[0], '-', device_id[1])
            print('---------------------------------------------')
        else:
            detect_usb = False
    if detect_usb == False:
        print(Fore.RED+'[-]'+Fore.RESET+' No such device: '+info+'...')
        

sys.exit()
