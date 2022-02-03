"""
This file is for my Code Institute Diploma in
Software Development (E-commerce Applications).
This is my Portfolio Project 3 (Python).
It is a CLI python hangman game.
"""
import random
import os


def clear():
    """
    This function clears the CLI
    """
    os.system("clear")


def print_hangman(values):
    """
    This function adds the body parts
    to the hangman graphic when the
    user has an incorrect guess.
    """
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5], values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()


def print_hangman_win():
    """
    This function prints a
    graphic to show that the
    user has won.
    """
    print()
    print("\t +--------+")
    print("\t         | |")

    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()


def print_word(values):
    """
    This function displays the
    word/phrase to the user.
    """
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()


def check_win(values):
    """
    This function checks if the
    user has won the game or not.
    """
    for character in values:
        if character == "-":
            return False
    return True


def hangman_game(word):
    """
    This function is the main function
    for the hangman game. It displays
    the word, checks the user inputs,
    and creates graphics for each incorrect
    guess or when the user wins.
    """
    clear()
    word_display = []
    correct_letters = []
    incorrect_letters = []
    guesses = 0
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # If the character is not a letter e.g "'" or " "
    # It is displayed as itself.
    for character in word:
        if character.isalpha():
            word_display.append('-')
            correct_letters.append(character.upper())
        else:
            word_display.append(character)
    # Shows the word and the incorrect guesses list.
    while True:
        clear()
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print("Incorrect Guessues: ", incorrect_letters)
        print()

        # Takes the user's guess
        guess = input("Guess a letter: ")
        # Checks if the guess is one letter
        if len(guess) != 1:
            clear()
            print("Invalid guess, try one letter a time!")
            continue
        # Checks if the guess is a letter
        if not guess[0].isalpha():
            clear()
            print("Invalid guess, English letters only!")
            continue
        # Checks if the letter has already been guessed
        if guess.upper() in incorrect_letters:
            clear()
            print(f"You have already guessed {guess.upper()}!")
            continue

        # Adds incorrect guesses to the list
        if guess.upper() not in correct_letters:
            incorrect_letters.append(guess.upper())
            show_hangman_values[guesses] = hangman_values[guesses]
            guesses = guesses + 1
            # Checks if the user is out of lives
            if guesses == len(hangman_values):
                print()
                clear()
                print("\tGame Over!")
                print_hangman(hangman_values)
                print(f"The answer was: {word.upper()}")
                break
        # Checks if the user has won the game
        else:
            for i in range(len(word)):
                if word[i].upper() == guess.upper():
                    word_display[i] = guess.upper()
            if check_win(word_display):
                clear()
                print("\tCongratulations! You won!")
                print_hangman_win()
                print(f"The answer was: {word.upper()}")
                break

# This is used to execute the code.
if __name__ == "__main__":
    clear()

    # The 3 different game modes that the user can play
    game_modes = {1: "Easy", 2: "Hard", 3: "Phrases"}

    # The different answers in the different game modes
    dataset = {"Easy": ["Bake", "Word", "List", "Four", "Five", "Nine", "Good", "Best", "Cute", "Zero", "Huge", "Cool", "Tree", "Race", "Rice", "Keep", "Lace", "Beam", "Game", "Mars", "Tide", "Ride", "Hide", "Exit", "Hope", "Cold", "From", "Need", "Stay", "Come", "Cramp", "Fudge", "Drink", "Grown", "Swamp", "Threw", "Right", "Still", "Petal", "Fibre", "Dread", "Crust", "Ditch", "Nomad", "Peach", "Speak", "Tramp", "Grand", "Fancy", "Dingo", "Worse", "Unite", "Ulcer", "Groom", "Thorn", "Doubt", "Qualm", "Bound", "Gauze", "Curve"],
               "Hard": ["Inched", "Cookie", "Haggle", "Pinned", "Attend", "Boiled", "Rasped", "Glance", "Dampen", "Zealot", "Mantle", "Excess", "Drench", "Having", "Chrome", "Jogger", "Plural", "Expire", "Browse", "Urchin", "Amazing", "Seaweed", "Opposed", "Messiah", "Traffic", "Changed", "Hunting", "Caliber", "Auditor", "Handled", "Dairies", "Shuttle", "Respect", "Minting", "Trumpet", "Proposal", "Nebulous", "Somberly", "Reprieve", "Accepted", "Trombone", "Dynamite", "Fraudful", "Lounging", "Juvenile", "Advising", "Dispense", "Portrait", "Nihilist", "Anchored", "Associate", "Scuffing", "Explosion", "Cynically", "Excelling", "Intercept", "Monstrous", "Wandering", "Apparatus", "Paralytic"],
               "Phrases": ["Hard Pill to Swallow", "Top Drawer", "Man of Few Words", "Back To the Drawing Board", "Curiosity Killed The Cat", "Beating a Dead Horse", "Fish Out Of Water", "In a Pickle", "Fit as a Fiddle", "In the Red", "Close But No Cigar", "A Dime a Dozen", "Wild Goose Chase", "Right Off the Bat", "No-Brainer", "A Little from Column A, a Little from Column B", "High And Dry", "Between a Rock and a Hard Place", "Knock Your Socks Off", "You Can't Teach an Old Dog New Tricks"]
               }

    # This displays a menu for the game
    # Allows the user to choose a mode or quit
    while True:
        print()
        print("--------------------------")
        print("\tGAME MENU")
        print("--------------------------")
        for key in game_modes:
            print("Press", key, "to select", game_modes[key])
            print("Press", len(game_modes) + 1, "to quit.")
            print()
        try:
            mode_select = int(input("Enter your preferred game mode: "))
        except ValueError:
            clear()
            print("Invalid input. Try again!")
            continue

        if mode_select > len(game_modes) + 1:
            clear()
            print("Invalid selction. Try again!")
            continue
        elif mode_select == len(game_modes) + 1:
            print()
            print("Thank you for playing hangman!")
            break

        # Stores the user's choice of mode
        game_mode = game_modes[mode_select]
        # Stores the current word/phrase
        word = random.choice(dataset[game_mode])
        # Executes the game function
        hangman_game(word)
