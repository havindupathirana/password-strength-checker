# 🔐 Password Strength Checker

A web-based password strength checker built with Python and Flask. Evaluates passwords against multiple security criteria and provides real-time feedback.

## Features

- Real-time password strength evaluation
- Checks for length, uppercase, lowercase, numbers, special characters
- Detects repeated characters and common patterns
- Dark-themed hacker-style UI
- Simple REST API backend

## Tech Stack

- Python 3
- Flask
- HTML/CSS/JavaScript

## Installation

1. Clone the repository
```bash
   git clone https://github.com/havindupathirana/password-strength-checker.git
   cd password-strength-checker
```

2. Install dependencies
```bash
   pip3 install -r requirements.txt
```

3. Run the app
```bash
   python3 app.py
```

4. Open your browser and go to
   ```
   http://localhost:5000
   ```
## How It Works

Passwords are scored based on:

| Check | Points |
|---|---|
| Length 8-11 chars | +1 |
| Length 12+ chars | +2 |
| Uppercase letter | +1 |
| Lowercase letter | +1 |
| Number | +1 |
| Special character | +2 |
| Repeated characters | -1 |
| Common patterns | -1 |

| Score | Strength |
|---|---|
| 0-2 | Weak |
| 3-4 | Medium |
| 5+ | Strong |

## Project Structure
## Author

Havindu Pathirana - [GitHub](https://github.com/havindupathirana)
