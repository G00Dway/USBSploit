# import os
# import usb
# import sys
# devices = []
# devices.append({'device': 'test/pro'})
# # devices = usb.core.find(find_all=True)

# # sys.stdout.write('There are ' + len(devices) + ' in the system\n.')
# for name in devices:
#     if 'device' in name.keys():
#         zoz = name['device'].split('/')
#         print(zoz)
#         print(zoz[1])

from subprocess import getoutput
out = getoutput('dir')
for line in out.split('\n'):
    print("Name ---> "+line)