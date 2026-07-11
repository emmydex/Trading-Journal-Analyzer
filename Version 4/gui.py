
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
window.geometry("900x600")

# tto keep the window always running
window.mainloop()
