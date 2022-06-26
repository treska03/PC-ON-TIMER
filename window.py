import tkinter as tk
from tkinter import ttk


def popup():
   # root window
   root = tk.Tk()
   root.geometry("400x100")
   root.title('Time exceeded')
   root.resizable(0, 0)

   # configure the grid
   root.columnconfigure(0, weight=1)
   root.columnconfigure(1, weight=1)
   
   def information(n):
      information_label = ttk.Label(root, text=f"Your device has been turned on for {n} today")
      information_label.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)


   information(10)
   off_button = ttk.Button(root, text="Turn OFF device")
   off_button.grid(column=0, row=1)

   stop_popup_button = ttk.Button(root, text="STOP")
   stop_popup_button.grid(column=1, row=1)

   remind_button = ttk.Label(root, text="Remind in:")
   remind_button.grid(column=2, row=1)

   remind_entry = ttk.Entry(root,  show="*")
   remind_entry.grid(column=3, row=1)

   

   def on_closing():
      root.destroy()
      return 

   root.protocol("WM_DELETE_WINDOW", on_closing)
   root.mainloop()

if __name__ == "__main__":
   popup()
