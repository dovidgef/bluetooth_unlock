#!/usr/bin/env python

from rssi import BluetoothRSSI
import time
import yaml
import os

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

bt_address = cfg['mac_address']
intervals = cfg['intervals']
max_rssi = cfg['max_rssi']
lost_rssi = intervals * -15
delay = cfg['delay']
locked = False
last_values = []
average_value = 0

unlock_script = cfg['unlock_script']
lock_script = cfg['lock_script']

print("track device:", bt_address)
btrssi = BluetoothRSSI(addr=bt_address)

while True:
    rssi = btrssi.request_rssi()
    if rssi is not None:
        rssi = rssi[0]
    else:
        print("lost connection")
        rssi = lost_rssi

    last_values.append(rssi)
    # print(last_values)
    if len(last_values) > intervals:
        last_values.pop(0)
    average_value = sum(last_values) / len(last_values)
    print("last signal:", rssi, "average:", average_value)

    if average_value < max_rssi and not locked:
        os.system('xdg-screensaver lock')
        locked = True
        # Run lock script
        os.system(lock_script)
        # Delay before checking for unlock condition
        time.sleep(delay)
    elif average_value >= max_rssi and locked:
        os.system('loginctl unlock-session && xset dpms force on')
        locked = False
        # Run unlock script
        os.system(unlock_script)
        # Delay after unlock before checking for lock condition
        time.sleep(delay)

    time.sleep(.4)
