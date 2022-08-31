cd /usr/share/usbsploit
echo -e "\033[1;77m[i] \033[0mChecking for latest updates..."
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;33m[!] \033[0mUpdate detected, building..."
        echo -e "\033[1;77m[i] \033[0mCopying optional files to backup directory..."
        bash /usr/share/usbsploit/bus/base/copy_op.sh
        echo -e "\033[1;33m[!] \033[0mUpdating (This might take a while)..."
        echo -e "\033[1;33m[!] \033[0mTrying to update using GIT..."
        sleep 1
        python3 /usr/share/usbsploit/bus/base/update_pull.py
else
        echo -e "\033[1;77m[i] \033[0mNo updates available, this is the latest version"
fi