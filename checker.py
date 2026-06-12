import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Track core requirements separately
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))
    has_length = len(password) >= 12

    # Length check
    if len(password) < 8:
        feedback.append("Too short — use at least 8 characters")
    elif len(password) < 12:
        score += 1
        feedback.append("Consider using 12+ characters for better security")
    else:
        score += 2

    # Uppercase check
    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase check
    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Number check
    if has_number:
        score += 1
    else:
        feedback.append("Add at least one number")

    # Special character check
    if has_special:
        score += 2
    else:
        feedback.append("Add at least one special character e.g. !@#$%")

    # Repeated characters check
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("Avoid repeated characters e.g. aaa or 111")

    # Common patterns check
    patterns = ['1234', 'abcd', 'qwerty', 'asdf', '0000', '1111', 'password']
    for pattern in patterns:
        if pattern in password.lower():
            score -= 1
            feedback.append(f"Avoid common patterns like '{pattern}'")
            break

    # Strong requires ALL core checks to pass
    all_core = has_upper and has_lower and has_number and has_special and has_length

    if score <= 2 or not all_core:
        if score > 2 and not all_core:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Weak"
            color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    if not feedback:
        feedback.append("Great password!")

    return {
        "score": score,
        "strength": strength,
        "color": color,
        "feedback": feedback
    }
