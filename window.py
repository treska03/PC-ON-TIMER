import tkinter as tk


def popup(vals, hours, minutes, seconds):
   root = tk.Tk()
   root.geometry("347x70")
   root.title('Time exceeded')
   root.eval('tk::PlaceWindow . center')
   root.resizable(0, 0)

   frame2 = tk.Frame(root)
   
   information_label = tk.Label(root, text=f"Your device has been turned on for {hours}:{minutes:02}:{seconds:02} today")
   information_label.grid(column=0, row=0, sticky=tk.N, padx=5, pady=5)

   off_button = tk.Button(frame2, text="Turn OFF Device", command= lambda: on_closing(-2))
   off_button.grid(column=0, row=0)

   stop_popup_button = tk.Button(frame2, text="STOP POPUPS", command= lambda: on_closing(-1))
   stop_popup_button.grid(column=1, row=0, padx=10)

   remind_button = tk.Button(frame2, text="Remind in", width=9, command= lambda: process_data(remind_entry.get()))
   remind_button.grid(column=2, row=0)

   remind_entry = tk.Entry(frame2, width=3)
   remind_entry.grid(column=3, row=0)

   remind_button = tk.Label(frame2, text="minutes")
   remind_button.grid(column=4, row=0)
   
   frame2.grid(column=0, row=1)

   def process_data(input_data):
      if not input_data or not input_data.isdigit():
         error_label = tk.Label(root, text="Please enter a correct number", fg="red")
         root.geometry("347x80")
         error_label.grid(column=0, row=2)
         raise TypeError("Please enter a correct number")

      return on_closing(int(input_data))

   def on_closing(val):
      vals.append(val)
      root.destroy()
      return 

   root.protocol("WM_DELETE_WINDOW", lambda: on_closing(1))
   root.mainloop()

if __name__ == "__main__":
   random_list = []
   print(popup(random_list, 5, 5,0))
   print(random_list)
