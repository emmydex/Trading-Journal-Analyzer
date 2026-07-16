
#Requirements 12/7/2026
#Create the statistics frame

#Total Trades:       0
#Winning Trades:     0
#Losing Trades:      0
#Breakeven Trades:   0
#Win Rate:           0%
#Total Profit:       $0
#Average Profit:     $0

import tkinter as tk
from tkinter import filedialog
# creating the window
window = tk.Tk()

#created the title
window.title("Trading Journal Analyzer V4")
#set the window size
window.geometry("700x600")

#created a frame and gave it the variable frame_one
frame_one = tk.Frame(window)
frame_one.pack(pady=20)

# a label Trade Pair
label_one = tk.Label(frame_one, text="Trade Pair")
label_one.pack()

# an entry widget
entry_one = tk.Entry(frame_one)
entry_one.pack()

#the button function
def read_text():
   
   value = entry_one.get()
   label_two.config(text=f"Selected Pair:  {value}")

#a button widget
button_one = tk.Button(frame_one, text="Show Pair", command=read_text)
button_one.pack()

# another label
label_two = tk.Label(frame_one, text="Selected Pair")
label_two.pack()

#created the button_frame
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

def file_import():
   global file_browse
   file_browse = filedialog.askopenfilename(initialdir="/", 
   title="Select a file", filetypes=[("CSV FILE", "*.*")]
   )
   
   print(f"file selected path: {file_browse}")


#import CSV button
import_button = tk.Button(button_frame, text="Import CSV", command=file_import)
import_button.pack(side="left")

#Analyze Button
analyze_button = tk.Button(button_frame, text="Analyze", command=file_browse)
analyze_button.pack(side="left")

# clear button
clear_button = tk.Button(button_frame, text="Clear")
clear_button.pack(side="left")

# creating the stats_frame
stats_frame = tk.Frame(window)
stats_frame.pack(pady=20)

#Total Trades:       0
total_trades = tk.Label(stats_frame, text="Total Trades: ")
total_trades.grid(row=0, column=0, pady=5, padx=10, sticky="w")

total_trades_value = tk.Label(stats_frame, text="0")
total_trades_value.grid(row=0, column=1,  pady=5, padx=10, sticky="w")


#Winning Trades:     0
winning_trades = tk.Label(stats_frame, text="Winning Trades: ")
winning_trades.grid(row=1, column=0,  pady=5, padx=10, sticky="w")

winning_trades_value = tk.Label(stats_frame, text="0")
winning_trades_value.grid(row=1, column=1,  pady=5, padx=10, sticky="w")

#Losing Trades:      0
losing_trades = tk.Label(stats_frame, text="Losing Trades: ")
losing_trades.grid(row=2, column=0,  pady=5, padx=10, sticky="w")

losing_trades_value = tk.Label(stats_frame, text="0")
losing_trades_value.grid(row=2, column=1,  pady=5, padx=10, sticky="w")

#Breakeven Trades:   0
breakeven_trades = tk.Label(stats_frame, text="BreakEven Trades: ")
breakeven_trades.grid(row=3, column=0,  pady=5, padx=10, sticky="w")

breakeven_trades_value = tk.Label(stats_frame, text="0")
breakeven_trades_value.grid(row=3, column=1,  pady=5, padx=10, sticky="w")

#Win Rate:           0%
win_rate = tk.Label(stats_frame, text="Win Rate: ")
win_rate.grid(row=4, column=0,  pady=5, padx=10, sticky="w")

win_rate_value = tk.Label(stats_frame, text="0%")
win_rate_value.grid(row=4, column=1,  pady=5, padx=10, sticky="w")

#Total Profit:       $0
total_profit = tk.Label(stats_frame, text="Total Profit: ")
total_profit.grid(row=5, column=0,  pady=5, padx=10, sticky="w")

total_profit_value = tk.Label(stats_frame, text="$0")
total_profit_value.grid(row=5, column=1,  pady=5, padx=10, sticky="w")

#Average Profit:     $0
average_profit = tk.Label(stats_frame, text="Average Profit: ")
average_profit.grid(row=6, column=0,  pady=5, padx=10, sticky="w")

average_profit_value = tk.Label(stats_frame, text="$0")
average_profit_value.grid(row=6, column=1,  pady=5, padx=10, sticky="w")

# tto keep the window always running
window.mainloop()
