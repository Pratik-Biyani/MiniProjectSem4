import csv
from send_whatsapp import send_whatsapp

def process_vote(voter_id):
  
    with open("voters.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["VoterID"] == voter_id:
                phone_number = row["Phone"]
                voter_name = row["Name"]
                
                # Send WhatsApp confirmation
                send_whatsapp(phone_number, voter_name)
                return f"Vote registered successfully for {voter_name}."
    
    return "❌ Voter not found."

# Example usage: Ask user for voter ID and process their vote
if __name__ == "__main__":
    voter_id = input("Enter Voter ID: ")
    print(process_vote(voter_id))
