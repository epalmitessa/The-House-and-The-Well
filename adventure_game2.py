import time
import random
weapon = random.choice(["amulet", "birch wand", "Heaven's sword"])
items = [weapon]

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You find yourself on a tree-lined, dead end street.")
    print_pause("The leaves wave above you, seemingly whispering, but you can't understand.")
    print_pause("In front of you is a grand, long abandoned house.")
    print_pause("At the end of the lane is an ancient stone well.")

    print_pause("Enter 1 to open the door of the house.")
    print_pause("Enter 2 to peer down into the well.")

def creepy_house():
        print_pause("You open the door and slowly step into the house.")
        print_pause("You gaze around; a hundred years' worth of dust covers everything, "
        "and an air of decay pervades the room.")
        print_pause("You notice a thin, leather bound book resting at the bottom "
        "of the staircase.")
        print_pause("You open to the first page and see a phrase "
        "written in what appears to be Latin.")
        print_pause("You slowly read the words, 'i vocare te'.")
        print_pause("Suddenly, the air swirls with rage, "
        "and an angry demon emerges to devour you.")

        if "amulet" in items:
            print_pause("Instinctually, you grab the amulet out of your pocket.")
            print_pause("The sight of it seems to stun the demon, and suddenly "
            "you find yourself shouting, 'EGO TE AMO'")
            print_pause("The demon shrieks and is sucked into the amulet.")
            print_pause("The amulet glows red in your hands as you look down.")
            print_pause("You let out a deep sigh and exit the house, triumphant.")


        elif "birch wand" in items:
            print_pause("Instinctually, the grab the birch wand from your pocket.")
            print_pause("The wand glows gold as you scream 'SOL ORIENS SUM'")
            print_pause("The demon shrieks as it rends apart and leaves sun-shot dust floating.")
            print_pause("You let out a deep sigh and exit the house, triumphant.")


        elif "Heaven's sword" in items:
            print_pause("Instinctually, you grab Heaven's sword from your side.")
            print_pause("The sword glows with a celestial light as you raise it above your head.")
            print_pause("You bring the sword down, splitting through the demon.")
            print_pause("The hellish entity screams and collapses to the ground, "
            "leaving its limp form behind.")
            print_pause("You let out a deep sigh and exit the house, triumphant.")


        else:
            print_pause("You scream and leave the house, running away as fast as you can.")

def spooky_well():
        print_pause("You stare into the well and "
        "notice a set of stairs along its edge.")
        print_pause("You descend into the darkness, fear washing over you.")
        print_pause("You reach the bottom to find the well is dry; "
        "something tells you to run your hands along the earth.")
        print_pause("Suddenly, your fingers close around an object.")
        print_pause("You clutch it and climb back into the light.")
        items.append("weapon")



def choose_path():
    path = input("What would you like to do? Please enter 1 or 2.\n")
    if path == '1':
        creepy_house()
    elif path == '2':
        spooky_well()
    else:
        print_pause("I'm sorry, I don't understand.")




def play_again():

    print_pause("Would you like to: "
              " 1. play again or\n"
              " 2. exit?\n")
    print_pause("Please enter 1 or 2")

    choice == input("1. play again or\n"
                    "2. exit?\n")
    if choice == '1':
        play_game()

    if choice == '2':
        exit()

    else:
        print_pause("I'm sorry, I don't understand.")

def play_game():
    items = [weapon]
    intro()
    choose_path()
    play_again()

play_game()
