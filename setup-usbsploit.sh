#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m
echo -e "\033[1;77m[i] \033[0mLoading/Installing setup script requirements (APT) (This might take long)..."
echo "Packages to install: 'python dfu-programmer perl php ruby php-cgi php-xml bc bd hostapd-wpe usbview usbutils gcc pmount'" >> apt.log
apt install python-is-python3 -y &>> apt.log
apt install python3-pip -y &>> apt.log
apt install python2-is-python3 -y &>> apt.log
apt install dfu-programmer perl php ruby php-cgi php-xml bc bd -y &>> apt.log
apt install hostapd-wpe usbview usbutils gcc pmount -y &>> apt.log
echo -e "\033[1;33m[!] \033[0mChecking PIP..."
echo -e "\033[1;77m[i] \033[0mInstalling packages via PIP (This might take long)..."
echo "Packages to install: 'colorama scapy future paramiko pyfiglet sploitkit argparse bs4 pyusb libusb1 pylibusb pyparsing'" >> pip.log
pip install colorama scapy future paramiko pyfiglet sploitkit argparse bs4 pyusb libusb1 pylibusb pyparsing &>> pip.log
echo -e "\033[1;77m[i] \033[0mRequirements installed, continuing..."
sleep 1
echo -e "\033[1;33m[!] \033[0mChecking for updates..."
bash bus/update_framework.sh
sleep 1
mkdir /usr/share/usbsploit-drivers
echo -e "\033[1;77m[i] \033[0mBuilding database using GIT at /usr/share..."
git clone https://github.com/G00Dway/USBSploit /usr/share/usbsploit &>> git-db.log
mkdir /usr/share/usbsploit-update
python3 usb/install/driver_install.py
echo -e "\033[1;77m[i] \033[0mCopying execution files..."
chmod +x /usr/share/usbsploit/bin/consoleusb/usbconsole
chmod +x /usr/share/usbsploit/bin/consoleusb/usbcc
cp -r /usr/share/usbsploit/bin/consoleusb/usbconsole /usr/bin
cp -r /usr/share/usbsploit/bin/consoleusb/usbcc /usr/bin
echo -e "\033[1;32m[+] \033[0mBuild done, but no output"
echo -e "\033[1;77m[i] \033[0mLoading drivers..."
echo -e "\033[1;77m[i] \033[0mLoading setup files..."
mkdir /usr/share/usbsploit-drivers/DRIVERS
python3 /usr/share/usbsploit/usb/opt/load_driver.py
echo -e "\033[1;77m[i] \033[0mFinishing setup script..."
bash /usr/share/usbsploit/src/bus.sh
read -p "[?] Do you want to check modules for any corrupted requirements? (Y/n): " MODULES
if [ $MODULES = "Y" ] || [ $MODULES = "y" ] || [ $MODULES == "YES" ] || [ $MODULES = "yes" ]; then
        echo -e "\033[1;77m[i] \033[0mChecking/Installing modules requirements (This might take long)..."
        python3 /usr/share/usbsploit/modules/bus/update_modules.py
else
        echo -e "\033[1;77m[i] \033[0mSkipping modules check..."
fi
echo -e "\033[1;77m[i] \033[0mCopying launcher files..."
cp -r /usr/share/usbsploit/desktop/usbsploit.desktop /usr/share/applications
cp -r /usr/share/usbsploit/desktop/usbsploit.desktop /usr/share/kali-menu/applications
sleep 1
echo -e "\033[1;77m[i] \033[0mCleaning up..."
rm -rf /usr/share/usbsploit/setup-usbsploit.sh
rm -rf /usr/share/usbsploit/uninstall-usbsploit.sh
rm -rf /usr/share/usbsploit/README.md
rm -rf /usr/share/usbsploit/LICENSE
echo "-------------------------------------------------------------------------------------------"
echo -e "\033[1;32m[+] \033[0mSetup script finished, execute usbsploit via sudo in terminal by typing: 'usbconsole' or 'usbcc'"