from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user credentials (username: password)
users = {"user1": "password123", "user2": "securepass"}

# Store votes in a dictionary (username: party)
votes = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username, password = data.get("username"), data.get("password")

    if users.get(username) == password:
        return jsonify({"success": True, "message": "Login successful"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    data = request.json
    username, party_name = data.get("username"), data.get("party_name")

    if username in votes:
        return jsonify({"success": False, "message": "You have already voted!"}), 400

    votes[username] = party_name
    return jsonify({"success": True, "message": f"Vote for {party_name} submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
