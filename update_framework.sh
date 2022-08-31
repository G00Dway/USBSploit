BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        echo -e "\033[1;33m[!] \033[0mUpdate detected, trying to update..."
        git pull &> update-viagit.log
        echo "VERSION.txt" > latest
        echo -e "\033[1;32m[+] \033[0mDone, but no output, logs saved as: 'update-viagit.log', skipping..."
else
        echo -e "\033[1;77m[i] \033[0mNo updates, this is the latest version"
fi