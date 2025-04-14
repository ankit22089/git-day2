import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Customize the clock label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Define time updating function
def update_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, update_time)  # update every 1 second

# Start the clock
update_time()
root.mainloop()
