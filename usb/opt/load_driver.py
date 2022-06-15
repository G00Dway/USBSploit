import os
import time
import sys
import colorama
from colorama import Fore
colorama.init()
drive_path = "/usr/share/usbsploit-drivers"

def install():
    try:
        if os.path.exists("/usr/share/usbsploit-drivers"):
            pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' DRIVER Path was not found! exiting...')
            exit()
    except:
        pass

    get = os.listdir(drive_path)
    for driver in get:
        if os.path.isfile(drive_path+'/'+driver):
            if driver == "about.txt":
                with open(drive_path+'/'+driver, "r") as g:
                    about = g.read()
            else:
                pass
            if ".py" in driver and "setup" in driver or ".pyw" in driver and "setup" in driver:
                with open("logs", "a") as f:
                    f.write("Launching: "+driver)
                os.system(f'python3 {drive_path}/{driver}')
            else:
                with open("logs", "a") as f:
                    f.write("Ignoring: "+driver)
        else:
            get_in = os.listdir(drive_path+'/'+driver)
            for main in get_in:
                if main == "about.txt":
                    with open(drive_path+'/'+driver+'/'+main, "r") as g:
                        about = g.read()
                else:
                    pass
                if ".py" in main and "setup" in main or ".pyw" in main and "setup" in main:
                    with open("logs", "a") as f:
                        f.write("Launching: "+main)
                    os.system(f'python3 {drive_path}/{driver}/{main}')
                else:
                    with open("logs", "a") as f:
                        f.write("Ignoring: "+driver)


install()