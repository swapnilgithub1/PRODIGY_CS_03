Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[@$!%*?&#]', password) is not None

...     # Strength levels
...     strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
... 
...     # Assessing strength
...     strength_score = sum([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria])
...     
...     # Ensure strength_score doesn't exceed the index range of strength_levels
...     strength_score = min(strength_score, len(strength_levels) - 1)
... 
...     # Feedback messages
...     feedback = []
...     if not length_criteria:
...         feedback.append("Password should be at least 8 characters long.")
...     if not lowercase_criteria:
...         feedback.append("Password should include at least one lowercase letter.")
...     if not uppercase_criteria:
...         feedback.append("Password should include at least one uppercase letter.")
...     if not number_criteria:
...         feedback.append("Password should include at least one number.")
...     if not special_criteria:
...         feedback.append("Password should include at least one special character (@, $, !, %, *, ?, & or #).")
... 
...     return strength_levels[strength_score], feedback
... 
... def main():
...     # Replace input with a hardcoded password for testing
...     password = "ABCd123!"  # Modify this for testing
...     strength, feedback = assess_password_strength(password)
...     print(f"Password Strength: {strength}")
...     if feedback:
...         print("Feedback:")
...         for item in feedback:
...             print(f"- {item}")
... 
... if __name__ == "__main__":