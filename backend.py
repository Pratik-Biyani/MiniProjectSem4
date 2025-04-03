from flask import Flask, request, jsonify
import sqlite3
from bcrypt import checkpw

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    security_ans1 = data.get("security_ans1").lower().strip()
    security_ans2 = data.get("security_ans2").lower().strip()

    conn = sqlite3.connect("evoting.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password, security_ans1, security_ans2, role, voted FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    
    conn.close()

    if not user or not checkpw(password.encode(), user[0].encode()):
        return jsonify({"success": False, "message": "Invalid credentials!"})

    if user[3] == "Voter" and user[4] == 1:
        return jsonify({"success": False, "message": "You have already voted!"})

    if user[1] != security_ans1 or user[2] != security_ans2:
        return jsonify({"success": False, "message": "Incorrect security answers!"})

    return jsonify({"success": True, "message": "Login successful!", "role": user[3]})

@app.route("/submit_vote", methods=["POST"])
def submit_vote():
    data = request.json
    username = data.get("username")
    party_name = data.get("party_name")  # Get party_name from request

    conn = sqlite3.connect("evoting.db")
    cursor = conn.cursor()

    # Check if user has already voted
    cursor.execute("SELECT voted FROM users WHERE username=?", (username,))
    voted = cursor.fetchone()

    if voted and voted[0] == 1:
        conn.close()
        return jsonify({"success": False, "message": "You have already voted!"})

    # Update user's voting status
    cursor.execute("UPDATE users SET voted = 1 WHERE username=?", (username,))
    cursor.execute("UPDATE voters SET has_voted = 'Yes' WHERE username=?", (username,))

    # Update vote count for the selected party
    cursor.execute("UPDATE votes2 SET vote_count = vote_count + 1 WHERE party_name=?", (party_name,))

    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": "Vote submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
