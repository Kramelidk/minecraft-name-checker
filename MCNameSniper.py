import requests
import random
import string
import time
import sys
import os
from colorama import Fore
from clint.textui import colored
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("by kramel")

print("")
print(colored.blue("░██████╗███╗░░██╗██╗██████╗░███████╗██████╗░"))
print(colored.blue("██╔════╝████╗░██║██║██╔══██╗██╔════╝██╔══██"))
print(colored.blue("╚█████╗░██╔██╗██║██║██████╔╝█████╗░░██████╔╝"))
print(colored.blue("░╚═══██╗██║╚████║██║██╔═══╝░██╔══╝░░██╔══██╗"))
print(colored.blue("██████╔╝██║░╚███║██║██║░░░░░███████╗██║░░██║"))
print(colored.blue("╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝"))
print("")
print(colored.blue("Made by") + colored.yellow(" kramel"))
print("")
print(colored.blue("Note: the usernames are generated every second it cannot go faster because it will get rate limited quickly."))
print("")
genNumbers = input("Include numbers in the username? (y/n): ")
print("")
howManyCharacters = int(input("How many characters? enter a number: "))
print("")

def generate_random_username():
    if genNumbers == "y":
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(howManyCharacters))
    elif genNumbers == "n":
        characters = string.ascii_lowercase
        return ''.join(random.choice(characters) for _ in range(howManyCharacters))
    else:
        print("Error: Invalid input. Please enter 'y' or 'n'.")

def check_minecraft_username(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    time.sleep(1)
    response = requests.get(url)
    
    if response.status_code == 200:
        return False
    elif response.status_code == 204:
        return True
    elif response.status_code == 404:
        return True
    else:
        print(colored.red("An error occurred while checking a username... Could be getting rate limited."))
        return None

def main():
    found_available = False
    
    while not found_available:
        username = generate_random_username()
        
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        print(colored.red(f'Checking username: {username}'), end="\r")
        available = check_minecraft_username(username)
        
        if available is None:
            print("Please try again later.")
            break

        if available:
            print(colored.green(f"The username '{username}' is available!"))
            found_available = True

            if found_available is True:
                print(colored.green("Continuing in 2 seconds."), end="\r")
                time.sleep(2)
                found_available = False
                

if __name__ == "__main__":
    main()
