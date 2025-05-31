#!/bin/sh
echo "Installing USB Keyboard event mapper"
mkdir /home/root/rpp_usbkbd
mv rpp_* /home/root/rpp_usbkbd/
mount / -o remount,rw
cp rpp_usbkbd.service /etc/systemd/system/
systemctl enable --now rpp_usbkbd.service
echo "starting system service"
sleep 1
mount / -o remount,ro
sleep 4
systemctl status rpp_usbkbd.service
