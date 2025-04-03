import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import face_recognition

# Initialize the Tkinter window
root = tk.Tk()
root.title("Face Recognition App")

# OpenCV video capture (Webcam)
cap = cv2.VideoCapture(0)

# Load a known image and encode it
# You can replace this with any image of a known person
known_image = face_recognition.load_image_file("C:/Users/Pratik/Desktop/Coding/EvotingPortalSem4/login_python/face/pratik1.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# List of known face encodings and their names
known_face_encodings = [known_face_encoding]
known_face_names = ["Known Person"]

# Function to update the frame
def update_frame():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Convert frame from BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = frame[:, :, ::-1]

        # Detect faces and their encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the face encoding with the known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Draw rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Draw label with the name
            cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        # Convert the frame to ImageTk format for Tkinter display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(img)

        # Update the image on the Tkinter Label widget
        panel.config(image=img)
        panel.image = img

    # Call this function again after 10 milliseconds
    root.after(10, update_frame)

# Tkinter label to display the webcam feed
panel = tk.Label(root)
panel.pack()

# Start updating frames
update_frame()

# Start the Tkinter event loop
root.mainloop()

# Release the capture when the window is closed
cap.release()
