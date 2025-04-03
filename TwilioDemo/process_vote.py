import csv
from TwilioDemo.send_whatsapp import send_whatsapp

def process_vote(username):
    """
    Reads voter details from 'voters.csv' and sends a WhatsApp confirmation.
    """
    with open("voters.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == username:
                phone_number = row["Phone"]  # Ensure it's in "whatsapp:+91XXXXXXXXXX" format
                voter_name = row["Name"]
                
                # Send WhatsApp confirmation
                send_whatsapp(phone_number, voter_name)
                return f"✅ Vote registered successfully for {voter_name}."
    
    return "❌ Voter not found."

# Run the script
if __name__ == "__main__":
    voter_id = input("Enter Voter ID: ")
    print(process_vote(voter_id))
