import random
import os


def clear():
    os.system("cls")


if __name__ == "__main__":
    clear()

    game_modes = {1: "Easy", 2: "Hard", 3: "Phrases"}

    dataset = {"Easy": ["Bake", "Word", "List", "Four", "Five", "Nine", "Good", "Best", "Cute", "Zero", "Huge", "Cool", "Tree", "Race", "Rice", "Keep", "Lace", "Beam", "Game", "Mars", "Tide", "Ride", "Hide", "Exit", "Hope", "Cold", "From", "Need", "Stay", "Come", "Cramp", "Fudge", "Drink", "Grown", "Swamp", "Threw", "Right", "Still", "Petal", "Fibre", "Dread", "Crust", "Ditch", "Nomad", "Peach", "Speak", "Tramp", "Grand", "Fancy", "Dingo", "Worse", "Unite", "Ulcer", "Groom", "Thorn", "Doubt", "Qualm", "Bound", "Gauze", "Curve"],
               "Hard": ["Inched", "Cookie", "Haggle", "Pinned", "Attend", "Boiled", "Rasped", "Glance", "Dampen", "Zealot", "Mantle", "Excess", "Drench", "Having", "Chrome", "Jogger", "Plural", "Expire", "Browse", "Urchin", "Amazing", "Seaweed", "Opposed", "Messiah", "Traffic", "Changed", "Hunting", "Caliber", "Auditor", "Handled", "Dairies", "Shuttle", "Respect", "Minting", "Trumpet", "Proposal", "Nebulous", "Somberly", "Reprieve", "Accepted", "Trombone", "Dynamite", "Fraudful", "Lounging", "Juvenile", "Advising", "Dispense", "Portrait", "Nihilist", "Anchored", "Associate", "Scuffing", "Explosion", "Cynically", "Excelling", "Intercept", "Monstrous", "Wandering", "Apparatus", "Paralytic"],
               "Phrases": ["Hard Pill to Swallow", "Top Drawer", "Man of Few Words", "Back To the Drawing Board", "Curiosity Killed The Cat", "Beating a Dead Horse", "Fish Out Of Water", "In a Pickle", "Fit as a Fiddle", "In the Red", "Close But No Cigar", "A Dime a Dozen", "Wild Goose Chase", "Right Off the Bat", "No-Brainer", "A Little from Column A, a Little from Column B", "High And Dry", "Between a Rock and a Hard Place", "Knock Your Socks Off", "You Can't Teach an Old Dog New Tricks"]
               }

    while True:
        print()
        print("--------------------------")
        print("\tGAME MENU")
        print("--------------------------")
        for key in game_modes:
            print("Press", key, "to select", game_modes[key])
            print("Press", len(game_modes) + 1, "to quir.")
            print()
