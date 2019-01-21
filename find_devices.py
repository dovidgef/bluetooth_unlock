#!/usr/bin/env python

# simple inquiry example
import bluetooth
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

nearby_devices = bluetooth.discover_devices(4, lookup_names=True,)
found = len(nearby_devices)

if found:
    print("Devices Found:")
    for idx, device in enumerate(nearby_devices):
        print("Device %s  %s - %s" % (idx, device[0], device[1]))
    while True:
        print("Choose your devices number:")
        try:
            choice = int(input())
            device = nearby_devices[choice]
        except (ValueError, IndexError):
            print("Error: please enter you devices number only e.g. 0")
            continue

        break

    print("Device:", device[1], "has been added to the config")

    cfg['mac_address'] = device[0]

    with open("config.yml", 'w') as ymlfile:
        yaml.dump(cfg, ymlfile, default_flow_style=False)
else:
    print("No devices found, make sure your device is discoverable")
