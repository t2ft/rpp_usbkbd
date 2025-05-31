#!/bin/sh
echo host > /sys/class/usb_role/ci_hdrc.0-role-switch/role
sleep 3
/usr/bin/python3 /home/root/rpp_usbkbd/rpp_usbkbd2ev.py
