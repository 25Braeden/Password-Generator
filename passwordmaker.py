"""
This module contains a password maker tool allows users to save website
login details on their computer. Please consult the README to understand
the program.

Usage:
    python passwordmaker.py

Author:
    25braeden 25baudlin@msjnet.net

"""

import random
import string
import time

print("Welcome to the password maker tool")
time.sleep(2)
print("Would you like to generate full login detail or just a password?")
time.sleep(2)

decision = input("(1 for full login, 2 for just password): ")

while decision not in ['1', '2']:
    print("Invalid input, please enter either '1' or '2'")
    time.sleep(2)
    decision = input("Select option '1' or '2': ")

if decision == '1':
    while True:
        website = input("Enter the name of the website you are accessing: ")   
        email = input("Enter an email address to save with the password: ")
        length = int(input("How many characters should your password be: "))

        while length <= 7:
            print("password length must be at least 8 characters")
            time.sleep(2)
            length = int(input("How long would you like your password to be: "))

        ALPHABET = string.ascii_letters + string.digits + string.punctuation

        PASSWORD = ''.join(random.choice(ALPHABET) for i in range (length))

        print("Generating a secure password")
        time.sleep(2)
        print("Your secure password is:", PASSWORD)
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write(f"Website: {website}\nEmail: {email}\nPassword: {PASSWORD}\n\n")
        print("Your secure login details are:\n" + website + "\n" + email + "\n" + PASSWORD)
        time.sleep(2)
        print("Would you like to generate another login?")
        time.sleep(2)
        generate_another = input("(Y/N): ")
        if generate_another.lower() == 'y':
            continue
        else:
            break

elif decision == '2':
    while True:
        length = int(input("How many characters should your password be: "))

        while length <= 7:
            print("Password needs to be at least 8 characters")
            time.sleep(2)
            length = int(input("How long would you like your password to be: "))
            
        ALPHABET = string.ascii_letters + string.digits + string.punctuation
        PASSWORD = ''.join(random.choice(ALPHABET) for i in range (length))

        print("Generating a secure password")
        time.sleep(2)
        print("Your secure password is:", PASSWORD)
        time.sleep(2)
        print("Would you like to generate another password?")
        generate_another = input("(Y/N): ")
        if generate_another.lower() == 'n':
            break
time.sleep(2)         
print("Thanks for using my password generator!\n Stay safe!")
