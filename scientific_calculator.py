import tkinter as tk
from math import *

# Function to update the display with the button's text
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to evaluate the expression in the display
def evaluate_expression():
    try:
        # Replace certain symbols for compatibility with Python's math functions
        result = eval(display.get().replace('^', '**').replace('√', 'sqrt'))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to add scientific functions like sin, cos, etc.
def add_scientific_function(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value + "(")

# Setting up the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="lightgray")

# Setting up the outer frame
outer_frame = tk.Frame(root, bg="black", bd=10)
outer_frame.pack(pady=20)

# Setting up the inner frame
inner_frame = tk.Frame(outer_frame, bg="lightgray")
inner_frame.pack()

# Setting up the display
display = tk.Entry(inner_frame, font=("Arial", 24), borderwidth=5, relief=tk.RIDGE, justify='right')
display.pack(pady=20, padx=10, fill="x")

# Defining button text and layout
buttons = [
    '7', '8', '9', '/', '√', 'sin', 'cos', 'tan',
    '4', '5', '6', '*', '^', '(', ')', 'log',
    '1', '2', '3', '-', 'exp', 'asin', 'acos', 'atan',
    'C', '0', '.', '+', 'pi', 'e', 'In', '='
]

# Creating buttons and placing them in the window
button_frame = tk.Frame(inner_frame, bg="lightgray")
button_frame.pack(pady=20)
row_val = 0
col_val = 0

for button in buttons:
    if button in ['sin', 'cos', 'tan', 'log', 'exp', 'asin', 'acos', 'atan', '√', 'In']:
        action = lambda x=button: add_scientific_function(x)
    else:
        action = lambda x=button: button_click(x)
    
    if button == "=":
        btn = tk.Button(button_frame, text=button, font=("Arial", 18), command=evaluate_expression, bg="orange", fg="white")
    elif button == "C":
        btn = tk.Button(button_frame, text=button, font=("Arial", 18), command=clear_display, bg="red", fg="white")
    else:
        btn = tk.Button(button_frame, text=button, font=("Arial", 18), command=action, bg="lightblue", fg="black")
    
    btn.grid(row=row_val, column=col_val, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 7:
        col_val = 0
        row_val += 1

# Configuring grid layout for responsive resizing
for i in range(8):
    button_frame.grid_columnconfigure(i, weight=1)

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

root.mainloop()
