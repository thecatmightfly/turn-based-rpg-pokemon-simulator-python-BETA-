import os
import time
from playsound import playsound

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def beginning():
    clear_screen()
    name = input("What is your name? \n")
    clear_screen()
    print(f"Hello {name}, welcome to the world of Pokemon!")
    time.sleep(0.25)
    playsound("start_noise.wav")
    time.sleep(1)
    clear_screen()
    print("Please choose your starter Pokemon: \n1. Bulbasaur \n2. Charmander \n3. Squirtle \n")
    starter_selection = input("Type the number of your choice: \n")
    if starter_selection == "1":
        player_pokemon = "Bulbasaur"
    elif starter_selection == "2":
        player_pokemon = "Charmander"
    elif starter_selection == "3":
        player_pokemon = "Squirtle"
    else:
        print("Invalid selection, please try again in a few seconds.")
        time.sleep(3)
        clear_screen()
        beginning()
        return

def fight_system():
    clear_screen()
    

def fight_choose():
    clear_screen()
    print("A wild Pokemon appeared!")
    time.sleep(1)
    print("What will you do?")
    action = input("1. Fight \n2. Run \n")
    if action == "1":
        print("You chose to fight!")
        fight_system()
    elif action == "2":
        print("You ran away safely!")
        time.sleep(1)
        clear_screen()
    else:
        print("Invalid selection, please try again in a few seconds.")
        time.sleep(3)
        clear_screen()
        fight_system()

print("Welcome to pokemon battle simulator!")
menu_selection = input("Type one of the following to start your adventure: \n1. Start New Game \n2. Exit \n")
if menu_selection == "1":
    beginning()
elif menu_selection == "2":
    exit()
else:
    print("Invalid selection, please try again in a few seconds.")
    time.sleep(3)
    clear_screen()
