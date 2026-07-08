import tkinter as tk

window = tk.Tk()
window.title("Trading Journal Analyzer")
window.geometry("800x500")
label = tk.Label(window, text="My First Trading Journal")
label.pack()
another_label =tk.Label(window, text='lets Create, oluwafemi')
another_label.pack()
button = tk.Button(window, text= 'import CSV', command=load_trades)

window.mainloop()