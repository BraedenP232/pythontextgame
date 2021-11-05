from textGameFunctions import *

# Variable Declarations
fork = 0


def Stage2(currentHP, name):
    print(Color.CYAN + f"{name}.")
    loading(1.5)
    print(f"\r{name}, wake up this is getting old.")
    print("...")
    input(Color.END + "Press enter to wake up..." + Color.CYAN)
    loading(1)
    print(f"\r\nYou look like sh** {name}, you should eat something.")
    loading(1)
    print("\r\nHere, I found this squirrel. Well actually I hunted it while you slept for\n"
          "5 hours and I watched it play dead for 2 of the hours. Stupid squirrel.\n"
          "It's dead now, I'm surprised I didn't die of boredom to be honest. Here, take it.\n")
    input("Press enter to continue...")
    print(Color.END + "\r\n* The cat giddily prances over to you with, yup, a dead squirrel in it's mouth *\n")
    print("Eat the dead squirrel?\n")
    input("Press enter to continue...")
    loading(0.5)
    print(Color.PURPLE + "\r      ~8~ \n" + Color.END)
    loading(0.5)
    print("       You have " + Color.RED + str(currentHP) + "/5 " + Color.END + "health points")
    print("\rEnter 1 to eat the dead squirrel " + Color.YELLOW + "     (50%)" + Color.END)
    print("Enter 2 to not eat the dead squirrel")
    while True:
        choice = int(input("Enter choice: "))
        if choice == 1 or choice == 2:
            break
        else:
            print("Invalid entry, please try again: ")
            continue
    loading(1)
    if choice == 1:
        # Roll the odds to see if you are successful
        # oddsAction(RangeOfOdds ex 0-9 = 10, RangeOfWinning ex 0-4 = 50%)
        successful = oddsAction(9, 4)
        # If player has beat the odds, do this, or else that
        if successful:
            global fork
            fork = 1
            print("With hesitation, you proceed to eat the dead mammal.\n"
                  "You think to yourself, \"It's human nature.. This is "
                  "what my ancestors did. Here goes nothing.\"\n")
            loading(1)
            input("\rPress enter to continue...")
            print("\rYou feel a little disturbed but the hunger has subsided for now.\n")
            currentHP = heal(currentHP, 1)
        else:
            fork = 2
            print("With hesitation, you proceed to eat the dead mammal.\n"
                  "You think to yourself, \"It's human nature.. This is "
                  "what my ancestors did. Here goes nothing.\"\n")
            loading(1)
            input("\rPress enter to continue...")
            print("\rSomething about either the mammal corpse, or your sanity, is not okay.\n"
                  "You exhale what remnants of the squirrel you could.\n"
                  "Meanwhile, the cat looks at the remains yearningly..")
            currentHP = takeDamage(currentHP, 1)
    if choice == 2:
        print("You thank the cat for the kind gesture, pat his head, and\n"
              "kindly refuse. Raw dead mammals just aren't your thing.\n")
        print(Color.CYAN + "You sure? Alright, more for me then!" + Color.END)
        print("You take a seat on a nearby stump to catch your breath while the cat\n"
              "picks up the mammal corpse with it's front teeth and finds a comfy\n"
              "nook to consume the mongrel.")
    loading(5)
    input("\r\nPress enter to continue...\n")
    print("Now that you have recouped, you have a chance to look around or start moving forward,")
    loading(1)
    print("\ror ask the cat some questions.\n")
    input("Press enter to continue...")
    loading(1)
    print(Color.PURPLE + "\r      ~8~ \n" + Color.END)

    loading(0.5)
    while True:
        print(Color.END + "\rEnter 1 to look around")
        print("Enter 2 to speak to the cat")
        print("Enter 3 to move forward\n")
        print(Color.PURPLE + "You can look around and speak to the cat as much as you want.\n"
                             "If you move forward, you will not be able to choose other options." + Color.END)
        while True:
            choice = int(input(Color.END + "\rEnter choice: "))
            if choice == 1 or choice == 2:
                print("\r")
                break
            elif choice == 3:
                break
            else:
                print("\rInvalid entry, please try again: ")
                continue

        if choice == 1:
            print("You decide to look around you and acknowledge the environment.")
            input("\rPress enter to continue...")
            print("\r* The trees in the dark forest were nicotine-brown. *"
                  "* The musty air was difficult to breathe. The forest was old *\n"
                  "* and otherworldly. Oxblood-red toadstools littered the ground. *"
                  "* Poisonous cowbane grew next to them. *\n"
                  "* An acrid odour hung off everything. Its a teeth-gritting experience. *\n\n"
                  "~ How did I end up here? Why can't I remember anything. Who am I? ~\n")
            input("Press enter to continue...")
            continue
        if choice == 2:
            print("You walk over to the calico cat,")
            if fork == 0:
                print(" whom has finished with the dead squirrel and is\n"
                      "now cleaning themself. They briefly pause with one paw\n"
                      "mid brush when you approach, but continue their business\n"
                      "shortly after.")
            if fork == 1:
                print(" whom seems to be taking a catnap. The cat's ears prick\n"
                      "up as you approach.")
            if fork == 2:
                print(" whom seems to be sniffing your vomit again but it seems\n"
                      "even THAT is too gross for this cat. The cat sits attentively\n"
                      "when you approach.")
                input("Press enter to continue...")
            print(Color.CYAN + "Well would you look at that, you made it out alive\n"
                               "and in one piece. You're welcome.")
            if fork == 0:
                print("Too bad you didn't want that squirrel, it was delicious." + Color.END)
            if fork == 1:
                print("Hope that squirrel was good, it looked delicious." + Color.END)
            if fork == 2:
                print("In hindsight, I think I would have enjoyed that delicious\n"
                      "squirrel more. Oh well." + Color.END)
            print(Color.RED + "\nFor testing purposes, only say a greeting or a gratitude phrase." + Color.END)
            talkChoice = input("What should I say: ")
            talkChoice = talkChoice.lower()
            # TODO Add more dynamic situational conversation if/else(s)
            gratitudeList = ["thank", "thx", "ty", "gratitude", "appreciate", "appreciation"]
            helloList = ["hello", "hi", "greetings", "hey", "suh", "sup", "howdy", "waddup", "ay"]
            # To make all of the cat's following text CYAN
            print(Color.CYAN + "")
            if any(x in talkChoice for x in helloList):
                print("Yo, " + name + ".")
                print("What's up?")
                input("Press enter to continue...")
                continue
            elif any(x in talkChoice for x in gratitudeList):
                print("No problem, " + name + ". I didn't doubt you for a second.")
                input("Press enter to continue...")
                continue
            else:
                input("Press enter to continue...")
                continue
        if choice == 3:
            print(Color.END + "You start walking and-")
            print(Color.RED + "The END for now.." + Color.END)
            input("Press enter to continue...")

            break

        return currentHP, name
