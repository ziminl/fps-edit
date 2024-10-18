


import win32api

def printInfo(device):
    #print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    for varName in ['DisplayFrequency']:
        print("%s: %s"%(varName, getattr(settings, varName)))

device = win32api.EnumDisplayDevices()
printInfo(device)

##result##
#DisplayFrequency: 24



#sort only fps

import win32api
import re

def printInfo(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    frequency = getattr(settings, 'DisplayFrequency')
    print(f"{frequency}")
    #return f"{frequency}"

device = win32api.EnumDisplayDevices()
frequency_str = printInfo(device)

##result##
#24


