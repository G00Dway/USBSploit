import os
import subprocess
import colorama
from banners.banner import banner
import sys
from colorama import Fore
import pyparsing
import time
import random
import future
from subprocess import getoutput
Banner = banner()
modules = "/usr/share/usbsploit/modules"
console = ["usbconsole", "usbcc"]
connected = False
drivers = "/usr/share/usbsploit-drivers/DRIVERS"
update = "/usr/share/usbsploit-update"
update_install = "/usr/share/usbsploit/bus/base/update_framework.sh"
scan_usb = "/usr/share/usbsploit/usb/scanner/scan_usb.py"
root = "/root/.usbcc"
history = "on"
root_load = os.listdir(root)
for file in root_load:
    if file == 'logs' or file == 'options':
        continue
    os.system('rm -rf /root/.usbcc/'+file)
if os.path.exists(root+'/logs/history.log'):
    pass
else:
    os.system('touch '+root+'/logs/history.log')
if os.path.exists(root+'/options/history.options'):
    with open(root+'/options/history.options', 'r') as g:
        hs = g.readline()
    if hs == 'on':
        history = 'on'
    elif hs == 'off':
        history = 'off'
    else:
        history = 'on'
else:
    os.system('echo "on" > '+root+'/options/history.options')
load_modules = []
load_drivers = []
num = 0
module_nums_load = {}
driver_comment = []
loaded = 0
plugins_loaded = 0
try:
    if os.path.exists("/usr/share/usbsploit/VERSION.txt"):
        with open("/usr/share/usbsploit/VERSION.txt", "r") as v:
            version = v.readline()
    else:
        version = '???'
except:
    pass

modules_comment = []
load_all_modules = []
load_all_modules_name = []
driver_path = []
driver_run = []
drivers_desc_all = {}
modules_desc_all = {}
load_all_drivers = []
remove = ['.sh', '.py', '.pyc', '.pyh', '.pyw', '.rb', '.pl', '.yaml', '.json', '.xml', '.usbf', '.so', '.hid']
read = ['.txt', '.log', '.conf', '.ini']

try:
    mdl = os.listdir(modules)
    for module in mdl:
        for check in read:
            if check in module:
                continue
        if module == "bus":
            continue
        elif os.path.isfile(modules+'/'+module):
            for r in remove:
                if r in module:
                    loaded += 1
                    load_all_modules_name.append(module)
                    load_all_modules.append('modules/'+module)
                    m = module.replace(r, "")
                    load_modules.append('modules/'+m)
                    with open(modules+'/info.txt', 'r') as d:
                        desc = d.readline()
                    modules_desc_all[m] = desc
                    break
        else:
            inside = os.listdir(modules+'/'+module)
            for module_2 in inside:
                for check_2 in read:
                    if check_2 in module_2:
                        continue
                if module_2 == "bus":
                    continue
                for f in remove:
                    if f in module_2:
                        loaded += 1
                        load_all_modules_name.append(module_2)
                        load_all_modules.append('modules/'+module+'/'+module_2)
                        h = module_2.replace(f, "")
                        load_modules.append('modules/'+module+'/'+h)
                        with open(modules+'/'+module+'/info.txt', 'r') as d:
                            desc = d.readline()
                        modules_desc_all[h] = desc
                        break
except:
    pass

try:
    drv = os.listdir(drivers)
    for driver in drv:
        for drv_check in read:
            if drv_check in driver:
                continue
        if driver == "bus":
            continue
        elif driver == "UPDATE":
            continue
        elif "setup" in driver:
            continue
        elif os.path.isfile(drivers+'/'+driver):
            for g in remove:
                if g in driver:
                    load_all_drivers.append(driver)
                    driver_run.append(driver)
                    driver_path.append(driver)
                    j = driver.replace(g, "")
                    load_drivers.append(j)
                    with open(drivers+'/desc.txt', 'r') as d:
                        desc = d.readline()
                    drivers_desc_all[j] = desc
                    break
        else:
            path = os.listdir(drivers+'/'+driver)
            for driver_2 in path:
                for drv_check_2 in read:
                    if drv_check_2 in driver_2:
                        continue
                if driver_2 == "bus":
                    continue
                elif driver_2 == "UPDATE":
                    continue
                elif "setup" in driver_2:
                    continue
                for k in remove:
                    if k in driver_2:
                        load_all_drivers.append(driver_2)
                        driver_run.append(driver_2)
                        driver_path.append(driver+'/'+driver_2)
                        l = driver_2.replace(k, "")
                        load_drivers.append(l)
                        with open(drivers+'/'+driver+'/desc.txt', 'r') as d:
                            desc = d.readline()
                        drivers_desc_all[l] = desc
                        break
except:
    pass
try:
    num = 0
    for n in load_modules:
        num += 1
        module_nums_load[num] = n
except:
    pass
about = f'''
About USBSploit Framework
==================

Version      : {version}
Developed At : Azerbaijan, Baku
Developer    : {Fore.GREEN}G00Dway{Fore.RESET}
By Group     : {Fore.GREEN}Blest † Boyz{Fore.RESET}
Credits      : Fux
Members      : G00Dway, Fux, Nemesis, Rotasız, Dilax, Cyrus, Yakuza, Others...

Social Links
==================

Our Discord  : {Fore.GREEN}https://discord.gg/NE7REnjs2p{Fore.RESET}
FUX          : {Fore.GREEN}@torbacidiyorlar{Fore.RESET}
G00Dway      : {Fore.GREEN}https://github.com/G00Dway{Fore.RESET}
'''
drvrs = ''''''
list_cmd = '''
List Commands
==================

    command                 description
    -------                 -----------
    list modules            Show/List all usable and available modules
'''
show_cmd = '''
Module Command(s):
==================

    command                 description
    -------                 -----------
    show options            Show all available options for loaded module
'''

help_main = '''
Global Commands
=================

    command                 description
    -------                 -----------
    clear                   Clear terminal window
    back                    Go one input back

Main Commands
=================

    command                 description
    -------                 -----------
    help                    Show this help menu
    show <arg>              Show <arg> specified menu, type "show" for more options
    list <arg>              List <arg> available options-modules, type "list" for more options
    search <name>           Search specified module-text in loaded modules list
    use <module>            Use specified module
    info <module>           Get information about specified module
    about                   Show about the framework and its developers
    banner                  Show cool banners
    exit                    Quit framework

Module Commands
=================

    command                 description
    -------                 -----------
    set <option> <value>    Set the specified option to specified value
    show <arg>              Show <arg> specified menu, type "show" for more options
    start, run, execute     Load the selected module

Database Commands
=================

    command                 description
    -------                 -----------
    update                  Check for latest available updates and update
    clean                   Remove all old databases in "usbsploit-update" directory

USB Commands
=================

    command                 description
    -------                 -----------
    connect <dev>           Connect specified USB device "/dev/" to USBSploit Framework (Optional)
    sdshow                  Show all mounted disk/devices (blocks)
    format <mode> <dev>     Quick format the specified USB device, format modes: "NTFS, FAT"
    delete <dev>            Delete everything in device

Logs Commands
=================

    command                 description
    -------                 -----------
    history                 Show history
    history delete          Delete the history
    history off             Turn off the history
    history on              Turn on the history
    changelogs              Show changelogs, release versions

'''
def add():
    global help_main, drvrs
    log = '''
Drivers Installed
=================

    driver
    ------'''
    for desc in drivers_desc_all.keys():
        log += f'''
    {desc}'''
    help_main += log+'\n'
    drvrs += '\n'+log+'\n'


def show_banner():
    Banner.generate()
    print("+ -- ---={ "+Fore.YELLOW+"USBSploit Framework Version "+version+" "+Fore.RESET+"")
    print("- -- ---={ Modules loaded : "+str(loaded))
    print("- -- ---={ Plugins loaded : "+str(plugins_loaded))


def main():
    global num, connected, history
    try:
        usbf = input('\033[4musbf\033[0m > ').strip(" ").lower()
    except KeyboardInterrupt:
        print("")
        print(Fore.RED+'[-]'+Fore.RESET+' KeyboardInterrupt detected, force quitting...')
        sys.exit()
    usbf = usbf.split()
    while True:
        if usbf == []:
            pass
        elif usbf[0] == 'help':
            print(help_main)
        elif usbf[0] == 'clear':
            os.system('clear')
        elif usbf[0] == 'back':
            pass
        elif usbf[0] == 'exit' or usbf[0] == 'quit':
            if len(usbf) < 2:
                exit()
            else:
                try:
                    if usbf[1] == '-f':
                        print(Fore.RED+'[-]'+Fore.RESET+' Force quitting...')
                        try:
                            sys.exit()
                        except:
                            exit()
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized arg: '+usbf[1])
                        print(Fore.RED+'[-]'+Fore.RESET+' Quitting anyway...')
                        try:
                            exit()
                        except:
                            sys.exit()
                except:
                    pass
        elif usbf[0] == 'show':
            if len(usbf) < 2:
                print(show_cmd)
            else:
                try:
                    if usbf[1] == 'options':
                        print(Fore.RED+'[-]'+Fore.RESET+' No module loaded!')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized command: '+usbf[1])
                except:
                    pass
        elif usbf[0] == 'list':
            if len(usbf) < 2:
                print(list_cmd)
            else:
                try:
                    if usbf[1] == 'modules':
                        print('')
                        print("Available modules")
                        print('=================')
                        print('')
                        print('    name')
                        print('    ----')
                        num = 0
                        for mod in load_modules:
                            num += 1
                            print('    '+mod)
                        print('')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized command: '+usbf[1])
                except:
                    pass
        elif usbf[0] == 'search':
            if len(usbf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter what to search!')
            else:
                try:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Searching "'+usbf[1]+'"...')
                    found = 0
                    print('')
                    print("Found Modules")
                    print('=================')
                    print('')
                    print('    name')
                    print('    ----')
                    for get in load_modules:
                        if usbf[1] in get:
                            found += 1
                            print('    '+get)
                    print('')
                    if found == 0:
                        print('')
                        print(Fore.BLUE+'[i]'+Fore.RESET+' No modules found for: "'+usbf[1]+'"')
                except:
                    pass
        elif usbf[0] == 'use':
            if len(usbf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter a module name to use!')
            else:
                try:
                    if usbf[1] in load_modules:
                        if connected == False:
                            print(Fore.MAGENTA+'[!] WARN:'+Fore.RESET+' You have no USB device connected, so you will get in trouble, please connect one with command: "connect"!')
                        module_load = ""
                        hint = usbf[1].replace("modules/", "")
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Loading module "'+hint+'"...')
                        for rm in load_all_modules:
                            if usbf[1] in rm:
                                module_load = rm
                        os.system(f'python3 /usr/share/usbsploit/modules/bus/load_module.py {module_load} {usbf[1]}')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unknown module: '+usbf[1])
                except:
                    pass
        elif usbf[0] == 'info':
            if len(usbf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter a module name')
            else:
                try:
                    if usbf[1] in load_modules:
                        print(Fore.BLUE+f'MODULE  {Fore.RESET}: '+usbf[1])
                        print(Fore.BLUE+f'ABOUT   {Fore.RESET}: '+modules_desc_all[usbf[1]])
                        print('')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unknown module: '+usbf[1])
                except:
                    pass
        elif usbf[0] == 'about':
            print(about)
        elif usbf[0] == 'banner':
            show_banner()
        elif usbf[0] == 'clean':
            old = os.listdir(update)
            if old == [] or old == () or old == ['\n'] or old == ('\n') or old == False:
                print(Fore.YELLOW+'[+]'+Fore.RESET+' No old databases found, skipping...')
            for f in old:
                if "_" in f or "OLD" in f:
                    print(Fore.BLUE+'[i]'+Fore.RESET+' Removing all old databases...')
                    time.sleep(1) 
                    for pr in old:
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Removing database: '+pr)
                        time.sleep(0.3)
                        os.system('rm -rf '+update+'/'+pr)
            else:
                print(Fore.YELLOW+'[+]'+Fore.RESET+' No old databases found, skipping...')
        elif usbf[0] == 'update':
            os.system('bash '+update_install)
        # elif usbf[0] == 'scan':
        #     print(Fore.MAGENTA+'[!] WARN:'+Fore.RESET+' The "/dev/sdb-sda" path of the usb devices will NOT be shown, so in modules use you need to specify the path manually!')
        #     print(Fore.BLUE+'[i]'+Fore.RESET+' Scanning for connected USB devices...')
        #     time.sleep(1)
        #     os.system('python3 '+scan_usb)
        # elif usbf[0] == 'usb':
        #     def more_info(more_system):
        #         print(Fore.BLUE+'[i]'+Fore.RESET+' Device name: '+more_system)
        #         dev = input(Fore.CYAN+'[?]'+Fore.RESET+' Please enter the "/dev/sdb-sda" path of the device: ')
        #         time.sleep(1)
        #         if dev == '' or dev == ' ':
        #             print(Fore.RED+'[-]'+Fore.RESET+' Please enter a valid USB device!')
        #         elif '/dev' in dev:
        #             os.system('python3 '+scan_usb+f' {dev}')
        #         else:
        #             print(Fore.RED+'[-]'+Fore.RESET+' Please enter device path with "/dev"')
        #     def info(system):
        #         os.system('python3 '+scan_usb+f' {system}')
        #     if len(usbf) <= 3:
        #         if len(usbf) == 2:
        #             info(usbf[1])
        #         elif len(usbf) == 3:
        #             if usbf[1] == 'more':
        #                 more_info(usbf[2])
        #             else:
        #                 print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized command: '+usbf[1])
        #         else:
        #             print(Fore.RED+'[-]'+Fore.RESET+' Please enter USB name/path_id!')
        #     else:
        #         print(Fore.RED+'[-]'+Fore.RESET+' Please enter a valid command!')
        elif usbf[0] == 'sdshow':
            print(Fore.BLUE+'[i]'+Fore.RESET+' Listing devices...')
            time.sleep(0.4)
            fdisk = getoutput('lsblk -l')
            for line in fdisk.split('\n'):
                print(Fore.BLUE+'[i] '+Fore.RESET+str(line))
        elif usbf[0] == 'format':
            formats = ['ntfs', 'fat']
            if len(usbf) < 3:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter MODE to use in format and DEV path of the device!')
            else:
                try:
                    if usbf[1].lower() in formats:
                        if "/dev" in usbf[2]:
                            print(Fore.BLUE+'[i]'+Fore.RESET+' Unmounting device...')
                            rem = getoutput('umount '+usbf[2])
                            if "Failed" in rem or "No such" in rem or "failed" in rem:
                                print(Fore.RED+'[-]'+Fore.RESET+' Failed to unmount device')
                            else:
                                print(Fore.BLUE+'[i]'+Fore.RESET+' Formatting device "'+usbf[2]+'" (This might take long)...')
                                format = getoutput('mkfs -t '+usbf[1].lower()+f' -n "USB" {usbf[2]}')
                                if "Failed" in format or "No such" in format or "failed" in format or "mount" in format:
                                    print(Fore.RED+'[-]'+Fore.RESET+' Failed to format the device!')
                                else:
                                    print(Fore.YELLOW+'[+]'+Fore.RESET+' Successfully formatted the device to "'+usbf[1]+'"')
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Please enter a valid USB device "/dev" path!')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please enter a valid format mode!')
                except:
                    pass
        elif usbf[0] == 'delete':
            if len(usbf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter DEV path of the device!')
            else:
                try:
                    if "/dev" in usbf[1]:
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Unmounting device...')
                        rem = getoutput('umount '+usbf[1])
                        if "Failed" in rem or "No such" in rem or "failed" in rem:
                            print(Fore.RED+'[-]'+Fore.RESET+' Failed to unmount device')
                        else:
                            print(Fore.BLUE+'[i]'+Fore.RESET+' Mounting device to /devices/USB...')
                            mount = getoutput('mount '+usbf[1]+' /usr/share/usbsploit/devices/USB')
                            if "Failed" in mount or "No such" in mount or "failed" in mount:
                                print(Fore.RED+'[-]'+Fore.RESET+' Failed to mount device')
                            else:
                                print(Fore.BLUE+'[i]'+Fore.RESET+' Removing everything in the device...')
                                delete = os.listdir("/usr/share/usbsploit/devices/USB")
                                for name in delete:
                                    remove = getoutput('rm -rf /usr/share/usbsploit/devices/USB/'+name)
                                    if "Failed" in remove or "No such" in remove or "failed" in remove:
                                        print(Fore.RED+'[-]'+Fore.RESET+' Failed to remove: "'+name+'", passing...')
                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Done.')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please enter a valid DEV path of the device!')
                except:
                    pass

        # elif usbf[0] == 'driver':
        #     if len(usbf) < 2:
        #         print(Fore.RED+'[-]'+Fore.RESET+' Please enter driver name!')
        #     else:
        #         try:
        #             if usbf[1] in load_drivers:
        #                 print(Fore.BLUE+f'DRIVER   {Fore.RESET}: '+usbf[1])
        #                 print(Fore.BLUE+f'ABOUT    {Fore.RESET}: '+drivers_desc_all[usbf[1]])
        #                 print('')
        #             else:
        #                 print(Fore.RED+'[-]'+Fore.RESET+' No such driver: '+usbf[1])
        #         except:
        #             pass
        # elif usbf[0] == 'load':
        #     if len(usbf) < 2:
        #         print(Fore.RED+'[-]'+Fore.RESET+' Please enter driver name to load!')
        #     else:
        #         try:
        #             rem = ""
        #             load = ""
        #             if usbf[1] in load_drivers:
        #                 for main in load_all_drivers:
        #                     if usbf[1] in main:
        #                         rem = main
        #                 for drv in driver_path:
        #                     if usbf[1] in drv:
        #                         load = drv
        #                 print(Fore.BLUE+'[i]'+Fore.RESET+f' Driver "{load}" loaded successfully!')
        #             else:
        #                 print(Fore.RED+'[-]'+Fore.RESET+' No such driver: '+usbf[1])
        #         except:
        #             pass
        elif usbf[0] == 'history':
            if len(usbf) < 2:
                with open(root+'/logs/history.log', 'r') as j:
                    his = j.read()
                print(Fore.BLUE+'[i]'+Fore.RESET+' History:')
                print('')
                print(his)
            else:
                try:
                    if usbf[1] == 'delete':
                        print(Fore.MAGENTA+'[!]'+Fore.RESET+' History deleted.')
                        os.system('rm -rf '+root+'/logs/history.log')
                        os.system('touch '+root+'/logs/history.log')
                    elif usbf[1] == 'off':
                        print(Fore.MAGENTA+'[!]'+Fore.RESET+' History turned off.')
                        with open(root+'/options/history.options', 'w') as f:
                            f.write('off')
                        history = "off"
                    elif usbf[1] == 'on':
                        print(Fore.MAGENTA+'[!]'+Fore.RESET+' History turned on.')
                        with open(root+'/options/history.options', 'w') as k:
                            k.write('on')
                        history = "on"
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid command: '+usbf[1])
                except:
                    pass
        elif usbf[0] == 'changelogs':
            os.system('vim /usr/share/usbsploit/changes/changelog')
        elif usbf[0] == 'connect':
            if len(usbf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please enter the devices DEV path to connect!')
            else:
                try:
                    if "/dev" in usbf[1]:
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Unmounting device...')
                        un = getoutput('umount '+usbf[1])
                        if "Failed" in un or "No such" in un or "failed" in un:
                            print(Fore.RED+'[-]'+Fore.RESET+' Failed to unmount device')
                        else:
                            print(Fore.BLUE+'[i]'+Fore.RESET+' Mounting to "usbsploit/devices/USB"...')
                            mount = getoutput('mount '+usbf[1]+' /usr/share/usbsploit/devices/USB')
                            if "Failed" in mount or "No such" in mount or "failed" in mount:
                                print(Fore.RED+'[-]'+Fore.RESET+' Failed to mount device')
                            else:
                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Successfully mounted "'+usbf[1]+'" to USBSploit!')
                                connected = True
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid DEV path: '+usbf[1])
                except:
                    pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized command: '+usbf[0])
        if history == 'on':
            with open(root+'/logs/history.log', 'a') as log:
                logs = ""
                for i in usbf:
                    logs+=i+' '
                log.write('> '+logs+'\n')
        elif history == 'off':
            pass
        else:
            with open(root+'/logs/history.log', 'a') as log:
                logs = ""
                for i in usbf:
                    logs+=i+' '
                log.write('> '+logs+'\n')
        try:
            usbf = input('\033[4musbf\033[0m > ').strip(" ").lower()
        except KeyboardInterrupt:
            print("")
            print(Fore.RED+'[-]'+Fore.RESET+' KeyboardInterrupt detected, force quitting...')
            sys.exit()
        usbf = usbf.split()



os.system('clear')
show_banner()
main()
