from textGameFunctions import *


def Stage1(currentHP):
    name = str(input("\rEnter your character's name:\n"))
    print(f"{name}? ... {name}, wake up...")
    print("...")
    input("Press enter to wake up.\n")
    loading(0.5)
    print("\r* As you come to you are suddenly aware of the freezing sensation hugging your body. *"
          "\n* Though you are dazed you start to notice the world around you, you don't see much. *"
          "\n* You vaguely see dirt, darkness, and damp stone walls... and a cat? *\n")  # TODO reword and add aesthetic
    loading(1)
    input("\rPress enter to continue...")
    print(f"\nHey! {name}, you're awake! It's about time.")
    loading(0.5)
    print("\rListen, my name is s-")
    loading(1)
    print("\r...")
    loading(0.8)
    print("\rMy name is not important right now, what's important is that you're awake.")
    loading(1)
    print("\rYou have to get out of here, you've fallen into a deep hole")
    loading(1.2)
    print("\rand water is starting to seep through the earth..")
    loading(1.3)
    print("\rThe hole is flooding!\n")
    input("Press enter to continue...")
    print("\r* Studying the hole, it looks to be about 10 feet deep and large rocks protrude the walls. *"
          "\n* It might be possible to climb the rocks, though risky it may be the only way.. *"
          "\n* Then again, I could spend some time to see what is with the talking cat.. *\n")
    loading(1)
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
        talkChoice = input("Greet the cat: \n")
        print(Color.YELLOW + talkChoice + "\n")
        talkChoice = talkChoice.lower()
        # TODO Add more dynamic situational conversation if/else(s)
        helloList = ["hello", "hi", "greetings", "hey"]
        if any(x in talkChoice for x in helloList):
            print(Color.CYAN + "Is this really a time for greetings, " + name + "?!")
            print("You gotta get outta here!")
        else:
            print(Color.CYAN + "What? Anyways..")
        print("Follow me I know these rocks.\n")
        input(Color.END + "Press enter to continue...")
        print("\rYou gather what strength you have, nod to the cat and follow his lead.")
        loading(1)
        print("\rThe mysterious cat gives a warming meow and then leaps gracefully onward.")
        loading(1)
        print("\rYou watch the rocks the cat chooses and start your ascent.")
        print("Gripping a large rock, just above your head to the left, planting your foot on another.")
        print("You lunge upwards to a hook-like rock and-")
        input("Press enter to continue...")
        print("\n-catch enough of the rock to steadily raise yourself above the cusp of the hole.\n"
              "You have made it out unscathed, though, over exertion has caught up with you and you cannot shake "
              "it.\n\n "
              "Your eyes become so heavy and the grass beneath you feels as comfortable\n"
              "as ever..\n\n"
              "Just before you lose consciousness, you see that darn cat licking it's butthole.\n")
        input("Press enter to continue...")
        return currentHP, name
