from textGameFunctions import *


def Stage1(currentHP):
    name = str(input("\rEnter your character's name:\n"))
    print(f"{name}? ... {name}, wake up...")
    print("...")
    input("Press enter to wake up.\n")
    loading(2)
    print("\r* As you come to you are suddenly aware of the freezing sensation hugging your body. *"
          "\n* Though you are dazed you start to notice the world around you, you don't see much. *"
          "\n* You vaguely see dirt, darkness, and damp stone walls... and a cat? *\n")  # TODO reword and add aesthetic
    loading(5)
    input("\rPress enter to continue...")
    print(f"\nHey! {name}, you're awake! It's about time.")
    loading(2)
    print("\rListen, my name is s-")
    loading(1.3)
    print("\r...")
    loading(1.5)
    print("\rMy name is not important right now, what's important is that you're awake.")
    loading(3)
    print("\rYou have to get out of here, you've fallen into a deep hole")
    loading(2.6)
    print("\rand water is starting to seep through the earth..")
    loading(2.3)
    print("\rThe hole is flooding!\n")
    input("Press enter to continue...")
    print("\r* Studying the hole, it looks to be about 10 feet deep and large rocks protrude the walls. *"
          "\n* It might be possible to climb the rocks, though risky it may be the only way.. *"
          "\n* Then again, I could spend some time to see what is with the talking cat.. *\n")
    loading(3)
    input("\rPress enter to continue...\n")
    print(Color.PURPLE + "\r     {ACTION SYMBOL}")
    print("           ~8~\n" + Color.END)
    print("~ Whenever this symbol is shown," + Color.PURPLE + " ~8~ " + Color.END +
          "it means you will have to decide on an action ~")
    print("~ When a percentage is shown, like" + Color.YELLOW + " (50%)" + Color.END +
          ", it means there is a " + Color.YELLOW + "(50%)" + Color.END + " chance of succession ~\n")
    input("Press enter to continue...")
    print("\r")
    print(Color.PURPLE + "      ~8~ \n" + Color.END)
    print("Enter 1 to attempt to scale the wall " + Color.YELLOW + "  (30%)" + Color.END)
    print("Enter 2 to talk to the mysterious cat " + Color.YELLOW + " (100%)" + Color.END)
    while True:
        choice = int(input("Enter choice: "))
        if choice == 1 or choice == 2:
            break
        elif choice < 1 or choice > 2:
            print("Invalid entry, please try again: ")
            continue
        else:
            print("Enter a valid value, please try again: ")
            continue
    loading(1)

    if choice == 1:
        # Roll the odds to see if you are successful
        # oddsAction(RangeOfOdds ex 0-9 = 10, RangeOfWinning ex 0-6 = 70%)
        successful = oddsAction(9, 6)
        # If player has beat the odds, do this, or else that
        if successful:
            print("You gather what strength you have, nod to the cat, and begin to climb.")
            print("Gripping a large rock, just above your head to the left, planting your foot on another.")
            print("You lunge upwards to a hook-like rock and-\n")
            loading(1)
            input("\rPress enter to continue...")
            print("\rcatch enough of the rock to steadily raise yourself above the cusp of the hole.")
            print("You have made it out unscathed.")
            input("Press enter to continue...")
        else:
            print("You gather what strength you have, nod to the cat, and begin to climb.")
            print("Gripping a large rock, just above your head to the right, planting your foot on another.")
            print("You lunge upwards to a hook-like rock and-\n")
            loading(1)
            input("\rPress enter to continue...")
            print("\rswing your arm to catch the rock, but " + Color.BOLD + "miss." + Color.END)
            print("Falling backwards through the air like a nest-less bird, you manage to turn over")
            print("and brace most of your weight with your arms but you still impact the ground below.")
            # Call takeDamage function and set Health to Health - damage taken
            # takeDamage(CurrentHP, DamageTaken)
            currentHP = takeDamage(currentHP, 1)
            input("\rPress enter to continue...")

    if choice == 2:
        print("\rYou decide to not test your luck with this daunting wall but instead to speak to a cat..")
        print("Maybe the fall that got you in this hole has made you delirious or something but as far")
        print("as you know, this cat was talking. What should you say?\n")
        talkChoice = input("Enter text here: \n")
        helloList = ["Hello", "hello", "hi", "Hi", "Greetings", "greetings"]
        if any(x in talkChoice for x in helloList):
            print(Color.CYAN + "Is this really a time for greetings, " + name + "?!")
            print("You gotta get outta here!")
        else:
            print(Color.CYAN + "What? Anyways..")
        print("Follow me I know these rocks.\n")
        print(Color.END + "You gather what strength you have, nod to the cat and follow his lead.")
        print("The mysterious cat gives a warming meow and then leaps gracefully onward.")
        print("You watch the rocks the cat chooses and start your ascent.")
        print("Gripping a large rock, just above your head to the left, planting your foot on another.")
        print("You lunge upwards to a hook-like rock and-\n")
        loading(1)
        input("\rPress enter to continue...")
        print("\rcatch enough of the rock to steadily raise yourself above the cusp of the hole.\n"
              "You have made it out unscathed.\n"
              "Though over exertion has caught up with you and you cannot shake it,\n"
              "your eyes become so heavy and the grass beneath you feels as comfortable\n"
              "as ever..\n"
              "Just before you lose consciousness, you see that darn cat licking it's butthole.")
        input("Press enter to continue...")
        return currentHP, name


def Stage2(currentHP, name):
    print(Color.CYAN + f"{name}.")
    loading(1.5)
    print(f"\r{name}, wake up this is getting old.")
    print("...")
    input(Color.END + "Press enter to wake up..." + Color.CYAN)
    loading(1)
    print(f"\rYou look like sh** {name}, you should eat something.")
    loading(1)
    print("\rHere, I found this squirrel. Well actually I hunted it while you slept for\n"
          "5 hours and I watched it play dead for 2 of the hours. Stupid squirrel.\n"
          "It's dead now, I'm surprised I didn't die of boredom to be honest. Here, take it.\n")
    loading(3)
    print(Color.END + "\r* The cat giddily prances over to you with, yup, a dead squirrel in it's mouse *\n")
    print("Eat the dead squirrel?\n")
    input("Press enter to continue...")
    loading(0.5)
    print(Color.PURPLE + "\r      ~8~ \n" + Color.END)
    loading(0.5)
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
            print("You eat the dead squirrel.")
            currentHP = heal(currentHP, 1)
            # TODO Write more flavour
        else:
            print("The dead squirrel is not sitting right..... Ouch.")
            currentHP = takeDamage(currentHP, 1)
            # TODO Write more flavour

    return currentHP
