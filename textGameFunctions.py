# IMPORT STATEMENTS
import itertools
import secrets
import sys
import threading
import time

from color import *


def loading(duration):
    done = False

    # here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\r- ' + c + ' - ')
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(duration)
    done = True


def takeDamage(Health, dmgTaken):
    print("You take " + Color.RED + str(dmgTaken) + " damage" + Color.END + " and now have "
          + Color.RED + str(Health - dmgTaken) + "/5 " + Color.END + "health points")
    return Health - dmgTaken


def heal(Health, amount):
    if Health < 5:
        print("You heal " + Color.GREEN + str(amount) + " HP" + Color.END + " and now have "
              + Color.RED + str(Health + amount) + "/5 " + Color.END + "health points")
        return Health + amount
    else:
        print("You are at full health - " + Color.GREEN + str(Health) + "/5 " + Color.END + "health points")
        return Health


def oddsAction(randrange, oddsToBeat):
    odds = secrets.randbelow(randrange)
    if odds > oddsToBeat:
        print("Succeeded Action\n")
        oddsBeat = True
    else:
        print("Failed Action\n")
        oddsBeat = False
    return oddsBeat
