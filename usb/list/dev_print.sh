for i in /sys/class/block/*; do
    /sbin/udevadm info -a -p $i | grep -qx '    SUBSYSTEMS=="usb"' &&
    echo ${i##*/}
done