# Bluetooth_Listener

Code referenced from: https://github.com/Douglas6/cputemp


## Prerequisites

    1) sudo nano /etc/systemd/system/dbus-org.bluez.service 
    2) Look for ExecStart and replace it with below line
        ExecStart=/usr/libexec/bluetooth/bluetoothd -E
    3) Save the file and reboot (sudo reboot)


## Troubleshooting

### 1. Anytime device is getting connected then follow the below steps
    1) Stop the bluetooth listener program
    2) Identify the device connected to pi by executing the below command
        bluetoothctl devices
    3) Remove the device which has connection issue
        bluetoothctl remove <PHONE_MAC>
    4) Run the below set of commands
        sudo btmgmt power off
        sudo btmgmt bredr off
        sudo btmgmt sc off
        sudo btmgmt bondable off
        sudo btmgmt power on
    5) sudo btmgmt info and verify that "current settings" key should be "powered le"
    6) Start the bluetooth listener again
