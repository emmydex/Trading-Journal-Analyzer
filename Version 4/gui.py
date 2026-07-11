import tkinter as tk
# running a demo

window = tk.Tk()
window.title("Trading Journal Analyzer V4")
window.geometry("900x600")
 #creating the frame structure

 #Button frame
button_frame = tk.Frame(window)
button_frame.pack()

# Statistics Frame
stats_frame = tk.Frame(window)
stats_frame.pack()

window.mainloop()