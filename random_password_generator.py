import tkinter as tk
import secrets
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 1:
        password_result.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(password_length))
    password_result.set(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and set a variable for displaying the generated password
password_result = tk.StringVar()
password_result.set("")

# Create and set a label to display the password
password_label = tk.Label(root, textvariable=password_result)
password_label.pack(pady=10)

# Create a label and entry for password length input
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Run the GUI main loop
root.mainloop()
