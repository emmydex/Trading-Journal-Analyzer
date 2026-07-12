
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
#create the button frame
# add the import CSV button
#add the Analyze button
#add the Clear button

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
button_frame.pack()

#import CSV button
import_button = tk.Button(button_frame, text="Import CSV")
import_button.pack(side="left")

#Analyze Button
analyze_button = tk.Button(button_frame, text="Analyze")
analyze_button.pack(side="left")

# clear button
clear_button = tk.Button(button_frame, text="Clear")
clear_button.pack(side="left")

# tto keep the window always running
window.mainloop()
