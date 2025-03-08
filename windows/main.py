import ctypes
from win32api import EnumDisplayDevices, EnumDisplaySettings, ChangeDisplaySettings
from win32con import DM_DISPLAYFREQUENCY, CDS_UPDATEREGISTRY

rr = 60  # 24 50 60 100 120 144

device = EnumDisplayDevices(None, 0)  #1st monitor
settings = EnumDisplaySettings(device.DeviceName, 0)

original_bpp = settings.BitsPerPel

settings.PelsWidth = 1920
settings.PelsHeight = 1080
settings.DisplayFrequency = rr  
settings.BitsPerPel = original_bpp

result = ChangeDisplaySettings(settings, CDS_UPDATEREGISTRY)

if result == 0:
    print(f"1920x1080, fps {rr}Hz")
else:
    print("error.")
