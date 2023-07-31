import os
import time
import random
import enum
import string


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=2):
    typewriter_simulator(message)
    time.sleep(delay)


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message, delay=2):
    print(Color.get_color() + message)
    time.sleep(delay)


def start():
    villian = random.choice(["wicked fairie", "dragon"])
    weapon = "dagger"

    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villian} is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")

    if(weapon == "dagger"):
        print_pause(f"In your hand you hold your"
                    f" trusty (but not very effective) {weapon}.")

    operation(villian, weapon)


def valid_input(message, options):
    value = input(message).lower()
    while(value not in options):
        value = input(message).lower()

    return value


def operation(villian, weapon):
    print("Enter 1 to knock on the door of the house")
    print("Enter 2 to peer into the cave")
    print("What would you like to do")

    option = valid_input("Please enter 1 or 2: ", ['1', '2'])
    while(option == '1'):
        house(villian, weapon)
    if(option == '2'):
        cave(villian, weapon)
    else:
        print("\n**** Please enter a valid option ****\n")
        operation(villian, weapon)


def house(villian, weapon):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the"
                f" door opens and out steps a {villian}!")
    print_pause(f"Eep! This is the {villian}'s house!")
    print_pause(f"The {villian} attacks you!")

    if(weapon == "dagger"):
        print_pause(f"You feel a bit under-prepared for"
                    f" this, what with only having a tiny {weapon}.")

    option2 = valid_input("Would you like to (1) fight,"
                          "or (2) run away? ", ['1', '2'])

    if(option2 == '1'):
        attack(villian, weapon)
        os._exit(0)
    elif(option2 == '2'):
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        operation(villian, weapon)
    else:
        print("\n**** Please enter a valid option ****\n")
        house(villian, weapon)


def cave(villian, weapon):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    weapon = "sword"
    print_pause("You discard your silly old dagger"
                " and take the sword with you.")
    print_pause("You walk back out to the field.")
    operation(villian, weapon)


def attack(villian, weapon):
    if(weapon == "sword"):
        print_pause(f"As the {villian} moves to attack,"
                    "you unsheath your new {weapon}.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause(f"But the {villian} takes one look at your"
                    " shiny new sword and runs away!")
        print_pause(f"You have rid the town of the {villian}."
                    "You are victorious!")

        replay()
    else:
        print_pause("\nYou do your best...")
        print_pause(f"but your {weapon} is no match for the {villian}.")
        print_pause("\nYou have been defeated!\n")

        replay()


def replay():
    option = valid_input("Would you like to play again? (y/n): ", ['y', 'n'])

    if(option == 'y'):
        print_pause("Excellent! Restarting the game ...")
        start()
    elif(option == 'n'):
        print_pause("Thanks for playing! See you next time.")
        os._exit(0)
    else:
        print("\n**** Please enter a valid option ****\n")
        replay()


start()
