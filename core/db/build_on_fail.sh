echo -e "\033[1;31m[-] \033[0mBuild failed, trying again..."
git clone https://github.com/G00Dway/USBSploit /usr/share/usbsploit &> git-db.log
python3 /usr/share/usbsploit/core/db/check_db.py