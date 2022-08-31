import os
import time
import sys
import colorama
from colorama import Fore
if len(sys.argv) < 3:
    exit()

module = sys.argv[1]
run = "/usr/share/usbsploit/"+sys.argv[2]
module = module.split("/")
name = module[1]+'/'+module[2]

# options
FOLDER = ""
NAME = "tweak.bat"
help_menu = '''
Global Commands
=================

    command                 description
    -------                 -----------
    clear                   Clear terminal window
    back                    Go one input back

Module Commands
=================

    command                 description
    -------                 -----------
    set <option> <value>    Set the specified option to specified value
    show <arg>              Show <arg> specified menu, type "show" for more options
    start, run, execute     Load the selected module
'''

try:
    usbf = input(f'\033[4musbf\033[0m-(MODULE: {Fore.RED}{name}{Fore.RESET}) > ').strip(" ")
except KeyboardInterrupt:
    exit()
usbf = usbf.split()
while True:
    if usbf == []:
        pass
    elif usbf[0] == 'help':
        print(help_menu)
    elif usbf[0] == 'clear':
        os.system('clear')
    elif usbf[0] == 'back':
        sys.exit()
    elif usbf[0] == 'show':
        if len(usbf) < 2:
            print(Fore.RED+'[-]'+Fore.RESET+' Available menus: (options)')
        else:
            try:
                if usbf[1] == 'options':
                    print(f'''
--> Options of the ({name}) module:
========================================================

    option              description                                   current value
    ------              -----------                                   -------------
    FOLDER              Folder name where data will be stored         {FOLDER} 
    NAME                Name of the executable data stealer file      {NAME}
''')
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Not a valid menu: '+usbf[1])
            except:
                pass
    elif usbf[0] == 'set':
        if len(usbf) < 3:
            print(Fore.RED+'[-]'+Fore.RESET+' Usage: set <option> <value>')
        else:
            try:
                if usbf[1].isdigit():
                    print(Fore.RED+'[-]'+Fore.RESET+' Unknown digital option: '+str(usbf[1]))
                else:
                    use = usbf[1].upper()
                    if use == "FOLDER":
                        FOLDER=str(usbf[2])
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' {use} ==> {FOLDER}')
                    elif use == "NAME":
                        NAME=str(usbf[2])+'.bat'
                        print(Fore.BLUE+'[i]'+Fore.RESET+f' {use} ==> {NAME}')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Unknown option: '+usbf[1]) 
            except:
                pass
    elif usbf[0] == 'start' or usbf[0] == 'run' or usbf[0] == 'execute':
        if FOLDER == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Please setup all the required (blank) options!')
        else:
            try:
                os.system(f'python3 {run} {FOLDER} {NAME}')
            except:
                pass
            print(Fore.BLUE+'[i]'+Fore.RESET+' Module execution completed.')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unknown command: '+usbf[0])
    try:
        usbf = input(f'\033[4musbf\033[0m-(MODULE: {Fore.RED}{name}{Fore.RESET}) > ').strip(" ")
    except KeyboardInterrupt:
        exit()
    usbf = usbf.split()