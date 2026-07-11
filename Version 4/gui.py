
#Requirements
#Create the window.
#Set the title to Trading Journal Analyzer V4.
#Set the window size.
#Create one frame.
#Inside the frame create:
#A label that says Trade Pair
#An Entry widget
#A button labeled Show Pair
#A label that initially says Selected Pair:
#When the button is clicked:
#Read the Entry using .get()
#Update the last label using .config()
#It should become:
#Selected Pair: EURUSD

#(or whatever the user typed.)
import tkinter as tk

# creating the window
window = tk.Tk()

#created the title
window.title("Trading Journal Analyzer V4")
#set the window size
window.geometry("700x600")

#created a frame and gave it the variable frame_one
frame_one = tk.Frame(window)
frame_one.pack()

# a label Trade Pair
label_one = tk.Label(frame_one, text="Trade Pair")
label_one.pack()

# an entry widget
entry_one = tk.Entry(frame_one)
entry_one.pack()

#a button widget
button_one = tk.Button(frame_one, text="Show Pair")
button_one.pack()

# another label
label_two = tk.Label(frame_one, text="Selected Pair")

# tto keep the window always running
window.mainloop()
