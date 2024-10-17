#pip install pywin32
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

ENUM_CURRENT_SETTINGS = -1

class DEVMODE(ctypes.Structure):
    _fields_ = [
        ('dmDeviceName', wintypes.WCHAR * 32),
        ('dmSpecVersion', wintypes.WORD),
        ('dmDriverVersion', wintypes.WORD),
        ('dmSize', wintypes.WORD),
        ('dmDriverExtra', wintypes.WORD),
        ('dmFields', wintypes.DWORD),
        ('dmPositionX', wintypes.LONG),
        ('dmPositionY', wintypes.LONG),
        ('dmDisplayOrientation', wintypes.DWORD),
        ('dmDisplayFixedOutput', wintypes.DWORD),
        ('dmColor', wintypes.DWORD),
        ('dmDuplex', wintypes.DWORD),
        ('dmYResolution', wintypes.DWORD),
        ('dmTTOption', wintypes.DWORD),
        ('dmCollate', wintypes.DWORD),
        ('dmFormName', wintypes.WCHAR * 32),
        ('dmLogPixels', wintypes.DWORD),
        ('dmBitsPerPel', wintypes.DWORD),
        ('dmPelsWidth', wintypes.DWORD),
        ('dmPelsHeight', wintypes.DWORD),
        ('dmDisplayFlags', wintypes.DWORD),
        ('dmDisplayFrequency', wintypes.DWORD),
        ('dmICMMethod', wintypes.DWORD),
        ('dmICMIntent', wintypes.DWORD),
        ('dmMediaType', wintypes.DWORD),
        ('dmDitherType', wintypes.DWORD),
        ('dmReserved1', wintypes.DWORD),
        ('dmReserved2', wintypes.DWORD),
        ('dmPanningWidth', wintypes.DWORD),
        ('dmPanningHeight', wintypes.DWORD),
    ]

def set_refresh_rate(rate):
    dm = DEVMODE()
    dm.dmSize = ctypes.sizeof(DEVMODE)

    if user32.EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, ctypes.byref(dm)):
        dm.dmDisplayFrequency = rate
        dm.dmFields |= 0x400000  # DM_DISPLAYFREQUENCY

        result = user32.ChangeDisplaySettingsW(ctypes.byref(dm), 0)
        if result != 0:
            print("Failed to change refresh rate")
        else:
            print(f"Refresh rate changed to {rate} Hz")

desired_refresh_rate = 60  # Set the desired refresh rate here
set_refresh_rate(desired_refresh_rate)
