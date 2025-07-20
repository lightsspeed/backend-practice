#ask the user if they want to generate a password
#if yes then ask for password length
#generate password
#if No response then quit the program

import random
import string

print("Welcome to Password Generator Program")

characters = list(string.ascii_letters + string.digits + "!@#$%^&*():;,.<>/?|=+-_")

def pass_gen():
    while True:
        try:
            password_length = int(input("Specify Password Length: "))
            if password_length <= 0:
                print("Please enter a positive number for password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")

    random.shuffle(characters)
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(password)

while True:
    option = input("Do you want to generate a password ? (y/n):")

    if option == "y":
        pass_gen()
        break
    elif option == "n":
        print("program ended")
        quit()
    else:
        print("Input a valid response")
