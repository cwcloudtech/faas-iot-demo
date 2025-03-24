import os

import tkinter as tk

from utils.common import is_empty
from utils.logger import log_msg

def display(title, message):
    if is_empty(os.environ.get('DISPLAY')):
        log_msg("DEBUG", "[gui] no display found, using: :0.0")
        os.environ.__setitem__('DISPLAY', ':0.0')

    try:
        window = tk.Tk()
        window.title(title)
        window.attributes("-fullscreen", True)
        window.bind("<Escape>", lambda _: window.attributes("-fullscreen", False))

        label = tk.Label(window, text=message, font=("Arial", 20))
        label.place(relx=0.5, rely=0.5, anchor='center')
        window.mainloop()
    except tk.TclError as te:
        log_msg("WARN", f"[gui] unexpected error: title={title}, message={message}, error={te}")
 
