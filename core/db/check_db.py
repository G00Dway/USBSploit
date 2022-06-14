import os
from subprocess import getoutput

try:
    if os.path.exists("/usr/share/usbsploit"):
        pass
    else:
        with open("/usr/share/usbsploit/core/db/git-db.log", 'r') as check:
            c = check.read()
            if "Failed" in c or "failed" in c or "fail" in c or "Fail" in c:
                output = getoutput("bash /usr/share/usbsploit/core/db/build_on_fail.sh")
                if "bash:" in output or ")" in output or "failed" in output:
                    os.system("bash /usr/share/usbsploit/core/db/build_on_fail.sh")
                else:
                    exit()
except:
    exit()
exit()