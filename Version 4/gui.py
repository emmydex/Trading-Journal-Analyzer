import tkinter as tk
# running a demo

window = tk.Tk()
window.title("Trading Journal Analyzer")
window.geometry("500x300")
 #creating a label status_label
status_label = tk.Label(window, text="Status: Not clicked")

status_label.pack(pady=20)

#created a function button_clicked which changes the label when clicked
def button_clicked():
    status_label.config(
        text="Status: Button Clicked!"
    )


button = tk.Button(
    window,
    text="Click Me",
    #passed the button_clicked function to button's command parameter
    command=button_clicked
)

button.pack()
window.mainloop()