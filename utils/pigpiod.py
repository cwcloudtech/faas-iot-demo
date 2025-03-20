
import os
import subprocess

from time import sleep

def is_pigpiod_running():
    return os.system("pgrep pigpiod > /dev/null") == 0

def start_pigpiod():
    if not is_pigpiod_running():
        subprocess.run(["sudo", "pigpiod"], check=True)
        sleep(2)
