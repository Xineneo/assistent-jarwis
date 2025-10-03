import ctypes
from Voice import speak

VK_LWIN = 0x5B
VK_D = 0x44
KEYEVENTF_KEYUP = 0x0002

def show_desktop():
    # Нажать Win
    ctypes.windll.user32.keybd_event(VK_LWIN, 0, 0, 0)
    # Нажать D
    ctypes.windll.user32.keybd_event(VK_D, 0, 0, 0)
    # Отпустить D
    ctypes.windll.user32.keybd_event(VK_D, 0, KEYEVENTF_KEYUP, 0)
    # Отпустить Win
    ctypes.windll.user32.keybd_event(VK_LWIN, 0, KEYEVENTF_KEYUP, 0)
    speak("Выполняю")
    
