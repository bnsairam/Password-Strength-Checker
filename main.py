
---

### `password_checker.py` Code

Below is the implementation of `password_checker.py` that matches the described functionality, using `re`, `string`, and `secrets` to analyze password strength, calculate a score, and provide suggestions.

```python
import re
import string
import secrets
import math

def calculate_entropy(password):
    """Calculate simplified Shannon entropy based on character set size."""
    char_set_size = 0
    if any(c.islower() for c in password):
        char_set_size += 26
    if any(c.isupper() for c in password):
        char_set_size += 26
    if any(c.isdigit() for c in password):
        char_set_size += 10
    if any(c in string.punctuation for c in password):
        char_set_size += 32
    if char_set_size == 0:
        return 0
    entropy = len(password) * math.log2(char_set_size)
    return min(entropy, 100)  # Cap entropy contribution

def check_password_strength(password):
    """Analyze password and return strength score and feedback."""
    score = 0
    feedback = []

    # Check length
    length = len(password)
    if length < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    elif length >= 12:
        score += 30
    else:
        score += length * 2

    # Check character variety
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")
    if re.search(r"\d", password):
        score += 15
    else:
        feedback.append("Add digits.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15
    else:
        feedback.append("Add special characters.")

    # Check for weak patterns
    if re.search(r"(.)\1{2,}", password):  # Repeated characters (e.g., aaa)
        score -= 20
        feedback.append("Avoid repeated characters.")
    if re.search(r"123|abc|qwerty", password, re.IGNORECASE):  # Common sequences
        score -= 20
        feedback.append("Avoid predictable sequences like '123' or 'qwerty'.")
    if re.search(r"password|admin|user", password, re.IGNORECASE):  # Common words
        score -= 30
        feedback.append("Avoid common words like 'password'.")

    # Add entropy contribution
    entropy = calculate_entropy(password)
    score += int(entropy / 5)  # Scale entropy to contribute to score

    # Ensure score is between 0 and 100
    score = max(0, min(100, score))

    # Determine strength label
    if score >= 80:
        strength = "Strong"
    elif score >= 60:
        strength = "Moderate"
    else:
        strength = "Weak"

    return score, strength, feedback

def generate_strong_password(length=12):
    """Generate a secure random password using secrets."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    print("🔐 Password Strength Checker")
    print("Enter a password to check its strength (or 'quit' to exit).")
    
    while True:
        password = input("Enter password: ")
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        score, strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {score}/100 ({strength})")
        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f"- {item}")
        if score < 80:
            suggested_password = generate_strong_password()
            print(f"Suggested Password: {suggested_password}")

if __name__ == "__main__":
    main()
