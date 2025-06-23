import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Define buttons
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 0), ('+', 4, 1), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 1), ('=', 5, 2),
    ('Clear', 6, 0)
]

# Create buttons in loop
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=30, pady=20, command=button_equal).grid(row=row, column=col)
    elif text == 'Clear':
        tk.Button(root, text=text, padx=79, pady=20, command=button_clear).grid(row=row, column=col, columnspan=2)
    else:
        tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Run the main loop
root.mainloop()