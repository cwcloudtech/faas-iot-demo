import os
import tkinter as tk

from utils.common import is_empty
from utils.logger import log_msg

if is_empty(os.environ.get('DISPLAY')):
    log_msg("DEBUG", "[screen] no display found, using: 0.0")
    os.environ.__setitem__('DISPLAY', ':0.0')

window = tk.Tk()
window.title("Hello")
label = tk.Label(window, text="Hello, Raspberry Pi!")
label.pack(padx=20, pady=20)
window.mainloop()
