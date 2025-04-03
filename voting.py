import tkinter as tk
from tkinter import messagebox
import requests
from TwilioDemo.process_vote import process_vote

API_URL = "http://127.0.0.1:5000"  # Change this if your API is hosted elsewhere
time_left = 30  # Voting time limit in seconds

def submit_vote(username, party_name):
    """Submits the vote to the backend API."""
    response = requests.post(f"{API_URL}/submit_vote", json={"username": username, "party_name": party_name})
    data = response.json()

    # Then process the vote through Twilio
    process_vote(username)  
    
    if response.status_code == 200 and data.get("success"):
        messagebox.showinfo("Success", f"You have successfully voted for {party_name}!")
        root.destroy()  # Close the voting window
    else:
        messagebox.showerror("Error", data.get("message"))

def update_timer():
    """Updates the countdown timer and disables voting if time runs out."""
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        disable_voting()
        timer_label.config(text="Time's up!")

def disable_voting():
    """Disables all voting buttons after time runs out."""
    for btn in buttons:
        btn.config(state=tk.DISABLED)
    messagebox.showwarning("Time Over", "You ran out of time! Please restart.")

def on_enter(e):
    """Changes button background color on hover."""
    e.widget.config(bg="#d0ebff")  

def on_leave(e):
    """Restores button background color when the mouse leaves."""
    e.widget.config(bg=e.widget.default_bg)

def launch_voting(username):
    """Launches the voting interface."""
    global root, timer_label, buttons
    root = tk.Tk()
    root.title("E-Voting Portal")
    root.geometry("500x500")
    root.config(bg="#dff6ff")  

    # Title Label
    tk.Label(root, text="Choose Your Party", font=("Arial", 18, "bold"), bg="#dff6ff", fg="#222").pack(pady=10)
    
    # Timer Label
    timer_label = tk.Label(root, text=f"Time left: {time_left}s", font=("Arial", 14, "bold"), fg="red", bg="#dff6ff")
    timer_label.pack()

    # Party Names, Symbols, and Colors
    parties = ["COMPUTER", "IT", "AI&DS", "EXTC", "CHEMICAL"]
    symbols = ["🌙", "🔥", "⭐", "🚀", "🌿"]
    colors = ["#a8cce6", "#f5b7b1", "#a9dfbf", "#f9e79f", "#d2b4de"]  

    # Buttons Frame
    button_frame = tk.Frame(root, bg="#dff6ff")
    button_frame.pack(pady=20)

    buttons = []  # List to store button references

    # Create buttons dynamically
    for i, party in enumerate(parties):
        btn = tk.Button(button_frame, text=f"{party} {symbols[i]}", font=("Arial", 14, "bold"),
                        bg=colors[i], fg="black", width=15, height=2, relief="raised",
                        command=lambda party=party: submit_vote(username, party))  
        btn.default_bg = colors[i]  
        btn.bind("<Enter>", on_enter)  
        btn.bind("<Leave>", on_leave)  
        btn.pack(pady=5)
        buttons.append(btn)

    update_timer()  
    root.mainloop()
