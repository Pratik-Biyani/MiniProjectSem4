import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import face_recognition

# Initialize the Tkinter window
root = tk.Tk()
root.title("E-Voting Portal - Face Recognition Authentication")
root.geometry("800x600")
root.config(bg="#f5f5f5")

# OpenCV video capture (Webcam)
cap = cv2.VideoCapture(0)

# Status variable
status_text = tk.StringVar()
status_text.set("Status: Waiting for face detection...")

# Function to update the frame
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert frame from BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = frame[:, :, ::-1]

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame)

        # Draw rectangle around faces
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Convert the frame to ImageTk format for Tkinter display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(img)

        # Update the image on the Tkinter Label widget
        panel.config(image=img)
        panel.image = img

        # Update status based on face detection
        if len(face_locations) > 0:
            status_text.set("Status: Face detected! Ready to vote.")
        else:
            status_text.set("Status: No face detected. Please try again.")

    # Call this function again after 10 milliseconds
    root.after(10, update_frame)

# Start the voting process
def start_voting(username):
    # Check if a face is detected before proceeding
    if "Ready to vote." in status_text.get():
        messagebox.showinfo("Authentication", "Face authentication successful. You can now vote!")
        # Proceed with the voting process (Placeholder)
        print(f"Voting process started for {username}.")
        # Assuming you have a 'voting.py' file with a 'launch_voting' function.
        try:
            from voting import launch_voting
            launch_voting(username)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Authentication Failed", "No face detected. Please ensure your face is clearly visible.")

# Stop the voting process (Stop face recognition)
def stop_voting():
    messagebox.showinfo("Voting Stopped", "Face recognition stopped. Thank you for using the E-Voting Portal.")
    cap.release()
    root.quit()  # Close the Tkinter window

# Instructions Label
instructions = tk.Label(root, text="Please position your face in front of the camera for authentication.", 
                        font=("Helvetica", 14), bg="#f5f5f5", wraplength=750)
instructions.pack(pady=10)

# Status Label
status_label = tk.Label(root, textvariable=status_text, font=("Helvetica", 12), bg="#f5f5f5")
status_label.pack(pady=10)

# Username Entry Field
username_label = tk.Label(root, text="Enter Username:", font=("Helvetica", 12), bg="#f5f5f5")
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Helvetica", 12))
username_entry.pack(pady=5)

# Start/Stop Buttons Frame
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=20)

# Start Voting Button
start_button = tk.Button(button_frame, text="Start Voting", font=("Helvetica", 14), bg="#4CAF50", fg="white", 
                         command=lambda: start_voting(username_entry.get()), width=15)
start_button.grid(row=0, column=0, padx=20)

# Stop Voting Button
stop_button = tk.Button(button_frame, text="Stop Voting", font=("Helvetica", 14), bg="#f44336", fg="white", 
                        command=stop_voting, width=15)
stop_button.grid(row=0, column=1, padx=20)

# Tkinter label to display the webcam feed
panel = tk.Label(root)
panel.pack(pady=20)

# Start updating frames
update_frame()

# Start the Tkinter event loop
root.mainloop()

# Ensure the capture is released when the window is closed
cap.release()
