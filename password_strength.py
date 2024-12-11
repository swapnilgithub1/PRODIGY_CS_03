Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re


def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[@$!%*?&#]', password) is not None
    # Strength levels
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    # Assessing strength
    strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])
    # Ensure strength_score doesn't exceed the index range of strength_levels
    strength_score = min(strength_score, len(strength_levels) - 1)
    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
...     if not number_criteria:
...         feedback.append("Password should include at least one number.")
...     if not special_criteria:
...         feedback.append("Password should include at least one special character (@, $, !, %, *, ?, & or #).")
...     return strength_levels[strength_score], feedback
... 
>>> 
>>> def check_password_strength():
...     password = password_entry.get()
...     strength, feedback = assess_password_strength(password)
...     result_label.config(text=f"Password Strength: {strength}")
...     feedback_text.delete('1.0', tk.END)
...     if feedback:
...         feedback_text.insert(tk.END, "Feedback:\n")
...         for item in feedback:
...             feedback_text.insert(tk.END, f"- {item}\n")
... 
...             
>>> 
>>> # Create the main window
>>> root = tk.Tk()
>>> root.title("Password Strength Checker")
''
>>> 
>>> # Create and place widgets
>>> ttk.Label(root, text="Enter your password:").grid(row=0, column=0, padx=10, pady=10)
>>> password_entry = ttk.Entry(root, width=50, show='*')
>>> password_entry.grid(row=0, column=1, padx=10, pady=10)
>>> 
>>> ttk.Button(root, text="Check Strength", command=check_password_strength).grid(row=1, column=0, columnspan=2, pady=10)
>>> 
>>> result_label = ttk.Label(root, text="Password Strength: ")
>>> result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
>>> 
>>> feedback_text = tk.Text(root, width=60, height=10)
>>> feedback_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
>>> 
>>> # Run the application #root.mainloop()
>>> root.mainloop()
