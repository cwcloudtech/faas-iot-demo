import os

import tkinter as tk

from utils.common import is_empty
from utils.logger import log_msg

def display(title, message):
    if is_empty(os.environ.get('DISPLAY')):
        log_msg("DEBUG", "[screen] no display found, using: 0.0")
        os.environ['DISPLAY'] = ':0.0'

    window = tk.Tk()
    window.title(title)
    window.attributes("-fullscreen", True)
    window.bind("<Escape>", lambda _: window.attributes("-fullscreen", False))

    label = tk.Label(window, text=message)
    label.pack(padx=20, pady=20)
    window.mainloop()
