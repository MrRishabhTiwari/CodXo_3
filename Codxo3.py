import tkinter as tk
import string
import secrets

class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")
        self.window.geometry("450x300")

        self.character_sets_var = tk.StringVar(self.window)
        self.character_sets_var.set("Alphanumeric")

        self.character_sets_label = tk.Label(window, text="Choose character sets:")
        self.character_sets_label.pack()

        self.character_sets_menu = tk.OptionMenu(window, self.character_sets_var, "Alphanumeric", "Alphabets", "Numbers", "Special Characters")
        self.character_sets_menu.pack()

        self.length_label = tk.Label(window, text="Enter password length:")
        self.length_label.pack()

        self.length_entry_box = tk.Entry(window)
        self.length_entry_box.pack()

        self.generate_button = tk.Button(window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_labels = []
        for i in range(10):
            label = tk.Label(window, text="")
            label.pack()
            self.password_labels.append(label)

    def generate_password(self):
        try:
            password_length = int(self.length_entry_box.get())
            character_sets = self.character_sets_var.get()
            passwords = []
            if character_sets == "Alphanumeric":
                data = string.ascii_letters + string.digits
            elif character_sets == "Alphabets":
                data = string.ascii_letters
            elif character_sets == "Numbers":
                data = string.digits
            else:
                data = string.punctuation
            for _ in range(10):
                password = ''.join(secrets.choice(data) for _ in range(password_length))
                passwords.append(password)
            for i, password in enumerate(passwords):
                self.password_labels[i].config(text=f"Password {i+1}: {password}")
        except ValueError:
            self.password_labels[0].config(text="Please enter a valid password length")

if __name__ == "__main__":
    window = tk.Tk()
    password_generator = PasswordGenerator(window)
    window.mainloop()
