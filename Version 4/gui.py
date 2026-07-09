import tkinter as tk
# running a demo

window = tk.Tk()
window.title("Trading Journal Analyzer")
window.geometry("500x300")
 #creating a label status_label
status_label = tk.Label(window, text="Status: Not clicked")

status_label.pack(pady=20)

#created a function button_clicked
def button_clicked():
    pass

window.mainloop()