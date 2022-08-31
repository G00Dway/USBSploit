import os
import time
import sys
modules = "/usr/share/usbsploit/modules"



def check():
    get = os.listdir(modules)
    for name in get:
        if name == "bus":
            continue
        if os.path.isfile(modules+'/'+name):
            if name == "requirements.txt":
                with open(modules+'/'+name, "r") as requirements:
                    req = requirements.readline() 
                os.system('pip install '+req+' &>> pip.log')
        else:
            other = os.listdir(modules+'/'+name)
            for module in other:
                if module == "bus":
                    continue
                if name == "requirements.txt":
                    with open(modules+'/'+name+'/'+module, "r") as requirements:
                        req = requirements.readline() 
                    os.system('pip install '+req+' &>> pip.log')



try:
    if os.path.exists(modules):
        check()
    else:
        sys.exit()
except:
    pass

sys.exit()