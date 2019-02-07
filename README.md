### Bluetooth Unlock
This program allows you to automatically lock/unlock your Ubuntu desktop based
on the distance of a bluetooth devices from your computer. 
It should work even if the device is not in discoverable mode.

It also allows you to run a bash script on system lock/unlock.
This for example could be used to allow you to play/pause a music player automatically 
on system lock/unlock using a program like [playerctl](https://github.com/acrisci/playerctl)

#### Prerequisites 
* Ubuntu
* Python 3
* Bluetooth adaptor
* Additional bluetooth device (e.g. cell phone)

It has been tested on both Ubuntu 16.04 and 18.04

#### Setup Instructions
1. Install libbluetooth-dev package `sudo apt-get install libbluetooth-dev`
2. Clone the repo
3. Optionally setup virtual environment
4. `pip install -r requirements.txt`

#### Usage Instructions
* Add bluetooth device to use for proximity sensing.

   1. Make sure your device is discoverable
   2. Run `python3 find_devices.py`
   3. Choose your device and it will be automatically added to the config.yml file.
   
* Start proximity detection
  1. Run `python3 bluetooth_unlock.py` to start automatic lock/unlock based on device proximity.
  
* Setup bash scripts for running on system lock/unlock
  * I have provided `unlock.sh` and `lock.sh` scripts which run on unlock/lock.
  * You can modify them for your needs, or you can provide the path to other
  scripts in the config.yml file.

* Optionally modify the config.yml file to modify program settings
    ```bash
    # delay: 5
    Sets how long program waits after locking or unlocking system 
    before it attempts to detect device proximity again.
    
    # intervals: 10
    Sets how large a set of signal strength values the program averages 
    to determine the devices proximity.
 
    # mac_address: A4:E4:B8:A5:A4:0E
    Determines which bluetooth device to track based on devices mac address.
    May be automatically set by using find_devices.py script

    # max_rssi: -36
    Determines the signal strength that will cause computer to be locked  
  
    # unlock_script: ./unlock.sh
    Path to bash script which runs when system is unlocked

    # lock_script: ./lock.sh
    Path to bash script which runs when system is locked
    ```
    

Credit to [FrederikBolding](https://github.com/FrederikBolding/bluetooth-proximity) for the RSSI detection script