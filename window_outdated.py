import tkinter as tk
from tkinter import ttk


def popup():
   # root window
   root = tk.Tk()
   root.geometry("600x100")
   root.title('Time exceeded')
   root.resizable(0, 0)

   #frames
   frame1 = tk.Frame(root)
   frame2 = tk.Frame(root)

   
   def information(n):
      information_label = ttk.Label(frame1, text=f"Your device has been turned on for {n} today")
      information_label.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)


   information(10)
   off_button = ttk.Button(frame2, text="Turn OFF device")
   off_button.grid(column=0, row=1)

   stop_popup_button = ttk.Button(frame2, text="STOP")
   stop_popup_button.grid(column=1, row=1)

   remind_button = ttk.Label(frame2, text="Remind in:")
   remind_button.grid(column=2, row=1)

   remind_entry = ttk.Entry(frame2,  show="*")
   remind_entry.grid(column=3, row=1)

   frame1.pack(pady=10)
   frame2.pack(pady=10)

   

   def on_closing():
      root.destroy()
      return 

   root.protocol("WM_DELETE_WINDOW", on_closing)
   root.mainloop()

if __name__ == "__main__":
   popup()
