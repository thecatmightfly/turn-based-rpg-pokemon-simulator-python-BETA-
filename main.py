import os
import time
import json
import random
from playsound import playsound

# with open("data.json") as f:
#    data = json.load(f)
#
# starters = data["starters"]

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def store_pokemon(pokemon_name):
    with open("users_pokemon.json", "r") as f:
        users_data = json.load(f)
    users_data["users_pokemon"].append(pokemon_name)
    with open("users_pokemon.json", "w") as f:
        json.dump(users_data, f, indent=4)

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
        store_pokemon("Bulbasaur")
    elif starter_selection == "2":
        store_pokemon("Charmander")
    elif starter_selection == "3":
        store_pokemon("Squirtle")
    else:
        print("Invalid selection, please try again in a few seconds.")
        time.sleep(3)
        clear_screen()
        beginning()
        return

#chooses a random pokemon from a list to fight
def get_pokemon():
    with open("pokemon.json", "r") as f:
        data = json.load(f)
    pokemons = data["pokemon"]
    pokemon_name = random.choice(list(pokemons.keys()))
    details = pokemons[pokemon_name]
    return {
        "name": pokemon_name,
        "chance": details["chance"],
        "location": details["location"]
    }

def fight_system():
    clear_screen()
    wild = get_pokemon()
    print(f"A wild {wild['name']} appeared on {wild['location']}!")

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
