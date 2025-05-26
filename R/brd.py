
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
from tkinter import messagebox
from random import choice
# ------------------ CONFIG -------------------
my_photo_path = r"C:\Users\hp\OneDrive\Pictures\Screenshot_20240613_000756.jpg"  # Use raw string
friend_photo_path = r"C:\Users\hp\OneDrive\Pictures\friend_photo.jpg"  # Use raw string

# ---------------------------------------------

# Create window
root = tk.Tk()
root.title("🎉 Birthday Surprise")
root.geometry("800x600")
root.configure(bg="black")

# Image label
img_label = tk.Label(root, bg="black")
img_label.pack(pady=20)

# Message label
msg_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="black", fg="white")
msg_label.pack(pady=20)

# Colors for animation
colors = ["red", "blue", "green", "orange", "purple", "magenta", "cyan", "gold"]

# Load and display image helper
def show_image(path):
    img = Image.open(path)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo

# Animate label colors
def animate_label():
    for _ in range(20):
        msg_label.config(fg=choice(colors))
        time.sleep(0.3)

# Surprise logic
def show_surprise():
    name = name_entry.get()
    if not name.strip():
        messagebox.showerror("Error", "Please enter your friend's name")
        return

    start_button.config(state="disabled")
    msg_label.config(text="🎁 Ready for a surprise?")

    # Step 1: Show your photo
    show_image(my_photo_path)
    msg_label.config(text="🎉 It's your turn!")
    animate_label()  # Animate your photo
    time.sleep(2)

    # Step 2: Show friend's photo + message
    show_image(friend_photo_path)
    msg_label.config(text=f"🎂 Happy Birthday, {name}! 🎉\nWishing you a joyful year ahead!")
    animate_label()  # Animate friend's photo

# Start button clicked
def start_surprise_thread():
    threading.Thread(target=show_surprise).start()

# UI elements
title = tk.Label(root, text="🎁 Enter Friend's Name:", font=("Arial", 16), bg="black", fg="white")
title.pack(pady=5)

name_entry = tk.Entry(root, font=("Arial", 16), justify="center", width=30)
name_entry.pack(pady=5)

start_button = tk.Button(root, text="🎉 Start Surprise 🎉", font=("Arial", 14, "bold"), bg="green", fg="white", command=start_surprise_thread)
start_button.pack(pady=10)

root.mainloop()






















