import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
#window.geometry("500x500")
window.title("Calculator by Iven Liang")

window.resizable(0,0)
# window.rowconfigure(0,weight=1)
# window.rowconfigure(1,weight=1)
# window.rowconfigure(2,weight=1)
# window.rowconfigure(3,weight=1)
# window.rowconfigure(4,weight=4)
buttonwidth = 3
buttonheight = 1

# Create an entry widget to display the calculations
entry = tk.Entry(window, font="Arial 18")
entry.grid(row=0, column=0, columnspan=4, padx=2, pady=2,sticky="nsew")

# Define the buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    (".", 4, 0),
    ("0", 4, 1),
    #("=", 4, 2),
    ("+", 4, 3),
]

buttonpadx = 20
buttonpady = 20

spacingpadx = 2
spacingpady = 2
# Create the buttons and associate them with the functions
for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, width=buttonwidth, height=buttonheight, padx=buttonpadx, pady=buttonpady, command=lambda number=button_text: button_click(number))
    button.grid(row=row, column=column, padx=spacingpadx, pady=spacingpady)

# Create the clear button
clear_button = tk.Button(window, text="C", width=buttonwidth, height=buttonheight, padx=buttonpadx, pady=buttonpady, command=button_clear)
clear_button.grid(row=4, column=2, padx=spacingpadx, pady=spacingpady)

# Create the equal button
equal_button = tk.Button(window, text="=", width=buttonwidth, height=buttonheight, padx=buttonpadx, pady=buttonpady, command=button_equal)
equal_button.grid(row=5, column=0, columnspan=4,sticky="nsew", padx=spacingpadx, pady=spacingpady)

# Start the main loop
window.mainloop()
