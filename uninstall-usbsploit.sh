#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m
echo -e "\033[1;77m[i] \033[0mUninstalling USBSploit framework..."
read -p "[?] Are you sure to uninstall usbsploit framework? (Y/n): " MODULES
if [ $MODULES = "Y" ] || [ $MODULES = "y" ] || [ $MODULES == "YES" ] || [ $MODULES = "yes" ]; then
        echo -e "\033[1;33m[!] \033[0mUninstalling framework..."
        rm -rf /usr/share/usbsploit-drivers
        rm -rf /usr/share/applications/usbsploit.desktop
        rm -rf /usr/share/kali-menu/applications/usbsploit.desktop
        rm -rf /usr/share/usbsploit-update
        sleep 1
        rm -rf /usr/bin/usbconsole
        echo -e "\033[1;33m[!] \033[0mRemoving/Cleaning main database..."
        rm -rf /usr/share/usbsploit
        rm -rf /usr/bin/usbcc
        sleep 1
        echo -e "\033[1;33m[!] \033[0mRemoving database files in /root..."
        rm -rf /root/.usbcc
        echo -e "\033[1;77m[i] \033[0mCleaning up..."
        echo -e "\033[1;32m[+] \033[0mUninstallation successfull!"
        echo -e "\033[1;32m[+] \033[0mThank you for using usbsploit framework!"
else
        echo -e "\033[1;77m[i] \033[0mUninstall skipped, Exiting..."
fi