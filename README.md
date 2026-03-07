# Password Checker & Generator 

This project has two main functions:

1. It asks for a password and generates a score out of 10 based on how strong the password is
2. It can generate a random password and allows the user to decide the length and what characters are included

It also has other sub functions such as saving the password and its score into a file with a timestamp.

---

## Features

- Scores passwords out of 10 based on length, complexity and common password detection
- Gives specific advice on how to improve weak passwords
- Generates random passwords with customisable character options
- Allows user to check the strength of a generated password immediately
- Saves password history with timestamps to a file
- Colour coded terminal output
- Mode switching between checker and generator

---

## How to Run

Make sure you have Python 3.10+ installed.

Install the required modules:

```
pip install termcolor colorama
```

Run the program:

```
python password_checker.py
```

---

## How It Works

### Password Checker

Enter a password and the program will check it against the following criteria:

- Length (longer = higher score)
- Contains uppercase letters
- Contains lowercase letters
- Contains numbers
- Contains special characters
- Not a common password (checks against a list of 28 common passwords)

The score is out of 10. You can then change your password, view it, or switch to the generator.

### Password Generator

Choose your password length and which character types to include:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

The generator evenly distributes characters across the chosen types, then shuffles them randomly. You can immediately check the strength of the generated password.

---

## Scoring System

| Score | Rating |
| --- | --- |
| 10 | Perfect password |
| 9 | Almost perfect |
| 8 | Very strong |
| 7 | Strong |
| 6 | Not bad |
| 5 | Fine |
| Below 5 | Weak |

---

## What I Learned

1. Object Oriented Programming — private attributes, property decorators and setters
2. Error handling with try/except
3. File handling — reading and writing to files
4. Using the random and datetime modules
5. The importance of strong passwords and what makes them secure

---

## Technologies Used

- Python 3.10+
- termcolor
- colorama
- OOP with two classes (PasswordChecker and PasswordGenerator)
- Python match/case statement
- datetime for timestamps
- random and string modules

---

## Possible Improvements

1. Encrypt saved passwords for better security
2. Add a decryption key to read encrypted password history
3. Display saved passwords ordered by date created
4. Add an estimate of how long it would take to crack a password
5. Add a password cracker feature

---

## Note

This tool saves passwords in plain text to password_history.txt. This is for educational purposes only. In a real application, passwords should never be stored in plain text.
