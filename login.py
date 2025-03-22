import tkinter as tk
from tkinter import messagebox

# Function to validate login
def login():
    global entry_username, entry_password
    username = entry_username.get()
    password = entry_password.get()
    
    # Define valid users
    valid_users = {
        "admin": "password",
        "user1": "pass123",
        "user2": "mypassword"
    }
    
    if username in valid_users and valid_users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Function for forgot password
def forgot_password():
    contact_info = "Please contact support at support@example.com or call +123456789 to reset your password."
    messagebox.showinfo("Forgot Password", contact_info)

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

# Create login frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=30)

# Username Label & Entry
label_username = tk.Label(frame, text="Username:", font=("Arial", 12))
label_username.grid(row=0, column=0, pady=5, padx=5)
entry_username = tk.Entry(frame, font=("Arial", 12))
entry_username.grid(row=0, column=1, pady=5, padx=5)

# Password Label & Entry
label_password = tk.Label(frame, text="Password:", font=("Arial", 12))
label_password.grid(row=1, column=0, pady=5, padx=5)
entry_password = tk.Entry(frame, font=("Arial", 12), show="*")
entry_password.grid(row=1, column=1, pady=5, padx=5)

# Login Button
button_login = tk.Button(frame, text="Login", font=("Arial", 12), command=login, bg="blue", fg="white")
button_login.grid(row=2, columnspan=2, pady=10)

# Forgot Password Button
button_forgot = tk.Button(frame, text="Forgot Password?", font=("Arial", 10), command=forgot_password, fg="red", borderwidth=0)
button_forgot.grid(row=3, columnspan=2, pady=5)

# Run the application
root.mainloop()