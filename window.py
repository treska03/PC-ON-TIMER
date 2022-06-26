import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("400x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


def popup(n):
   information_label = ttk.Label(root, text=f"Your device has been turned on for {n} today")
   information_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)


popup(10)
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)


# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)


root.mainloop()
