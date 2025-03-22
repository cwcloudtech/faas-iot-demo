import tkinter as tk

window = tk.Tk()
window.title("Hello")
label = tk.Label(window, text="Hello, Raspberry Pi!")
label.pack(padx=20, pady=20)
window.mainloop()
