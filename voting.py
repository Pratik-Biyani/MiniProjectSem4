import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:5000"  # Flask server URL

def submit_vote(username, party_name):
    response = requests.post(f"{API_URL}/submit_vote", json={"username": username, "party_name": party_name})
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        messagebox.showinfo("Success", f"You voted for {party_name}!")
        root.destroy()  # Close voting window after voting
    else:
        messagebox.showerror("Error", data.get("message"))

def launch_voting(username):
    global root
    root = tk.Tk()
    root.title("E-Voting Portal")
    root.geometry("400x400")

    tk.Label(root, text="Choose Your Party", font=("Arial", 16)).pack(pady=10)

    parties = ["COMPUTER", "IT", "AI&DS", "EXTC", "CHEMICAL"]
    symbols = ["🌙", "🔥", "⭐", "🚀", "🌿"]

    for i, party in enumerate(parties):
        btn = tk.Button(root, text=f"{party} {symbols[i]}", font=("Arial", 14), command=lambda p=party: submit_vote(username, p))
        btn.pack(pady=5)

    root.mainloop()
