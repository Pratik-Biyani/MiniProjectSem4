import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:5000"  # Flask server URL
time_left = 30  # Timer countdown

def submit_vote(username, party_name):
    response = requests.post(f"{API_URL}/submit_vote", json={"username": username, "party_name": party_name})
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        messagebox.showinfo("Success", f"You voted for {party_name}!")
        root.destroy()  # Close voting window after voting
    else:
        messagebox.showerror("Error", data.get("message"))

def update_timer():
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left}s")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        disable_voting()
        timer_label.config(text="Time's up!")

def disable_voting():
    for btn in buttons:
        btn.config(state=tk.DISABLED)
    messagebox.showwarning("Time Over", "You ran out of time! Please restart.")

def on_enter(e):
    e.widget.config(bg="#d0ebff")  # Lighter hover color

def on_leave(e):
    e.widget.config(bg=e.widget.default_bg)

def launch_voting(username):
    global root, timer_label, buttons
    root = tk.Tk()
    root.title("E-Voting Portal")
    root.geometry("500x500")
    root.config(bg="#dff6ff")  # Light Blue Background

    tk.Label(root, text="Choose Your Party", font=("Arial", 18, "bold"), bg="#dff6ff", fg="#222").pack(pady=10)
    
    timer_label = tk.Label(root, text=f"Time left: {time_left}s", font=("Arial", 14, "bold"), fg="red", bg="#dff6ff")
    timer_label.pack()

    parties = ["COMPUTER", "IT", "AI&DS", "EXTC", "CHEMICAL"]
    symbols = ["🌙", "🔥", "⭐", "🚀", "🌿"]
    colors = ["#a8cce6", "#f5b7b1", "#a9dfbf", "#f9e79f", "#d2b4de"]  # Lighter button colors

    button_frame = tk.Frame(root, bg="#dff6ff")
    button_frame.pack(pady=20)

    buttons = []
    for i, party in enumerate(parties):
        btn = tk.Button(button_frame, text=f"{party} {symbols[i]}", font=("Arial", 14, "bold"),
                        bg=colors[i], fg="black", width=15, height=2, relief="raised",
                        command=lambda p=party: submit_vote(username, p))
        btn.default_bg = colors[i]
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(pady=5)
        buttons.append(btn)

    update_timer()  # Start countdown
    root.mainloop()
