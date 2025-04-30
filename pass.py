import tkinter as tk
import secrets
import string
from PIL import Image, ImageTk 
def generate_password():
    
    if not length_entry.get().isdigit() or int(length_entry.get()) <= 7:
        result_label.config(text="Please enter a valid length.")
        return 
    else:

        length = int(length_entry.get())  
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        result_label.config(text=password)
        return password
    
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")
window.resizable(False, False)

title_label = tk.Label(window, text="Generate a Secure Password", font=("Goudy Old Style", 16), fg="darkblue")
title_label.pack(pady=10)

length_label = tk.Label(window, text="Enter Password Length:", font=("Arial", 12))
length_label.pack()
length_entry = tk.Entry(window, font=("Arial", 12), justify='center')
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate", font=("Arial", 12, "bold"), bg="black", fg="white", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Courier", 14), fg="darkblue")
result_label.pack(pady=10)

window.mainloop()
