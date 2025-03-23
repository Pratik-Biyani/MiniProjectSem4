import tkinter as tk
from tkinter import messagebox
import requests
import voting  # Import the voting system after login

API_URL = "http://127.0.0.1:5000"  # Flask server URL

def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return

    response = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  # Close login window
        voting.launch_voting(username)  # Open voting system
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

# Create Login Window
root = tk.Tk()
root.title("E-Voting Login")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
