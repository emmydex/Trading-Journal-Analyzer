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
stats_frame.pack(pady=20)

#adding a entry widget
entry = tk.Entry(window)
entry.pack(pady=20)

tk.Label(stats_frame, text="Total Trades").grid(row=0, column=0)
tk.Label(stats_frame, text="0").grid(row=0, column=1)
tk.Label(stats_frame, text="Winning Trades").grid(row=1, column=0)
tk.Label(stats_frame, text="0").grid(row=1, column= 1)
tk.Label(stats_frame, text="Losing Trades").grid(row=2, column=0)
tk.Label(stats_frame, text="0").grid(row=2, column=1)
 
#Table Frame
table_frame = tk.Frame(window)
table_frame.pack()

window.mainloop()