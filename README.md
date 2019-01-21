### Bluetooth Unlock
This program allows you to automatically lock/unlock your Ubuntu desktop based
on a bluetooth devices proximity to your computer. The devices bluetooth needs to be on 
but it should not need to be in discoverable mode for it to work.

#### Prerequisites 
* Ubuntu
* Gnome Desktop
* Python 3
* Bluetooth adaptor
* Additional bluetooth device (e.g. cell phone)

It has only been tested on Ubuntu 18.04 with Gnome desktop

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
    ```