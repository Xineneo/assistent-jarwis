import config
import subprocess
from Voice import speak
import time
import os




def shutdown_computer():
    speak("Выключаю компьютер")
    time.sleep(1)
    os.system("shutdown /s /t 0")


def open_opera():
    os.startfile(config.browser_path[0])
    
    speak("Открываю оперу")

def open_url_youtube():
    subprocess.Popen([config.browser_path[0],config.URL[0]], bufsize=0)
    speak("Открываю youtube")

def open_vsc():
    os.startfile(os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\code.exe"))
    speak("Редактор кода открыт")

def bot_odp():
    speak("Да я здесь")

def close_opera():
    os.system("taskkill /f /im opera.exe")
    speak("Закрываю")

def close_vsc():
    os.system("taskkill /f /im code.exe")

def search_youtube(request):
    subprocess.Popen([config.browser_path[0], request],bufsize=0)
