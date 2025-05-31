# Attach a USB device to a reMarkable Paper Pro

This project describes how I successfully attached and operated a standard USB keyboard to a reMarkable Paper Pro.
A systemd service unit is installed on the reMarkable Paper Pro 

Thanks to the great work of [haojiang99](https://github.com/haojiang99/key_nav_rm2) it is possible to map key strokes to touch gestures.
It is described how to install a systemd service on the remarkable to automatically start this script and use it to swipe through a document
using keyboard keys only.

## Disclosure
The program and drawings have been tested for my personal use only. It is not garanteed that the methods described here work for others. Please be aware that your reMarkable Paper Pro might get damaged by this. I will take no reposibilites whatsoever in that case. You have been warned.

## Prerequisites

- The reMarkable Paper Pro has be installed in *Developer Mode*
- SSH access over WLAN has to be enabled on the reMarkable Paper Pro (for details see *help* -> *Copyright and Licenses* on your reMarkable
- A USB-Y-Cable, similar to the drawing "" has to be available. 
  The reMmarkable Paper Pro does not provice power to the external USB device, therefore such a cable is required to power the device.
  A drawing of such a cable is given in the file `rpp_Y-cable_revA.pdf`
  As an additional bonus the reMarkable gets charged by this cable, too.

## Installation
The Installation of the required files is probably required after each firmware update of the reMarkable. 
To make this process easier a shell script is available to automate the installation process.

The installation is done using the following steps:

- copy these files to `/home/root/` on your reMarkable Paper Pro (for example via scp)

   `install.sh`   
   `rpp_usbkbd.service`   
   `rpp_usbkbd.sh`   
   `rpp_usbkbd2ev.py`   

- connect to you reMarkable via `ssh`, you should be in `/home/root` right now.
- make `install.sh` and `rpp_usbkbd.sh` executable (`root@imx8mm-ferrari:~$chmod +x *.sh`)
- execute `install.sh` (`root@imx8mm-ferrari:~$./install.sh`)
 That's all. After a few seconds the service should be up and running.


## Background
In order to get a USB device working at the USB-C connector of the reMarkable Paper Pro two things are required:
- A way to supply power to the device
- the USB interface has to be switched to Host-Mode

The power is supplied using a Y-cable like the one outlined in `rpp_Y-cable_revA.pdf`.

The switch to host mode is done by the command `echo host > /sys/class/usb_role/ci_hdrc.0-role-switch/role`.

Unfortunately host mode gets lost after a power cycle of the reMarkable. This is the reason why a systemd service is used to call 
a script that restarts the host mode when required.

Based on the great work of [haojiang99](https://github.com/haojiang99/key_nav_rm2) a python script is used to emulate touch gestures
to flip through the pages of a document.
Other than described in haojiang99's repository no extra software installation is required for the reMarkable Paper Pro. There is also
a limited Python installation on the device. But most of the python modules are missing. Therefore the orginal script was modified
to listen to the input-events directly.

On my device the touch screen events have to be sent to /dev/input/event3 and the USB keyboard events are received at /dev/input/event4.
It might be possible for these paths to change in the future, therefore they are defined at the very beginning of the Python script, so they
be changed easily.

**As mentioned above it is essential to enable ssh over WLAN on the reMarkable. Because the USB-Port cannot be used for shell access after this modification any more**

